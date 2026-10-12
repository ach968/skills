# Skills

My collection of reusable agent skills, organized by subject.

## Install

```sh
npx skills@latest add ach968/skills
```

Select the skills and installation scope prompted by the installer. Skills remain individually named by the `name` field in their SKILL.md, independent of category folders.

## Categories

### Authoring
| Skill | Purpose |
| --- | --- |
| [technical-manual](skills/authoring/technical-manual/SKILL.md) | Research, write, illustrate and verify dense, source-grounded PDF manuals. Includes an HTML/PDF renderer and reproducible evidence workflow. |

### Sports research
| Skill | Purpose |
| --- | --- |
| [nfl-deep-dd](skills/sports-research/nfl-deep-dd/SKILL.md) | Research NFL matchups and market prices with injuries, scheme analysis, reproducible probability models, trade execution and retrospective audits. |

## Contributing

Place each skill at `skills/<category>/<skill-name>/SKILL.md` and keep the skill's supporting `references/`, `scripts/`, `templates/` and `assets/` inside its own directory. Use a short lowercase kebab-case category and skill name. Add the skill to the category table above. Use descriptive metadata in SKILL.md so installers and coding agents discover it. Categories are organizational only; do not include categories in the skill's `name` field.

Keep generated documents, dependencies and private research outside skills. Bundled fonts in technical-manual retain their original SIL Open Font Licenses and attribution files. Previous `skills/technical-manual` path moved to `skills/authoring/technical-manual`; update hard-coded paths in external tooling.
