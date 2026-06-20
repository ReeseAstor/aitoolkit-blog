#!/usr/bin/env python3
"""
AI ToolKit — SEO Injector
Adds GA4 tracking, structured data (JSON-LD), canonical URLs, and favicon to all HTML files.

Usage: py scripts/seo_inject.py
"""
import os
import re
import json
from datetime import datetime

ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)))
SITE_URL = "https://aitoolkit-blog.vercel.app"
GA_ID = "G-XXXXXXXXXX"  # <-- REPLACE WITH YOUR GA4 MEASUREMENT ID

# Google Analytics 4 snippet
GA_SNIPPET = f"""
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}', {{'anonymize_ip': true}});
</script>
"""

FAVICON_TAG = f'<link rel="icon" type="image/svg+xml" href="/favicon.svg">'

def get_html_files():
    files = []
    for root, dirs, filenames in os.walk(ROOT):
        # Skip .git, node_modules, scripts, content
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'scripts', 'content', 'assets']]
        for f in filenames:
            if f.endswith('.html'):
                files.append(os.path.join(root, f))
    return files

def extract_title(content):
    match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    return match.group(1).strip() if match else "AI ToolKit"

def extract_description(content):
    match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content)
    return match.group(1) if match else ""

def extract_date_from_filename(filepath):
    basename = os.path.basename(filepath).replace('.html', '')
    # Try to find date pattern in filename
    match = re.search(r'(\d{4}-\d{2}-\d{2})', basename)
    if match:
        return match.group(1)
    return datetime.now().strftime('%Y-%m-%d')

def extract_article_body(content):
    """Extract first 200 chars of article text for structured data description"""
    # Find article-content div
    match = re.search(r'<div class="article-content">(.*?)</div>\s*</div>\s*</article>', content, re.DOTALL)
    if match:
        text = re.sub(r'<[^>]+>', '', match.group(1))
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:200] + "..."
    return ""

def inject_into_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Determine the URL for this page
    rel_path = os.path.relpath(filepath, ROOT).replace('\\', '/')
    canonical_url = f"{SITE_URL}/{rel_path}"

    # 1. Inject favicon after <meta charset>
    if 'rel="icon"' not in content:
        content = content.replace('<meta charset="UTF-8">', f'<meta charset="UTF-8">\n    {FAVICON_TAG}')

    # 2. Inject canonical URL
    if 'rel="canonical"' not in content:
        content = content.replace('</head>', f'    <link rel="canonical" href="{canonical_url}">\n</head>')

    # 3. Inject GA4 before </head>
    if 'googletagmanager' not in content:
        content = content.replace('</head>', f'{GA_SNIPPET}</head>')

    # 4. If this is an article page, inject JSON-LD structured data
    if '/articles/' in filepath:
        title = extract_title(content).split('—')[0].strip().replace('"', '\\"')
        description = extract_description(content).replace('"', '\\"')
        date = extract_date_from_filename(filepath)
        article_body = extract_article_body(content).replace('"', '\\"')

        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description or article_body,
            "author": {
                "@type": "Organization",
                "name": "AI ToolKit"
            },
            "publisher": {
                "@type": "Organization",
                "name": "AI ToolKit",
                "url": SITE_URL
            },
            "datePublished": date,
            "dateModified": date,
            "mainEntityOfPage": canonical_url,
            "url": canonical_url
        }

        schema_tag = f'\n<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'

        if 'application/ld+json' not in content:
            content = content.replace('</head>', f'{schema_tag}\n</head>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = get_html_files()
    modified = 0
    for f in html_files:
        if inject_into_file(f):
            modified += 1
            print(f"✓ {os.path.relpath(f, ROOT)}")
    print(f"\nSEO injection complete: {modified}/{len(html_files)} files updated")
    print(f"GA ID: {GA_ID} ← Replace 'G-XXXXXXXXXX' with your real GA4 Measurement ID")

if __name__ == "__main__":
    main()
