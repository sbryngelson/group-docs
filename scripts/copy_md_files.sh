#!/bin/bash

# Create the docs directory if it doesn't exist
mkdir -p docs

# Copy all markdown files from group-syllabus to docs
cp group-syllabus/*.md docs/

echo "All markdown files copied to docs directory." 