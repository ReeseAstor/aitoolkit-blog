#!/usr/bin/env python3
"""
AI ToolKit — Digital Product Generator
Reads products/catalog.json and builds a complete upload-ready package for the next planned product.

Usage: py scripts/generate_product.py
Output: ~/projects/aitoolkit-blog/content/products/upload-ready/<slug>/
"""
import argparse
import json
import os
from datetime import datetime

PROJECT = os.path.expanduser("~/projects/aitoolkit-blog")
CATALOG_PATH = os.path.join(PROJECT, "content", "products", "catalog.json")
UPLOAD_BASE = os.path.join(PROJECT, "content", "products", "upload-ready")


def load_catalog():
    with open(CATALOG_PATH, "r") as f:
        return json.load(f)


def save_catalog(catalog):
    with open(CATALOG_PATH, "w") as f:
        json.dump(catalog, f, indent=2)


def next_product(catalog):
    for p in catalog["products"]:
        if p.get("status") == "planned":
            return p
    return None


def ensure_product_dirs(slug):
    prod_dir = os.path.join(UPLOAD_BASE, slug)
    os.makedirs(os.path.join(prod_dir, "files"), exist_ok=True)
    return prod_dir


def write_readme(prod, prod_dir, affiliate_links):
    affiliates = "\n".join(
        f"- **{name}**: {affiliate_links.get(name, 'https://example.com/?via=aitoolkit')}"
        for name in prod["affiliate_tie"]
    )
    body = f"""# {prod['title']}

{prod.get('customer_pain', 'A focused digital product built by AI ToolKit.')}

Format: {prod['format']}
Price: ${prod['price_usd']}

## Recommended tool stack

{affiliates or '- No affiliate tie-ins for this product.'}

All links use `?via=aitoolkit`. FTC disclosure: https://aitoolkit-blog.vercel.app/disclosure.html

## What's included

- Placeholder: add the deliverable files in `files/`
- Listing copy in `listing-gumroad.md` and `listing-etsy.md`
- Social assets in `social-launch-assets.md`

## License

Personal use only. Do not resell or redistribute.
"""
    with open(os.path.join(prod_dir, "README.md"), "w") as f:
        f.write(body)


def write_listings(prod, prod_dir):
    gumroad = f"""{prod['title']}

{prod.get('customer_pain', 'A focused digital product from AI ToolKit.')}

Price: ${prod['price_usd']}

Format: {prod['format']} — instant digital download.

This product ties to the AI ToolKit article: {prod['article_tie']}

Get more AI tool reviews and resources: https://aitoolkit-blog.vercel.app

License: Personal use only.
"""
    etsy = f"""Title: {prod['title'][:140]}

Tags: {', '.join(prod.get('etsy_tags', []))}

Description:
{prod.get('customer_pain', 'A focused digital product from AI ToolKit.')}

Format: instant digital download
License: personal use only

See more at https://aitoolkit-blog.vercel.app
"""
    with open(os.path.join(prod_dir, "listing-gumroad.md"), "w") as f:
        f.write(gumroad)
    with open(os.path.join(prod_dir, "listing-etsy.md"), "w") as f:
        f.write(etsy)


def write_social(prod, prod_dir):
    body = f"""# Social launch assets — {prod['slug']}

## Instagram / LinkedIn carousel

Slide 1: {prod['title']} — link in bio
Slide 2: Problem: {prod.get('customer_pain', '')}
Slide 3: Solution: this {prod['format']} gives you the exact system.
Slide 4: CTA → aitoolkit-blog.vercel.app/products

## Twitter/X thread

1/ {prod.get('customer_pain', '')}
2/ I built {prod['title']} to fix it.
3/ Grab it at aitoolkit-blog.vercel.app/products

## Short-form video script

"I was stuck because {prod.get('customer_pain', 'of this problem').lower()}."
"Then I built a system: {prod['title']}."
"Link in bio. ${prod['price_usd']}."
"""
    with open(os.path.join(prod_dir, "social-launch-assets.md"), "w") as f:
        f.write(body)


def generate_product(product_id=None, mark_ready=False):
    catalog = load_catalog()
    prod = None
    if product_id:
        for p in catalog["products"]:
            if p["id"] == product_id:
                prod = p
                break
        if not prod:
            print(f"ERROR: Product {product_id} not found.")
            return
    else:
        prod = next_product(catalog)
        if not prod:
            print("No planned products remaining in catalog.")
            return

    print(f"Generating package for: {prod['title']} ({prod['id']})")
    prod_dir = ensure_product_dirs(prod["slug"])

    affiliate_links = {
        "Copy.ai": "https://copy.ai/?via=aitoolkit",
        "Writesonic": "https://writesonic.com/?via=aitoolkit",
        "Synthesia": "https://synthesia.io/?via=aitoolkit",
        "Speechify": "https://speechify.com/?via=aitoolkit",
        "AdCreative.ai": "https://adcreative.ai/?via=aitoolkit",
        "Canva": "https://canva.com/?via=aitoolkit",
    }

    write_readme(prod, prod_dir, affiliate_links)
    write_listings(prod, prod_dir)
    write_social(prod, prod_dir)

    if mark_ready:
        prod["status"] = "ready"
        save_catalog(catalog)

    print(f"Package created: {prod_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="Product ID to generate (default: next planned)")
    parser.add_argument("--ready", action="store_true", help="Mark the product as ready in catalog.json")
    args = parser.parse_args()
    generate_product(product_id=args.id, mark_ready=args.ready)
