# Skills

My collection of reusable agent skills.

## Install

```sh
npx skills@latest add ach968/skills
```

The installer lets you choose skills, agents, and installation scope.

## Available skills

| Skill | Purpose |
| --- | --- |
| [technical-manual](skills/technical-manual/SKILL.md) | Research, write, illustrate, and verify dense PDF manuals on any topic. Includes dark and light cover styles, an HTML/PDF renderer, and a reproducible evidence workflow. Inspired by [Caleb Fahlgren's post about learning with dense, source-grounded manuals](https://x.com/calebfahlgren/status/2104283566746329132). |

## Adding skills

Place each skill in `skills/<skill-name>/`, with a `SKILL.md` entrypoint and any references, scripts, or assets it needs. Keep generated documents, dependencies, and private working material outside the skill directory.

Bundled fonts retain their accompanying SIL Open Font Licenses and attribution files in `skills/technical-manual/assets/fonts/`.
