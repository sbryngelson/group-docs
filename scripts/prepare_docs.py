#!/usr/bin/env python3
"""
This script prepares markdown files for ReadTheDocs compatibility by:
1. Removing TOC markers
2. Fixing internal links
3. Copying processed files from group-syllabus to docs
"""

import os
import re
import glob
import shutil
import sys

def remove_toc_markers(content):
    """Remove TOC markers from markdown content."""
    # Define patterns for different types of TOC markers
    patterns = [
        r'<!-- START doctoc generated TOC please keep comment here to allow auto update -->.*?<!-- END doctoc -->\n?',
        r'<!-- toc -->.*?<!-- tocstop -->\n?',
        r'<!-- TOC -->.*?<!-- /TOC -->\n?',
        r'<!-- START doctoc -->.*?<!-- END doctoc -->\n?',
        r'<!-- AUTO-GENERATED-CONTENT:START \(TOC\) -->.*?<!-- AUTO-GENERATED-CONTENT:END -->\n?',
        r'<!--\s*Table of Contents.*?-->\n?',
        r'<!-- TOC START -->.*?<!-- TOC END -->\n?',
        r'<!-- TOC_START -->.*?<!-- TOC_END -->\n?',
        r'<!-- toc:start -->.*?<!-- toc:end -->\n?',
        r'<!-- TOC:start -->.*?<!-- TOC:end -->\n?',
        r'## Table of Contents\n\n.*?\n\n',  # Also remove the TOC content itself
    ]
    
    # Apply each pattern
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    return content

def fix_internal_links(content):
    """Fix internal links for ReadTheDocs compatibility."""
    # Replace internal links with proper format
    # 1. Replace links to other markdown files without extension
    pattern1 = r'\[([^\]]+)\]\(([^)]+?)(\.md)?\)'
    replacement1 = lambda m: f'[{m.group(1)}]({m.group(2)})' if m.group(2).startswith(('http://', 'https://', '#', '/')) else f'[{m.group(1)}]({m.group(2)})'
    
    # Apply the replacements
    content = re.sub(pattern1, replacement1, content)
    
    return content

def process_file(file_path, output_dir=None):
    """Process a single markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Apply transformations
    content = remove_toc_markers(content)
    content = fix_internal_links(content)
    
    # Determine output path
    if output_dir:
        file_name = os.path.basename(file_path)
        output_path = os.path.join(output_dir, file_name)
    else:
        output_path = file_path
    
    # Write the processed content
    with open(output_path, 'w') as f:
        f.write(content)
    
    return output_path

def process_directory(source_dir, output_dir=None):
    """Process all markdown files in a directory."""
    md_files = glob.glob(os.path.join(source_dir, '*.md'))
    processed_files = []
    
    for file_path in md_files:
        output_path = process_file(file_path, output_dir)
        processed_files.append(output_path)
        print(f"Processed {file_path} -> {output_path}")
    
    return processed_files

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        # Create .gitkeep file to ensure directory is tracked in git
        with open(os.path.join(directory, '.gitkeep'), 'w') as f:
            pass
        print(f"Created directory: {directory}")

def main():
    """Main function to prepare documentation."""
    # Ensure docs directory exists
    ensure_directory_exists('docs')
    ensure_directory_exists('docs/_static')
    ensure_directory_exists('docs/_templates')
    
    # Process group-syllabus files and copy to docs
    print("Processing files in group-syllabus directory...")
    processed_files = process_directory('group-syllabus', 'docs')
    print(f"Processed {len(processed_files)} files from group-syllabus to docs.")
    
    # Process any additional files in docs directory
    print("\nProcessing additional files in docs directory...")
    docs_files = process_directory('docs')
    print(f"Processed {len(docs_files)} files in docs directory.")
    
    print("\nDocumentation preparation complete!")
    return 0

if __name__ == '__main__':
    sys.exit(main()) 