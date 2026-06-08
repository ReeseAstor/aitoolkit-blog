#!/usr/bin/env python3
"""
AI ToolKit — Article List Updater
Updates the ARTICLES array in assets/main.js when a new article is published.
Called by the Hermes content pipeline after writing a new article.

Usage: py update_article_list.py --slug "article-slug" --title "Article Title" --excerpt "..." --category "Comparison" --date "2026-06-08" --read-time "8 min read"
"""
import argparse
import json
import os
import re

MAIN_JS_PATH = os.path.expanduser("~/projects/aitoolkit-blog/assets/main.js")

def update_articles(slug, title, excerpt, category, date, read_time):
    with open(MAIN_JS_PATH, "r") as f:
        content = f.read()
    
    # Find the ARTICLES array
    match = re.search(r'const ARTICLES = \[(.*?)\];', content, re.DOTALL)
    if not match:
        print("ERROR: Could not find ARTICLES array in main.js")
        return False
    
    # Check if slug already exists
    if f'"slug": "{slug}"' in match.group(1):
        print(f"Article with slug '{slug}' already exists in ARTICLES. Skipping.")
        return True
    
    new_entry = f'''    {{
        slug: "{slug}",
        title: "{title}",
        excerpt: "{excerpt}",
        category: "{category}",
        date: "{date}",
        readTime: "{read_time}"
    }}'''
    
    # Insert at the beginning of the array (newest first)
    old_array = match.group(1).strip()
    if old_array:
        new_array = new_entry + ",\n    " + old_array
    else:
        new_array = new_entry
    
    new_content = content.replace(match.group(1), "\n    " + new_array + "\n")
    
    with open(MAIN_JS_PATH, "w") as f:
        f.write(new_content)
    
    print(f"Added article '{title}' to ARTICLES array in main.js")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--excerpt", required=True)
    parser.add_argument("--category", default="Guide")
    parser.add_argument("--date", required=True)
    parser.add_argument("--read-time", default="8 min read")
    args = parser.parse_args()
    
    update_articles(
        args.slug, args.title, args.excerpt,
        args.category, args.date, args.read_time
    )
