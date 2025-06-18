#!/usr/bin/env python3
"""
This script updates markdown links in all markdown files in the docs directory
to use .html extensions for ReadTheDocs compatibility.
"""

import os
import re
import glob

def fix_markdown_links(file_path):
    """Update markdown links to use .html extension."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace markdown links with .md extension to .html extension
    pattern_md = r'\[([^\]]+)\]\(([^)]+)\.md\)'
    replacement_md = r'[\1](\2.html)'
    new_content = re.sub(pattern_md, replacement_md, content)
    
    # Replace markdown links without extension to add .html extension
    # But don't modify URLs with http/https or anchor links
    pattern_no_ext = r'\[([^\]]+)\]\((?!http|#)([^)]+)(?!\.html|\.[a-zA-Z0-9]{2,4})\)'
    replacement_no_ext = r'[\1](\2.html)'
    new_content = re.sub(pattern_no_ext, replacement_no_ext, new_content)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    return content != new_content  # Return True if changes were made

def main():
    """Process all markdown files in the docs directory."""
    docs_dir = 'docs'
    md_files = glob.glob(os.path.join(docs_dir, '*.md'))
    
    files_changed = 0
    for file_path in md_files:
        if fix_markdown_links(file_path):
            print(f"Fixed links in {file_path}")
            files_changed += 1
    
    print(f"\nProcessed {len(md_files)} files, {files_changed} files were modified.")

if __name__ == '__main__':
    main() 