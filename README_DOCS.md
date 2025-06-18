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

This repository uses GitHub Actions to automate the documentation process:

1. When you push changes to the `group-syllabus` directory, a GitHub Action is triggered.
2. The action runs `scripts/prepare_docs.py` to process the markdown files.
3. The processed files are force-added to the repository (overriding .gitignore).
4. ReadTheDocs automatically builds and deploys the updated documentation.

### Source Control Strategy

We use a specific source control strategy:

1. The original markdown files in `group-syllabus/` are the source of truth and tracked in git.
2. The processed files in `docs/` are generated and normally excluded via .gitignore.
3. The GitHub Action force-adds these files when changes are made.
4. This approach keeps the repository clean while ensuring ReadTheDocs has the files it needs.

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