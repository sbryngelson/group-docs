# ReadTheDocs Integration Setup

This document explains how to set up the integration between this repository and ReadTheDocs to automatically build and deploy documentation.

## How It Works

The integration works as follows:

1. You edit markdown files in the `group-syllabus` directory.
2. When you push changes to the main branch, a GitHub Action is triggered.
3. The GitHub Action:
   - Processes the markdown files (removes TOC markers, fixes links)
   - Copies the processed files to the `docs` directory
   - Builds the documentation locally to verify it works
   - Force-commits the changes to the `docs` directory (overriding .gitignore)
   - Pushes the changes to the repository
4. ReadTheDocs detects the changes and automatically builds and deploys the documentation.

### Source Control Strategy

We use a specific strategy for source control:

1. The original markdown files in `group-syllabus/` are the source of truth and are tracked in git.
2. The processed files in `docs/` are generated and normally excluded from git via .gitignore.
3. The GitHub Action force-adds these files to git when changes are made.
4. This approach keeps your repository clean while ensuring ReadTheDocs has the files it needs.

## Setup Instructions

### 1. Connect GitHub Repository to ReadTheDocs

1. Create an account on [ReadTheDocs](https://readthedocs.org/) if you don't have one.
2. Log in to ReadTheDocs and click on "Import a Project".
3. Connect your GitHub account if you haven't already.
4. Select this repository from the list of available repositories.
5. Click "Next" to proceed with the import.

### 2. Configure ReadTheDocs Project Settings

1. In the project's admin panel on ReadTheDocs, go to "Admin" > "Advanced Settings".
2. Set the following settings:
   - **Default branch**: `main` (or `master`, depending on your repository)
   - **Python configuration file**: `.readthedocs.yaml`
   - **Python interpreter**: CPython 3.x
   - **Use system packages**: No
3. Save the changes.

### 3. Enable GitHub Action

The GitHub Action is already set up in this repository. It's defined in `.github/workflows/readthedocs.yml`.

To ensure it works properly:

1. Go to your repository on GitHub.
2. Click on "Settings" > "Actions" > "General".
3. Make sure "Allow all actions and reusable workflows" is selected.
4. Under "Workflow permissions", select "Read and write permissions".
5. Save the changes.

### 4. Verify the Integration

1. Make a small change to a markdown file in the `group-syllabus` directory.
2. Commit and push the change to the main branch.
3. Go to the "Actions" tab in your GitHub repository to see the workflow running.
4. Once the workflow completes, check your ReadTheDocs project to see if the documentation is being built.
5. After the build completes, visit your ReadTheDocs URL to see the deployed documentation.

## Troubleshooting

If you encounter issues with the integration:

1. **GitHub Action fails**: Check the workflow logs in the "Actions" tab for error messages.
2. **ReadTheDocs build fails**: Check the build logs on ReadTheDocs for error messages.
3. **Links don't work in the deployed documentation**: Make sure the `prepare_docs.py` script is correctly processing the links.

## Manual Build

If you need to manually build the documentation:

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the preparation script:
   ```bash
   python scripts/prepare_docs.py
   ```
4. Build the documentation:
   ```bash
   sphinx-build -b html docs docs/_build/html
   ```
5. Open `docs/_build/html/index.html` in your browser to view the documentation. 