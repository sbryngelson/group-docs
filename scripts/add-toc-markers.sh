#!/bin/bash

# This script adds TOC markers to markdown files that have a "## Table of Contents" heading

# Check if a file path is provided
if [ "$#" -eq 0 ]; then
  echo "Usage: $0 <file.md> [file2.md ...]"
  echo "Example: $0 group-syllabus/*.md"
  exit 1
fi

# Process each file provided as an argument
for file in "$@"; do
  # Check if file exists
  if [ -f "$file" ]; then
    echo "Processing $file..."
    
    # Check if the file already has TOC markers
    if grep -q "<!-- toc -->" "$file"; then
      echo "  TOC markers already exist in $file, skipping..."
      continue
    fi
    
    # Find the line with "## Table of Contents"
    toc_line=$(grep -n "^## Table of Contents" "$file" | cut -d: -f1)
    
    if [ -n "$toc_line" ]; then
      # Create a temporary file
      temp_file=$(mktemp)
      
      # Extract content before TOC line
      head -n "$toc_line" "$file" > "$temp_file"
      
      # Add TOC markers
      echo "<!-- toc -->" >> "$temp_file"
      echo "<!-- tocstop -->" >> "$temp_file"
      
      # Extract content after TOC line
      tail -n +$((toc_line + 1)) "$file" >> "$temp_file"
      
      # Replace original file
      mv "$temp_file" "$file"
      
      echo "  Added TOC markers to $file"
    else
      echo "  No '## Table of Contents' found in $file"
    fi
  else
    echo "File $file does not exist"
  fi
done

echo "Done adding TOC markers" 