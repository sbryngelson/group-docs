# Documentation Scripts

This directory contains utility scripts for maintaining the group documentation.

## Available Scripts

### add-toc-markers.sh

This script adds TOC markers to markdown files that have a "## Table of Contents" heading.

#### Usage

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