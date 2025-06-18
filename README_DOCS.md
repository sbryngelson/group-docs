# Computational Physics @ GT Group Documentation

This repository contains the documentation for the Computational Physics @ GT research group, configured to be deployed on [ReadTheDocs](https://readthedocs.org/).

## 📚 Documentation Structure

The documentation is organized as follows:

- `group-syllabus/`: Contains the original markdown content files
- `docs/`: Contains the processed documentation files for ReadTheDocs
  - `conf.py`: Sphinx configuration file
  - `index.md`: Main landing page
  - `_static/`: Static files (CSS, images, etc.)
  - `_templates/`: Custom templates
- `requirements.txt`: Python dependencies for building the documentation
- `.readthedocs.yaml`: Configuration file for ReadTheDocs
- `Makefile`: Commands for building and serving the documentation locally
- `scripts/prepare_docs.py`: Main script for processing documentation files

## 🚀 Getting Started

### Local Development

To build and view the documentation locally:

1. Create a virtual environment and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Process the markdown files:
   ```bash
   python scripts/prepare_docs.py
   ```
   or
   ```bash
   make prepare
   ```

3. Build the documentation:
   ```bash
   make docs
   ```

4. Serve the documentation locally:
   ```bash
   make serve
   ```

5. Open your browser and navigate to `http://localhost:8000`

### Updating Content

1. Edit the markdown files in the `group-syllabus` directory.
2. Process the files to update the docs directory:
   ```bash
   python scripts/prepare_docs.py
   ```
   or
   ```bash
   make prepare
   ```
3. Build and preview the changes locally using the steps above.
4. Commit and push your changes to the repository.

## 🔄 Automated Workflow

The documentation workflow is as follows:

1. Edit the original markdown files in the `group-syllabus/` directory
2. Run `python scripts/prepare_docs.py` to process the files and copy them to the `docs/` directory
3. The script performs the following operations:
   - Removes TOC markers from markdown files
   - Fixes internal links for ReadTheDocs compatibility
   - Converts template links to GitHub repository links with the correct branch (master)
   - Fixes links in the index.md file to use proper extensions
   - Synchronizes readme.md to docs/index.md
   - Adds toctree directives for ReadTheDocs navigation
4. Run `make docs` to build the documentation
5. Run `make serve` to preview the documentation locally

## 🚀 GitHub Actions Integration

A GitHub Action is configured to automatically run the prepare_docs.py script when changes are made to the markdown files. This ensures that the documentation is always up-to-date with the latest content.

The GitHub Action performs the following steps:
1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Runs the prepare_docs.py script
5. Commits and pushes the changes to the repository

## 📝 Documentation Files

The documentation includes the following files:

- `README_DOCS.md`: This file, explaining the documentation system
- `READTHEDOCS_SETUP.md`: Instructions for setting up ReadTheDocs
- `Makefile`: Commands for building and serving the documentation locally
- `scripts/prepare_docs.py`: Script for processing markdown files for ReadTheDocs compatibility

## 🔧 Commands

The following commands are available in the Makefile:

- `make docs`: Build the documentation
- `make serve`: Serve the documentation locally
- `make clean`: Clean the build directory

## 📋 Notes on Link Handling

The `prepare_docs.py` script handles various types of links to ensure they work correctly in ReadTheDocs:

1. Internal links between markdown files are fixed to work in the ReadTheDocs HTML structure
2. Links to template files are converted to GitHub repository links pointing to the master branch
3. Links in the index.md file are properly formatted with correct extensions
4. The `.md` extension is removed from links as ReadTheDocs uses `.html` extensions
5. Special handling for the CONTRIBUTING.md link to point to the GitHub repository

## 🔍 Known Issues with External Links

Some external links may not work in the documentation due to the following reasons:

1. Georgia Tech-specific resources (Box folders, Outlook calendar) require authentication
2. Some external websites may be temporarily unavailable or have changed URLs
3. Email addresses with URL encoding may not work correctly

These external links need to be updated in the original markdown files if needed.

## 🌐 Deployment on ReadTheDocs

For detailed instructions on setting up ReadTheDocs, see [READTHEDOCS_SETUP.md](READTHEDOCS_SETUP.md).

## 🛠️ Customization

### Theme

The documentation uses the [Sphinx ReadTheDocs theme](https://sphinx-rtd-theme.readthedocs.io/). You can customize the theme by editing the `html_theme` and related settings in `docs/conf.py`.

### CSS

Custom CSS styles are defined in `docs/_static/custom.css`. You can modify this file to change the appearance of the documentation.

### Extensions

The documentation uses several Sphinx extensions:

- `myst_parser`: For parsing Markdown files
- `sphinx_markdown_tables`: For rendering tables in Markdown
- `sphinx.ext.autodoc`: For API documentation
- `sphinx.ext.viewcode`: For linking to source code
- `sphinx.ext.napoleon`: For Google-style docstrings

You can add or remove extensions in the `extensions` list in `docs/conf.py`.

## 📝 License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) - Creative Commons Attribution-NonCommercial 4.0 International 