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
    
    # Fix links to templates directory
    # Convert ../templates/ or templates/ paths to GitHub repo links
    repo_url = "https://github.com/comp-physics/group-docs/tree/master"
    
    # Replace links to templates directory
    content = re.sub(r'\[([^\]]+)\]\(\.\./templates/([^)]+)\)', 
                     fr'[\1]({repo_url}/templates/\2)', 
                     content)
    content = re.sub(r'\[([^\]]+)\]\(templates/([^)]+)\)', 
                     fr'[\1]({repo_url}/templates/\2)', 
                     content)
    
    # Also fix references to templates in text without markdown links
    content = re.sub(r'`(\.\.\/)?templates/([^`]+)`', 
                     fr'[`templates/\2`]({repo_url}/templates/\2)', 
                     content)
    
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

def sync_readme_to_index():
    """Synchronize readme.md content to docs/index.md with proper formatting."""
    print("Synchronizing readme.md to docs/index.md...")
    
    # Check if readme.md exists
    if not os.path.exists('readme.md'):
        print("Warning: readme.md not found, skipping synchronization.")
        return False
    
    # Read the content from readme.md
    with open('readme.md', 'r') as f:
        content = f.read()
    
    # Process the content for ReadTheDocs compatibility
    content = remove_toc_markers(content)
    
    # Fix specific links in the readme for ReadTheDocs
    # Don't add .html extension to links in the Quick Navigation section
    content = content.replace('group-syllabus/intro-to-group.md', 'intro-to-group')
    content = content.replace('group-syllabus/faq.md', 'faq')
    content = content.replace('CONTRIBUTING.md', 'https://github.com/comp-physics/group-docs/blob/master/CONTRIBUTING.md')
    # Fix the specific CONTRIBUTING link in the See section
    content = re.sub(r'\[https://github\.com/comp-physics/group-docs/blob/master/CONTRIBUTING\]', 
                    r'[https://github.com/comp-physics/group-docs/blob/master/CONTRIBUTING.md]', 
                    content)
    # Fix another instance of the CONTRIBUTING link
    content = content.replace('(https://github.com/comp-physics/group-docs/blob/master/CONTRIBUTING)', 
                            '(https://github.com/comp-physics/group-docs/blob/master/CONTRIBUTING.md)')
    
    content = content.replace('](group-syllabus/', '](')
    
    # Add .html extension to internal links in the tables (syllabus, papers, details sections)
    # This pattern matches markdown links in table rows
    pattern = r'\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|'
    
    def add_html_extension_in_tables(match):
        link_text = match.group(1)
        link_url = match.group(2)
        
        # Skip links that already have extensions or are external
        if (link_url.endswith('.html') or 
            link_url.startswith('http://') or 
            link_url.startswith('https://') or 
            link_url.startswith('#') or 
            link_url.startswith('/')):
            return f'| [{link_text}]({link_url}) |'
        
        # Remove .md extension if present and add .html extension
        if link_url.endswith('.md'):
            link_url = link_url[:-3]
        
        # Add .html extension
        return f'| [{link_text}]({link_url}.html) |'
    
    content = re.sub(pattern, add_html_extension_in_tables, content)
    
    # Fix links to templates directory in the readme
    repo_url = "https://github.com/comp-physics/group-docs/tree/master"
    
    # Fix template links in the "Templates" section
    pattern_templates = r'\[([^\]]+)\]\(templates/([^)]+)\)'
    content = re.sub(pattern_templates, 
                     fr'[\1]({repo_url}/templates/\2)', 
                     content)
    
    # Fix specific template links in the Quick Navigation section
    content = content.replace('.md.html)', '.html)')
    content = content.replace(f'{repo_url}/templates/paper.html', f'{repo_url}/templates/paper')
    content = content.replace(f'{repo_url}/templates/paper_rebuttal.html', f'{repo_url}/templates/paper_rebuttal')
    content = content.replace(f'{repo_url}/templates/paper/figures.html', f'{repo_url}/templates/paper/figures')
    content = content.replace(f'{repo_url}/templates/talks.html', f'{repo_url}/templates/talks')
    
    # Apply general link fixes
    content = fix_internal_links(content)
    
    # Add toctree directives if they don't exist
    if "```{toctree}" not in content:
        toctree_content = """

```{toctree}
:maxdepth: 2
:hidden:
:caption: Getting Started

intro-to-group
faq
why-phd
funding
working-with-me
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Research Process

doing-research
publishing
when-where-working
going-to-conferences
giving-talks
challenges
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Writing & Publishing

improving-your-writing
formatting
figures
responding-to-reviewers
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Resources

undergraduate-specifics
computers
hardware
```"""
        content += toctree_content
    
    # Write the processed content to docs/index.md
    with open('docs/index.md', 'w') as f:
        f.write(content)
    
    print("Successfully synchronized readme.md to docs/index.md")
    return True

def main():
    """Main function to prepare documentation."""
    # Ensure docs directory exists
    ensure_directory_exists('docs')
    ensure_directory_exists('docs/_static')
    ensure_directory_exists('docs/_templates')
    
    # Synchronize readme.md to docs/index.md
    sync_readme_to_index()
    
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