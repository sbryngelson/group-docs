#!/usr/bin/env python3
"""
This script fixes internal links in all markdown files for ReadTheDocs compatibility.
"""

import os
import re
import glob

def fix_internal_links(file_path):
    """Fix internal links for ReadTheDocs compatibility."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace internal links with proper format
    # 1. Replace links to other markdown files without extension
    pattern1 = r'\[([^\]]+)\]\(([^)]+?)(\.md)?\)'
    replacement1 = lambda m: f'[{m.group(1)}]({m.group(2)})' if m.group(2).startswith(('http://', 'https://', '#', '/')) else f'[{m.group(1)}]({m.group(2)})'
    
    # Apply the replacements
    new_content = content
    new_content = re.sub(pattern1, replacement1, new_content)
    
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
        if fix_internal_links(file_path):
            print(f"Fixed links in {file_path}")
            files_changed += 1
    
    print(f"\nProcessed {len(md_files)} files, {files_changed} files were modified.")

if __name__ == '__main__':
    main() 