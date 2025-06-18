# Documentation Scripts

This directory contains scripts for processing and managing the documentation.

## Main Scripts

- `prepare_docs.py`: The main script used by the GitHub Action to prepare markdown files for ReadTheDocs. It:
  - Removes TOC markers from markdown files
  - Fixes internal links for ReadTheDocs compatibility
  - Copies processed files from `group-syllabus/` to `docs/`

## Helper Scripts

These scripts were used during development and are kept for reference:

- `copy_md_files.sh`: Simple script to copy markdown files from `group-syllabus/` to `docs/`
- `fix_double_html.py`: Fixes double .html.html extensions in markdown links
- `fix_internal_links.py`: Fixes internal links in markdown files
- `fix_markdown_links.py`: Converts markdown links to use proper format for ReadTheDocs
- `remove_toc_markers.py`: Removes TOC markers from markdown files

## Usage

In normal operation, you should only need to use `prepare_docs.py`:

```bash
python scripts/prepare_docs.py
```

This script is automatically run by the GitHub Action when changes are pushed to the repository.



### add-toc-markers.sh

This script adds TOC markers to markdown files that have a "## Table of Contents" heading.

#### Use

```bash
./scripts/add-toc-markers.sh <file.md> [file2.md ...]
```

Example:
```bash
# Add TOC markers to a specific file
./scripts/add-toc-markers.sh group-syllabus/formatting.md

# Add TOC markers to all markdown files in group-syllabus
./scripts/add-toc-markers.sh group-syllabus/*.md
```

The script will:
1. Look for files with a "## Table of Contents" heading
2. Add `<!-- toc -->` and `<!-- tocstop -->` markers around the TOC
3. Skip files that already have TOC markers

These markers are used by the GitHub Action workflow to automatically update the table of contents. 
