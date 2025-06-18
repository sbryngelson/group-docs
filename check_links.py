#!/usr/bin/env python3
"""
Script to check if the GitHub repository links to templates are valid.
"""

import requests
import re
import glob
import sys
import time

def extract_github_links(file_path):
    """Extract GitHub links from a file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Pattern to match GitHub links to templates
    pattern = r'https://github\.com/comp-physics/group-docs/tree/([^/]+)/templates/[^)"]+'
    
    return re.findall(pattern, content)

def check_link(url):
    """Check if a link is valid."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    """Main function to check links."""
    md_files = glob.glob('docs/*.md')
    
    all_links_valid = True
    checked_links = set()
    
    print(f"Checking links in {len(md_files)} files...")
    
    for file_path in md_files:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Find all GitHub links to templates
        links = re.findall(r'(https://github\.com/comp-physics/group-docs/tree/[^/]+/templates/[^)"\']+)', content)
        
        if links:
            print(f"\nFile: {file_path}")
            
            for link in links:
                if link in checked_links:
                    continue
                
                checked_links.add(link)
                
                # Add a small delay to avoid rate limiting
                time.sleep(0.5)
                
                is_valid = check_link(link)
                status = "✅ Valid" if is_valid else "❌ Invalid"
                
                print(f"  {status}: {link}")
                
                if not is_valid:
                    all_links_valid = False
    
    if all_links_valid:
        print("\nAll template links are valid! 🎉")
        return 0
    else:
        print("\nSome template links are invalid. Please check them. ❌")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 