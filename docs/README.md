# Documentation

This directory contains the source files for the Computational Physics @ GT Group Documentation website.

## Local Development

To build and view the documentation locally:

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Build the documentation:
   ```
   make docs
   ```

3. Serve the documentation locally:
   ```
   make serve
   ```

4. Open your browser and navigate to `http://localhost:8000`

## Adding or Updating Content

1. Edit the markdown files in this directory.
2. Build and preview the changes locally using the steps above.
3. Commit and push your changes to the repository.

## Deployment on ReadTheDocs

The documentation is automatically built and deployed on ReadTheDocs whenever changes are pushed to the main branch of the repository.

To set up the ReadTheDocs deployment:

1. Create an account on [ReadTheDocs](https://readthedocs.org/).
2. Import your GitHub repository.
3. Configure the settings as needed.
4. ReadTheDocs will automatically build and deploy your documentation.

## Structure

- `conf.py`: Sphinx configuration file
- `index.md`: Main landing page
- Other `.md` files: Content pages
- `_static/`: Static files (CSS, images, etc.)
- `_templates/`: Custom templates 