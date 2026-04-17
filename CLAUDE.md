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

- **`publication/`** — 129+ entries. Named `YearTypeAuthor/` (e.g. `2024JTherapontos/`). Auto-generated from `publications.bib` via GitHub Actions workflow (`import-publications.yml`) using `academic import`. Do not hand-edit generated files; update the `.bib` instead.
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
- **Pre-push verification**: Before every `git push`, run `hugo --gc --minify` locally and confirm the build succeeds with no errors. Do not push if the build fails.

---

## Workflow Guides

### How to Add a New Publication

Publications are auto-generated from BibTeX. **Do not create publication folders by hand.**

1. **Add the BibTeX entry** to `publications.bib` at the repo root.
2. **Push to `main`** (or trigger the workflow manually).
3. GitHub Actions (`import-publications.yml`) runs `academic import publications.bib content/publication/ --compact` and opens a PR on branch `hugoblox-import-publications`.
4. **Review and merge** the PR. Each publication gets a folder named `YearTypeAuthor/` containing `index.md` and `cite.bib`.

**After the import**, you can optionally enhance the generated folder:
- Add a PDF named `YearTypeAuthor.pdf` (e.g. `2025CHashemnezhad.pdf`).
- Link to projects by adding `projects: ['project-slug']` in the frontmatter.
- Add a `featured.png` image.

**Publication type codes and frontmatter mapping:**

| Folder code | `publication_types` value | Meaning |
|---|---|---|
| `C` | `"paper-conference"` | Conference paper |
| `J` | `"article-journal"` | Journal article |
| `Th` | `"thesis"` | Thesis |
| `TR` | `"report"` | Technical report |
| `BC` | `"chapter"` | Book chapter |

When multiple publications share the same year, type, and author, append `b`, `c`, `d`, etc. (e.g. `2025JTherapontos/`, `2025JTherapontosb/`).

**Frontmatter reference** (TOML `+++` delimiters, auto-generated):
```toml
title = "Full title"
date = "2025-01-01"
authors = ["First Author", "Second Author"]
publication_types = ["article-journal"]   # see mapping below
publication = "Journal or Conference Name"
publication_short = ""
abstract = "Abstract text"
featured = false
tags = ["keyword1", "keyword2"]
doi = "10.xxxx/xxxxx"
projects = ["project-slug"]
url_pdf = ""
url_code = ""
url_dataset = ""
url_video = ""
math = true
highlight = true
```

### How to Add a News Item

1. **Edit `content/newslist.dat`** — prepend a new line at the top of the file.
2. **Format**: `**[DD/MM/YY]** Description with [links](/path/).`
3. The homepage displays the first N items (configured in `content/_index.md` via `{{< readfromfile "/content/newslist.dat" 5 >}}`).

**Examples:**
```
**[27/01/26]** New journal paper on [Paper title](/publication/2026jauthorname/) published in [Journal](/tag/journaltag/).
**[15/09/25]** Two conference papers presented at ISGT 2025 by {{% mention "a.-author" %}}. [Check them out](/tag/isgt25/).
```

### How to Add a New Blog Post

1. **Create a folder** `content/post/YYYY_Short_Name/` (e.g. `2026_New_Topic/`).
2. **Create `index.md`** with this frontmatter:

```yaml
---
title: "Post Title"
subtitle: ""
summary: "One-line summary for cards"
authors: ["first-initial.-lastname"]
tags: ['tag1', 'tag2']
categories: ['blog']
date: 2026-04-17T00:00:00+03:00
lastmod: 2026-04-17T00:00:00+03:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: true

projects: []
---

Markdown body here.
```

3. **Add images** to the same folder:
   - `featured.jpg` or `featured.png` — used as the card thumbnail.
   - Other images referenced in the body with `![alt](filename.jpg)`.
4. **Author slug** must match a folder name under `content/authors/` (e.g. `p.-aristidou`).

### How to Add a New Research Project

1. **Create a folder** `content/project/project-slug/` (use lowercase, hyphens; e.g. `content/project/my-new-project/`).
2. **Create `index.md`** with this frontmatter:

```yaml
---
title: "Project Full Name"
summary: "One-line description"
tags:
- Current projects
- Relevant Topic Tag
date: "2026-04-01T00:00:00Z"
profile: false

external_link:

image:
  caption: ""
  focal_point: Smart
---

Markdown body with project description.
```

3. **Add a `featured.png`** (or `.jpg`) — used as the project card image.
4. **Set the right filter tag** to control where the project appears on the homepage portfolio:
   - `themes` — Research themes / general areas
   - `Current projects` — Active funded projects
   - `Software tools` — Open-source tools
   - `Past projects` — Completed projects
5. **Link publications** to this project by adding `projects: ["project-slug"]` in their frontmatter.

### How to Add a New Team Member

1. **Create a folder** `content/authors/first-initial.-lastname/` (e.g. `content/authors/j.-smith/`).
2. **Create `_index.md`** (note the underscore) with this frontmatter:

```yaml
---
title: "Full Display Name"
authors:
- "F. Lastname"
superuser: false
role: "PhD Candidate"
organizations:
- name: Cyprus University of Technology
  url: "https://cut.ac.cy"
bio: ""
interests:
- Research Interest 1
- Research Interest 2
education:
  courses:
  - course: MSc in Electrical Engineering
    institution: University Name
    year: 2024
social:
- icon: envelope
  icon_pack: fas
  link: 'mailto:email@cut.ac.cy'
- icon: linkedin
  icon_pack: fab
  link: 'https://www.linkedin.com/in/username/'
- icon: google-scholar
  icon_pack: ai
  link: 'https://scholar.google.com/citations?user=XXXXX'
- icon: github
  icon_pack: fab
  link: 'https://github.com/username'
- icon: orcid
  icon_pack: ai
  link: 'https://orcid.org/0000-0000-0000-0000'
email: "email@cut.ac.cy"
user_groups:
- PhD Candidates
---

Optional bio paragraph in Markdown.
```

3. **Add `avatar.jpg`** (or `.png`) — profile photo in the same folder.
4. **User groups** control the team page grouping: `Principal Investigator`, `PostDocs`, `PhD Candidates`, `Research Associates`, `Alumni`.
5. **To move a member to alumni**, change `user_groups` to `["Alumni"]`.

### How to Add Course Materials

Courses live under `content/courses/`. Each course is a Hugo "book" type.

1. **Course overview**: Edit or create `content/courses/course-code/_index.md`:
```yaml
---
title: "EEN4XX - Course Name"
linkTitle: "EEN4XX"
summary: "One-line description"
date: '2026-09-01'
type: book
---
```

2. **Add sub-pages** (slides, exercises, screencasts, project) as separate `.md` files in the same folder:
```yaml
---
title: "Exercises"
date: '2026-09-01'
type: book
weight: 20
---
```
   - `weight` controls page ordering in the sidebar.

3. **Student projects** go in `content/courses/student-projects/` with `type: book` and a `weight` for ordering.

### How to Add a Sponsor Logo

1. **Place the logo** (PNG or SVG preferred) in `assets/media/sponsors/`.
2. The logos block on the homepage (`layouts/partials/blocks/logos.html`) auto-renders all images in that directory. No config changes needed.

### How to Add a Redirect

1. **Edit `netlify.toml`** at the repo root.
2. Add a `[[redirects]]` block:
```toml
[[redirects]]
  from = "/short-path"
  to = "https://destination-url.com"
  status = 302
```

### Cross-Referencing Content

- **Link a publication to a project**: Add `projects = ["project-slug"]` in the publication's frontmatter.
- **Mention a team member**: Use `{{% mention "first-initial.-lastname" %}}` in any Markdown file.
- **Link to internal content**: Use relative paths like `[text](/publication/2026jauthor/)` or Hugo refs like `{{< ref "/courses/een320/_index.md" >}}`.
- **Tag-based collections**: Add shared tags (e.g. `isgt25`) to group related publications, then link to `/tag/isgt25/`.
