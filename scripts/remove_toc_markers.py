#!/usr/bin/env python3
"""
This script removes HTML markers for markdown TOC extension from all markdown files.
These markers are typically used by GitHub actions to generate tables of contents.
Common formats include:
- <!-- toc -->
- <!-- TOC -->
- <!-- START doctoc -->
- <!-- END doctoc -->
- <!-- AUTO-GENERATED-CONTENT:START (TOC) -->
- <!-- AUTO-GENERATED-CONTENT:END -->
"""

import os
import re
import glob
import shutil

def remove_toc_markers(file_path):
    """Remove TOC markers from a markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
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
    new_content = content
    for pattern in patterns:
        new_content = re.sub(pattern, '', new_content, flags=re.DOTALL)
    
    # Write the modified content back to the file
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        return True
    
    return False  # No changes were made

def process_directory(directory):
    """Process all markdown files in the specified directory."""
    md_files = glob.glob(os.path.join(directory, '*.md'))
    
    files_changed = 0
    for file_path in md_files:
        if remove_toc_markers(file_path):
            print(f"Removed TOC markers from {file_path}")
            files_changed += 1
    
    return len(md_files), files_changed

def copy_fixed_files_to_docs():
    """Copy the fixed markdown files from group-syllabus to docs."""
    source_dir = 'group-syllabus'
    target_dir = 'docs'
    
    # Get all markdown files in the source directory
    md_files = glob.glob(os.path.join(source_dir, '*.md'))
    
    # Copy each file to the target directory
    for file_path in md_files:
        file_name = os.path.basename(file_path)
        target_path = os.path.join(target_dir, file_name)
        shutil.copy2(file_path, target_path)
        print(f"Copied {file_path} to {target_path}")
    
    return len(md_files)

def main():
    """Process markdown files in both docs and group-syllabus directories."""
    # First, process files in the group-syllabus directory
    syllabus_files, syllabus_changed = process_directory('group-syllabus')
    print(f"\nProcessed {syllabus_files} files in group-syllabus, {syllabus_changed} files were modified.")
    
    # Copy the fixed files to docs
    copied_files = copy_fixed_files_to_docs()
    print(f"Copied {copied_files} files from group-syllabus to docs.")
    
    # Then process files in the docs directory
    docs_files, docs_changed = process_directory('docs')
    print(f"Processed {docs_files} files in docs, {docs_changed} files were modified.")
    
    print(f"\nTotal: Processed {syllabus_files + docs_files} files, {syllabus_changed + docs_changed} files were modified.")

if __name__ == '__main__':
    main() 