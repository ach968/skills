#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { mkdir } from "node:fs/promises";
import { basename, dirname, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const usage = `Usage: node scripts/setup_renderer.mjs --node-modules DIR

Installs Paged.js 0.4.3 and Playwright 1.63.0 into a project-local directory.
Use .renderer/node_modules; never point this at a bundled runtime directory.

Options:
  --node-modules DIR    Local dependency directory (default: node_modules)
  --help                Show this help`;
const args = process.argv.slice(2);
if (args.includes("--help")) { console.log(usage); process.exit(0); }
for (let i = 0; i < args.length; i += 1) {
  if (args[i] !== "--node-modules" || !args[i + 1] || args[i + 1].startsWith("--")) throw new Error(`Invalid option: ${args[i]}\n${usage}`);
  i += 1;
}
const i = args.indexOf("--node-modules");
const modules = resolve(i >= 0 ? args[i + 1] : process.env.MANUAL_NODE_MODULES || "node_modules");
if (basename(modules) !== "node_modules") throw new Error("--node-modules must name a node_modules directory, for example work/renderer/node_modules.");
await mkdir(modules, { recursive: true });
const installedVersion = (name) => {
  try { return JSON.parse(readFileSync(resolve(modules, name, "package.json"), "utf8")).version; }
  catch { return null; }
};
if (existsSync(resolve(modules, "pagedjs/dist/paged.polyfill.js")) && installedVersion("pagedjs") === "0.4.3" && installedVersion("playwright") === "1.63.0") {
  console.log(`Renderer dependencies already available in ${modules}`);
  process.exit(0);
}
const npm = process.platform === "win32" ? "npm.cmd" : "npm";
const result = spawnSync(npm, ["install", "--no-save", "--prefix", dirname(modules), "pagedjs@0.4.3", "playwright@1.63.0"], { stdio: "inherit" });
process.exit(result.status ?? 1);
