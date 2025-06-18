#!/usr/bin/env python3
"""
Script to check all links in the documentation.
This checks both internal links and external links.
"""

import os
import re
import glob
import sys
import time
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Base URL for local server
BASE_URL = "http://localhost:8000/"

def get_all_html_files():
    """Get all HTML files in the built documentation."""
    return glob.glob('docs/_build/html/**/*.html', recursive=True)

def extract_links_from_html(file_path):
    """Extract all links from an HTML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Skip anchor links within the same page
        if href.startswith('#'):
            continue
        # Convert relative URLs to absolute
        if not href.startswith(('http://', 'https://')):
            href = urljoin(BASE_URL, href)
        links.append((href, a_tag.get_text().strip() or "No text"))
    
    return links

def check_link(url):
    """Check if a link is valid."""
    try:
        if url.startswith(BASE_URL):
            # For local links, just check if the file exists
            local_path = url.replace(BASE_URL, 'docs/_build/html/')
            # Handle URLs ending with / by appending index.html
            if local_path.endswith('/'):
                local_path += 'index.html'
            # Remove any query parameters or fragments
            local_path = local_path.split('#')[0].split('?')[0]
            return os.path.exists(local_path)
        else:
            # For external links, make an HTTP request
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.status_code == 200
    except (requests.RequestException, Exception) as e:
        print(f"  Error checking {url}: {e}")
        return False

def main():
    """Main function to check all links."""
    # First, build the documentation
    print("Building the documentation...")
    os.system("source venv/bin/activate && make docs")
    
    # Get all HTML files
    html_files = get_all_html_files()
    
    if not html_files:
        print("No HTML files found. Make sure the documentation was built correctly.")
        return 1
    
    print(f"Checking links in {len(html_files)} HTML files...")
    
    all_links_valid = True
    checked_links = {}  # URL -> (is_valid, [source_files])
    
    for file_path in html_files:
        relative_path = os.path.relpath(file_path, 'docs/_build/html')
        print(f"\nChecking links in: {relative_path}")
        
        links = extract_links_from_html(file_path)
        
        for url, text in links:
            if url in checked_links:
                # Already checked this link
                is_valid = checked_links[url][0]
                checked_links[url][1].append((relative_path, text))
            else:
                # Add a small delay to avoid rate limiting for external links
                if not url.startswith(BASE_URL):
                    time.sleep(0.5)
                
                is_valid = check_link(url)
                checked_links[url] = [is_valid, [(relative_path, text)]]
            
            status = "✅" if is_valid else "❌"
            print(f"  {status} {url} ('{text}')")
            
            if not is_valid:
                all_links_valid = False
    
    # Print summary
    print("\n=== SUMMARY ===")
    total_links = len(checked_links)
    valid_links = sum(1 for is_valid, _ in checked_links.values() if is_valid)
    
    print(f"Total links checked: {total_links}")
    print(f"Valid links: {valid_links}")
    print(f"Invalid links: {total_links - valid_links}")
    
    if not all_links_valid:
        print("\n=== INVALID LINKS ===")
        for url, (is_valid, sources) in checked_links.items():
            if not is_valid:
                print(f"\n❌ {url}")
                print("  Found in:")
                for source_file, text in sources:
                    print(f"    - {source_file} ('{text}')")
    
    if all_links_valid:
        print("\nAll links are valid! 🎉")
        return 0
    else:
        print("\nSome links are invalid. Please check them. ❌")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 