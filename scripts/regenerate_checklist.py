#!/usr/bin/env python3
"""
AI ToolKit — Regenerate Upload Checklist
Scans the catalog, landing pages, and preview assets; writes:
  - content/products/UPLOAD_CHECKLIST.md
  - content/products/UPLOAD_CHECKLIST.csv

Usage:
    py scripts/regenerate_checklist.py
"""
import csv
import json
import os

PROJECT = os.path.expanduser("~/projects/aitoolkit-blog")
CATALOG_PATH = os.path.join(PROJECT, "content", "products", "catalog.json")
CHECKLIST_MD = os.path.join(PROJECT, "content", "products", "UPLOAD_CHECKLIST.md")
CHECKLIST_CSV = os.path.join(PROJECT, "content", "products", "UPLOAD_CHECKLIST.csv")
PRODUCTS_DIR = os.path.join(PROJECT, "products")
PREVIEWS_DIR = os.path.join(PROJECT, "assets", "previews")


def count_previews(slug):
    total = 0
    # New PanicProofPrintables previews
    preview_dir = os.path.join(PREVIEWS_DIR, slug)
    if os.path.isdir(preview_dir):
        total += len([f for f in os.listdir(preview_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))])
    # Legacy upload-ready preview images
    legacy_dir = os.path.join(PROJECT, "content", "products", "upload-ready", slug, "preview-images")
    if os.path.isdir(legacy_dir):
        total += len([f for f in os.listdir(legacy_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))])
    return total


def landing_status(slug):
    return "OK" if os.path.exists(os.path.join(PRODUCTS_DIR, f"{slug}.html")) else "MISSING"


def deliverable_status(prod):
    upload_dir = os.path.join(PROJECT, "content", "products", "upload-ready", prod["slug"])
    files_dir = os.path.join(upload_dir, "files")

    # 1. If a zip exists at upload-ready root, that's the deliverable for bundles
    if os.path.isdir(upload_dir):
        zips = sorted([f for f in os.listdir(upload_dir) if f.lower().endswith(".zip")])
        if zips:
            return zips[0]

    # 2. Files folder: prefer PDF, then ZIP, then first non-empty file
    if os.path.isdir(files_dir):
        files = sorted([f for f in os.listdir(files_dir) if os.path.getsize(os.path.join(files_dir, f)) > 0])
        for f in files:
            if f.lower().endswith(".pdf"):
                return f
        for f in files:
            if f.lower().endswith(".zip"):
                return f
        if files:
            return files[0]

    # 3. Root deliverable naming convention
    root_files = os.listdir(PROJECT)
    for f in root_files:
        if f.lower().startswith(prod["slug"].replace("-", "_")) and f.lower().endswith((".pdf", ".zip")):
            return f
    return "MISSING"


def main():
    with open(CATALOG_PATH, "r") as f:
        catalog = json.load(f)

    rows = []
    for prod in catalog["products"]:
        status = prod.get("status", "").upper()
        rows.append({
            "id": prod["id"],
            "title": prod["title"],
            "price": f"${prod['price_usd']}",
            "deliverable": deliverable_status(prod),
            "landing": landing_status(prod["slug"]),
            "previews": count_previews(prod["slug"]),
            "verification": status,
        })

    # Markdown
    md = """# AI ToolKit — Upload Checklist

_Generated automatically. Verify all rows show READY before uploading to Gumroad/Etsy._

| ID | Title | Price | Deliverable | Landing | Previews | Verification |
| --- | --- | ---: | --- | --- | ---: | --- |
"""
    for r in rows:
        md += f"| {r['id']} | {r['title']} | {r['price']} | {r['deliverable']} | {r['landing']} | {r['previews']} | {r['verification']} |\n"

    with open(CHECKLIST_MD, "w") as f:
        f.write(md)

    # CSV
    with open(CHECKLIST_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "price", "deliverable", "landing", "previews", "verification"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {CHECKLIST_MD} and {CHECKLIST_CSV}")


if __name__ == "__main__":
    main()
