#!/bin/bash

# Function to fix a file by copying content from the original file
fix_file() {
  local target_file=$1
  local source_file=$2
  
  # Get front matter from target file
  local front_matter=$(sed -n '1,/---$/p' "$target_file")
  
  # Create a temporary file with front matter and source content
  echo "$front_matter" > "${target_file}.tmp"
  echo "" >> "${target_file}.tmp"
  cat "$source_file" >> "${target_file}.tmp"
  
  # Replace the target file
  mv "${target_file}.tmp" "$target_file"
  
  echo "Fixed $target_file with content from $source_file"
}

# Fix syllabus files
fix_file "_syllabus/giving-talks.md" "group-syllabus/giving-talks.md"
fix_file "_syllabus/going-to-conferences.md" "group-syllabus/going-to-conferences.md"
fix_file "_syllabus/publishing.md" "group-syllabus/publishing.md"
fix_file "_syllabus/when-where-working.md" "group-syllabus/when-where-working.md"

# Fix papers files
fix_file "_papers/figures.md" "group-syllabus/figures.md"
fix_file "_papers/formatting.md" "group-syllabus/formatting.md"
fix_file "_papers/improving-your-writing.md" "group-syllabus/improving-your-writing.md"
fix_file "_papers/responding-to-reviewers.md" "group-syllabus/responding-to-reviewers.md"

# Fix details files
fix_file "_details/hardware.md" "group-syllabus/hardware.md"
fix_file "_details/undergraduate-specifics.md" "group-syllabus/undergraduate-specifics.md"

echo "All files have been fixed." 