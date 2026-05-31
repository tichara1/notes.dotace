# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **content repository**, not a software project. It holds Czech-language Markdown
notes for planning a house renovation funded by the **Nová zelená úsporám 2026+**
grant. It is published as a GitHub Pages site using the `just-the-docs` theme via
`remote_theme` — there is **no local build, no CI, no scripts, no dependencies**.
You edit `.md` files; GitHub renders them.

Content language is **Czech**. Match it — keep notes, headings, and table labels in
Czech unless the user asks otherwise.

## Structure

Numbered top-level folders (`01-` … `06-`) define both the reading order and the
nav order. Each section folder has an `index.md` (the section landing page) plus
content pages. The numbering scheme is intentional — preserve it when adding files.

- `01-prehled/` — scope, priorities, timeline
- `02-dotace/` — NZÚ 2026+ overview, required documents, financing (grant vs. loan)
- `03-specialiste/` — energy specialist, contacted parties
- `04-realizace/` — execution: contractor vs. subcontractors, RFQs, bid comparison
- `05-rozpocet/` — budget
- `06-dokumenty/` — meeting log and document links
- `docs/superpowers/specs/` — design specs (the structure rationale lives here)

## just-the-docs front matter conventions

Every page needs YAML front matter. The theme builds the sidebar from it — get this
wrong and nav ordering/grouping breaks.

- **Section `index.md`**: `title`, `nav_order`, `has_children: true`.
- **Content page**: `title`, `parent: <exact title of the section index>`, `nav_order`.
- `parent` must match the parent page's `title` string exactly.
- `nav_order` is scoped within its parent; folder numbers and `nav_order` are kept in sync.

Example content page:
```yaml
---
title: Cíl a rozsah
parent: Přehled
nav_order: 1
---
```

## Conventions

- **Internal links use `.html`, not `.md`** (e.g. `[Harmonogram](harmonogram.html)`) —
  Jekyll outputs `.html`. Follow the existing pattern.
- Pages are **skeletons**: prepared headings, empty tables, and checklists the user
  fills in over time. When adding a page, follow this style — provide structure, not
  invented content. Don't fabricate grant figures, contacts, or budget numbers.
- Checklist items: `- [ ]` open, `- [x]` done.
- Placeholder prompts use blockquote italics: `> _what to fill in here…_`.

## Working rules

- **Personal data:** this repo is published as a **public GitHub Pages site**. Before
  committing/pushing anything that contains personal or sensitive data (incomes,
  exact salaries, birth dates, ID numbers, private contacts), **stop and ask the
  user first** — or leave it out. Aggregated/qualitative conclusions (e.g. "above
  the 4th income decile") are fine; raw personal figures are not.
- **Refresh all pages:** at the end of a task, do a quick review pass over **all**
  pages — check front matter, `.html` links, nav ordering, and cross-links, and fix
  anything that the task's changes left inconsistent.
- **Commit & push:** at the end of every task, **commit and push** the changes.
