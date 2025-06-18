.PHONY: docs clean serve prepare

# Build the documentation
docs:
	sphinx-build -b html docs docs/_build/html

# Clean the build directory
clean:
	rm -rf docs/_build

# Serve the documentation locally
serve: docs
	cd docs/_build/html && python -m http.server 8000

# Process markdown files from group-syllabus to docs
prepare:
	python scripts/prepare_docs.py 