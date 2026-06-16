#!/usr/bin/env python3
"""
AI ToolKit — Listing Copy Generator
Generates platform-ready listing copy from a product entry in the catalog.

Usage: py scripts/generate_listing.py --id prod-001
"""
import argparse
import json
import os

PROJECT = os.path.expanduser("~/projects/aitoolkit-blog")
CATALOG_PATH = os.path.join(PROJECT, "content", "products", "catalog.json")


def load_catalog():
    with open(CATALOG_PATH, "r") as f:
        return json.load(f)


def generate_listing(product_id):
    catalog = load_catalog()
    prod = next((p for p in catalog["products"] if p["id"] == product_id), None)
    if not prod:
        print(f"ERROR: Product {product_id} not found.")
        return

    title = prod["title"]
    pain = prod.get("customer_pain", "")
    price = prod["price_usd"]
    fmt = prod["format"]
    tags = prod.get("etsy_tags", [])

    print(f"\n=== GUMROAD LISTING: {product_id} ===\n")
    print(title)
    print(f"\n${price} | {fmt}")
    print(f"\n{pain}")
    print("\nInstant download. Personal use only.\n")
    print("Learn more at https://aitoolkit-blog.vercel.app")

    print(f"\n=== ETSY LISTING: {product_id} ===\n")
    print(f"Title: {title[:140]}")
    print(f"Price: ${price}")
    print(f"Tags: {', '.join(tags)}")
    print(f"\nDescription:\n{pain}\n\nFormat: instant digital download ({fmt})")
    print("License: personal use only")
    print("See more AI tool resources at https://aitoolkit-blog.vercel.app")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True, help="Product ID")
    args = parser.parse_args()
    generate_listing(args.id)
