#!/bin/bash

# Function to replace include_relative with file content
replace_include() {
  local file=$1
  local include_path=$(grep -o "include_relative.*\.md" "$file" | sed 's/include_relative //' | tr -d '%{}')
  
  # Get the front matter from the file
  local front_matter=$(sed -n '1,/---$/p' "$file")
  
  # Get the content from the included file
  local content=$(cat "$include_path")
  
  # Create a temporary file with the new content
  echo "$front_matter" > "${file}.tmp"
  echo "" >> "${file}.tmp"
  echo "$content" >> "${file}.tmp"
  
  # Replace the original file
  mv "${file}.tmp" "$file"
  
  echo "Fixed $file by including content from $include_path"
}

# Process all files with include_relative statements
for file in $(grep -l "include_relative" _syllabus/*.md _papers/*.md _details/*.md); do
  replace_include "$file"
done

echo "All include_relative statements have been replaced with actual content." 