# Search Functionality for Group Syllabus

This document explains how to use and maintain the search functionality for the Georgia Tech Computational Physics Group Syllabus.

## How It Works

The search functionality is implemented using GitHub Pages with the Just the Docs Jekyll theme, which includes built-in search capabilities. This allows students and researchers to quickly find information across all documentation pages.

## Features

- Full-text search across all documentation pages
- Search by headings, content, and keywords
- Highlighting of search terms in results
- Search results ranked by relevance

## Setting Up GitHub Pages

1. **Enable GitHub Pages in your repository settings**:
   - Go to Settings > Pages
   - Set the source to "GitHub Actions"

2. **Verify the workflow is running**:
   - Check the Actions tab to ensure the "Deploy Jekyll site to Pages" workflow is running
   - The first build may take a few minutes

## Adding New Content

When adding new content to be searchable:

1. Create markdown files in the appropriate collection directory:
   - `_syllabus/` - For general syllabus content
   - `_papers/` - For writing and publication guidance
   - `_details/` - For specific details and resources

2. Add front matter to each markdown file:
   ```yaml
   ---
   layout: page
   title: Your Page Title
   nav_order: 1
   description: "Brief description of the page content"
   permalink: /collection-name/page-name
   ---
   ```

3. Push changes to the repository, and GitHub Actions will automatically rebuild the site with updated search index

## Search Tips for Users

Share these tips with your students:

- Use the search bar in the top navigation to find content
- Use quotes for exact phrase matching: `"research meeting"`
- Use multiple terms to narrow results: `funding conference`
- Results are ranked by relevance

## Maintenance

- The search index is automatically updated when changes are pushed to the repository
- No manual maintenance is required
- To modify search behavior, edit the `search` section in `_config.yml`

## Troubleshooting

If search isn't working properly:

1. Check that the GitHub Pages site is properly deployed
2. Verify that front matter is correctly formatted in all markdown files
3. Ensure the `search_enabled: true` setting is in `_config.yml`
4. Check the GitHub Actions logs for any build errors 