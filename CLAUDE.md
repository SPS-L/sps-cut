# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hugo static site for the Sustainable Power Systems Laboratory (SPS Lab) at Cyprus University of Technology. Uses Hugo Blox Builder (Academic theme) with Go modules. Deployed on Netlify; also has a GitHub Pages workflow.

## Development Commands

```bash
# Local dev server (with drafts)
hugo server -D
# Served at http://localhost:1313

# Production build
hugo --gc --minify

# Fetch/update Hugo modules
hugo mod get

# Clean module cache
hugo mod clean
```

Hugo version: **0.135.0** (extended). Go 1.15+. Node 22 (for Netlify build environment).

## Architecture

### Content Types

All content lives under `content/` as Markdown with YAML frontmatter:

- **`publication/`** — 129+ entries. Named `YearAuthorType/` (e.g. `2024JTherapontos/`). Auto-generated from `publications.bib` via GitHub Actions workflow (`import-publications.yml`) using `academic import`. Do not hand-edit generated files; update the `.bib` instead.
- **`authors/`** — Team member profiles. Each is a directory with `_index.md` and `avatar.jpg`. Author slugs use format `first-initial.-lastname` (e.g. `p.-aristidou`).
- **`project/`** — Research projects. Filtered on homepage by tags: `themes`, `Current projects`, `Software tools`, `Past projects`.
- **`post/`** — Blog posts.
- **`courses/`** — Teaching materials (EEN320, EEN442, EEN452).

### Homepage (`content/_index.md`)

Single-page landing using Hugo Blox `sections` blocks: hero, about, news, recent posts, research portfolio, publications, sponsor logos, contact. The news section reads from `content/newslist.dat` via the `readfromfile` shortcode.

### Custom Layouts

- `layouts/shortcodes/readfromfile.html` — Reads a file and renders first N lines as Markdown. Used for news list on homepage.
- `layouts/shortcodes/rawhtml.html` — Passes raw HTML through.
- `layouts/partials/blocks/logos.html` — Renders sponsor logos from `assets/media/sponsors/`.
- `layouts/partials/custom_head.html` — Injects Plum X widgets script.

### Configuration

All Hugo config is in `config/_default/`:
- `hugo.yaml` — Core settings, taxonomies, permalinks, output formats
- `params.yaml` — Theme appearance, analytics, CMS settings
- `menus.yaml` — Navigation links (most point to homepage anchor sections)
- `languages.yaml` — English only
- `module.yaml` — Hugo Blox module imports (blox-bootstrap, decap-cms plugin, netlify plugin)

### Module Dependencies (`go.mod`)

Three Hugo Blox modules: `blox-bootstrap/v5`, `blox-plugin-decap-cms`, `blox-plugin-netlify`.

## Deployment

- **Netlify** (primary): Auto-deploys on push to `main`. Config in `netlify.toml`. Build: `hugo --gc --minify -b $URL`.
- **GitHub Pages** (secondary): Workflow in `.github/workflows/publish.yaml`, triggered on push to `main`.
- **Redirects**: Defined in `netlify.toml` — `/jhub`, `/meet`, `/open-positions`, and several JupyterHub notebook links.

## Publications Workflow

1. Edit `publications.bib` at the repo root.
2. Push to `main` (or trigger manually).
3. GitHub Actions runs `academic import publications.bib content/publication/ --compact` (Python 3.12, `academic==0.10.0`).
4. A PR is auto-created on branch `hugoblox-import-publications` for review.

## Key Conventions

- News items go in `content/newslist.dat` (plain text, one item per line, rendered as Markdown).
- Sponsor logos go in `assets/media/sponsors/` and are auto-rendered by the logos block.
- The `{{% mention "author-slug" %}}` shortcode links to author profiles.
- Taxonomies: `tags`, `categories`, `publication_types`, `authors` — each with custom permalink patterns.
- Editor config: UTF-8, LF line endings, 2-space indent (`.editorconfig`).
