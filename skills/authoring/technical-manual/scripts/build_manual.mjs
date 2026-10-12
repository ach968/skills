#!/usr/bin/env node
import { existsSync } from "node:fs";
import { access, mkdir, writeFile } from "node:fs/promises";
import { createRequire } from "node:module";
import { dirname, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const usage = `Usage: node scripts/build_manual.mjs [options]
  --input FILE          Source HTML (default: assets/starter.html)
  --output FILE.pdf     Output PDF (default: output/manual.pdf)
  --node-modules DIR    Local Paged.js and Playwright directory
  --browser-path PATH   Chromium executable (or MANUAL_BROWSER_PATH)
  --pagedjs PATH        Paged.js polyfill (or MANUAL_PAGEDJS_PATH)
  --help                Show this help`;
const args = process.argv.slice(2);
if (args.includes("--help")) { console.log(usage); process.exit(0); }
const known = new Set(["--input", "--output", "--node-modules", "--browser-path", "--pagedjs"]);
for (let i = 0; i < args.length; i += 1) if (args[i].startsWith("--") && (!known.has(args[i]) || !args[i + 1] || args[i + 1].startsWith("--"))) throw new Error(`Invalid option: ${args[i]}\n${usage}`);
const option = (name, fallback) => { const i = args.indexOf(name); return i < 0 ? fallback : args[i + 1]; };
const root = resolve(import.meta.dirname, "..");
const input = resolve(option("--input", resolve(root, "assets/starter.html")));
const output = resolve(option("--output", resolve(root, "output/manual.pdf")));
if (!output.toLowerCase().endsWith(".pdf")) throw new Error(`--output must end in .pdf: ${output}`);
const modules = resolve(option("--node-modules", process.env.MANUAL_NODE_MODULES || resolve(root, "node_modules")));
const browserPath = option("--browser-path", process.env.MANUAL_BROWSER_PATH);
const pagedjs = resolve(option("--pagedjs", process.env.MANUAL_PAGEDJS_PATH || resolve(modules, "pagedjs/dist/paged.polyfill.js")));
if (!existsSync(pagedjs)) throw new Error(`Cannot find Paged.js 0.4.x. Run setup_renderer.mjs --node-modules ${modules}`);
if (!existsSync(output) && !output.endsWith(".pdf")) throw new Error("PDF output required");
await access(input); await mkdir(dirname(output), { recursive: true });
let playwright;
try { playwright = createRequire(resolve(modules, "..", "package.json"))(resolve(modules, "playwright")); }
catch { throw new Error(`Cannot find Playwright. Run setup_renderer.mjs --node-modules ${modules}`); }

const browser = await playwright.chromium.launch({ headless: true, executablePath: browserPath || undefined, args: ["--allow-file-access-from-files"] });
const consoleErrors = [];
let diagnostics;
try {
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  page.on("console", message => { if (message.type() === "error") consoleErrors.push(message.text()); });
  page.on("pageerror", error => consoleErrors.push(error.message));
  await page.goto(pathToFileURL(input).href, { waitUntil: "load" });
  await page.evaluate(() => { window.PagedConfig = { auto: false }; });
  await page.addScriptTag({ path: pagedjs });
  await page.evaluate(async () => { await document.fonts.ready; await window.PagedPolyfill.preview(); await document.fonts.ready; document.querySelectorAll("body>:not(.pagedjs_pages)").forEach(el => { el.style.display = "none"; }); });
  await page.waitForSelector(".pagedjs_page");
  diagnostics = await page.evaluate(() => ({ pageCount: document.querySelectorAll(".pagedjs_page").length, splitTables: [...new Set([...document.querySelectorAll(".pagedjs_page table[data-split-from]")].map(table => table.dataset.ref))], missingAssets: [...document.images].filter(img => !img.complete || !img.naturalWidth).map(img => img.currentSrc || img.src), overflowing: [...document.querySelectorAll("figure,table,pre")].filter(el => el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2).map(el => el.tagName.toLowerCase()), replaceMarkers: document.querySelectorAll(".replace").length }));
  await page.pdf({ path: output, format: "Letter", printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
} finally { await browser.close(); }
const report = { input, output, pagedjs, ...diagnostics, consoleErrors, success: !diagnostics.missingAssets.length && !diagnostics.overflowing.length && !diagnostics.splitTables.length && !consoleErrors.length };
await writeFile(output.slice(0, -4) + ".report.json", JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify(report, null, 2));
if (diagnostics.splitTables.length) console.error("Split table detected. Author smaller continuation tables; Paged.js cannot safely repeat headers after layout.");
if (!report.success) process.exitCode = 1;
