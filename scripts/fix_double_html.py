#!/usr/bin/env python3
"""
This script fixes double .html.html extensions in markdown links in all markdown files in the docs directory.
"""

import os
import re
import glob

def fix_double_html_links(file_path):
    """Fix double .html.html extensions in markdown links."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace double .html.html extensions with single .html
    pattern = r'\[([^\]]+)\]\(([^)]+)\.html\.html\)'
    replacement = r'[\1](\2)'
    
    # Apply the replacement
    new_content = re.sub(pattern, replacement, content)
    
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
        if fix_double_html_links(file_path):
            print(f"Fixed links in {file_path}")
            files_changed += 1
    
    print(f"\nProcessed {len(md_files)} files, {files_changed} files were modified.")

if __name__ == '__main__':
    main() 