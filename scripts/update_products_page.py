#!/usr/bin/env python3
"""
AI ToolKit — Products Page Updater
Adds a product to products.html / products showcase and creates product landing page from template.

Usage: py scripts/update_products_page.py --id prod-001
"""
import argparse
import json
import os

PROJECT = os.path.expanduser("~/projects/aitoolkit-blog")
CATALOG_PATH = os.path.join(PROJECT, "content", "products", "catalog.json")
MAIN_JS_PATH = os.path.join(PROJECT, "assets", "main.js")
PRODUCT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — AI ToolKit</title>
    <meta name="description" content="{excerpt}">
    <link rel="stylesheet" href="/assets/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <a href="/" class="logo">🤖 AI ToolKit</a>
            <nav>
                <a href="/">Home</a>
                <a href="/#articles">Articles</a>
                <a href="/products.html">Products</a>
                <a href="/#tools">Tool Reviews</a>
                <a href="/#newsletter">Newsletter</a>
            </nav>
        </div>
    </header>

    <main class="article-page">
        <article class="container">
            <h1>{title}</h1>
            <div class="article-meta">{format_title} | ${price}</div>
            <div class="article-content">
                <p>{excerpt}</p>
                <div class="cta-box">
                    <p><strong>Get {title} for ${price}</strong></p>
                    <a href="https://gumroad.com/l/{slug}" class="btn-primary" target="_blank" rel="noopener sponsored">Buy on Gumroad →</a>
                </div>
                <p>License: personal use only. Instant digital download.</p>
            </div>
        </article>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>© 2026 AI ToolKit. <a href="/disclosure.html">Full disclosure</a>.</p>
        </div>
    </footer>

    <script src="/assets/main.js"></script>
</body>
</html>
"""


def update(product_id):
    with open(CATALOG_PATH, "r") as f:
        catalog = json.load(f)
    prod = next((p for p in catalog["products"] if p["id"] == product_id), None)
    if not prod:
        print(f"ERROR: {product_id} not found")
        return

    slug = prod["slug"]
    html_path = os.path.join(PROJECT, "products", f"{slug}.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)

    html = PRODUCT_TEMPLATE.format(
        title=prod["title"],
        excerpt=prod.get("customer_pain", ""),
        format_title=prod["format"].capitalize(),
        price=prod["price_usd"],
        slug=slug
    )
    with open(html_path, "w") as f:
        f.write(html)

    print(f"Product page created: {html_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    args = parser.parse_args()
    update(args.id)
