#!/usr/bin/env python3
"""
AI ToolKit / PanicProofPrintables — Preview Image Generator
Generates marketplace preview images in the PanicProofPrintables design system.

Usage:
    py scripts/generate_preview_images.py

Outputs:
    assets/previews/<slug>/<slug>-preview-{hero,etsy,social}.png
"""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

PROJECT = os.path.expanduser("~/projects/aitoolkit-blog")
OUT_DIR = os.path.join(PROJECT, "assets", "previews")

# PanicProofPrintables design tokens
NAVY = "#1f2a44"
NAVY_LIGHT = "#2a3a5c"
GOLD = "#c9a96e"
CREAM = "#f5f1eb"
HONEY = "#b8895a"
WHITE = "#ffffff"

PRODUCTS = [
    {
        "slug": "aitoolkit-ultimate-bundle",
        "title": "AI ToolKit Ultimate Bundle",
        "subtitle": "All 9 Products + Future Updates",
        "category": "Bundle",
        "price": "$97",
        "strike": "$146",
        "save": "Save 34%",
        "bullets": [
            "SOPs, prompts, templates & swipes",
            "SEO, outbound, social, video, image",
            "Instant download + lifetime updates",
        ],
        "badge": "COMPLETE LIBRARY",
    },
    {
        "slug": "ai-marketing-operations-vault",
        "title": "AI Marketing Operations Vault",
        "subtitle": "SOPs + SEO System + Cold Email Swipes",
        "category": "Bundle",
        "price": "$39",
        "strike": "$52",
        "save": "Save 25%",
        "bullets": [
            "15 drop-in marketing SOPs",
            "25-point SEO checklist + prompts",
            "40 cold email sequences that book meetings",
        ],
        "badge": "MARKETING OPERATING SYSTEM",
    },
    {
        "slug": "ai-content-creator-vault",
        "title": "AI Content Creator Vault",
        "subtitle": "Video Prompts + Social Calendar + YouTube Toolkit",
        "category": "Bundle",
        "price": "$37",
        "strike": "$45",
        "save": "Save 18%",
        "bullets": [
            "50 viral short-form video prompts",
            "30-day AI social media calendar",
            "YouTube scripts, thumbnails & SEO templates",
        ],
        "badge": "CONTENT PRODUCTION STACK",
    },
]


def get_fonts():
    """Return (font_regular, font_bold, font_light) paths if available."""
    candidates = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path, path, path
    return None, None, None


FONT_REGULAR, FONT_BOLD, FONT_LIGHT = get_fonts()


def font(size, bold=False, italic=False):
    """Load a TrueType font at the requested size. Falls back to default."""
    path = FONT_BOLD if bold else FONT_REGULAR
    if path is None:
        return ImageFont.load_default()
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle."""
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def generate_preview(product, kind):
    """Generate one preview image for a product."""
    if kind == "hero":
        width, height = 1280, 720
    elif kind == "etsy":
        width, height = 2700, 2025
    elif kind == "social":
        width, height = 1080, 1080
    else:
        raise ValueError(kind)

    img = Image.new("RGB", (width, height), NAVY)
    draw = ImageDraw.Draw(img)

    # Scale factor relative to hero 1280px width
    scale = width / 1280

    # Decorative geometric blocks
    # Top-right gold thin line accent
    line_y = int(28 * scale)
    line_x_start = width - int(220 * scale)
    draw.line([(line_x_start, line_y), (width, line_y)], fill=GOLD, width=int(3 * scale))

    # Bottom-left honey wood block
    block_w = int(140 * scale)
    block_h = int(8 * scale)
    draw.rectangle([0, height - block_h, block_w, height], fill=HONEY)

    # Left vertical gold bar
    bar_w = int(6 * scale)
    draw.rectangle([0, int(120 * scale), bar_w, int(540 * scale)], fill=GOLD)

    # Logo / watermark area
    logo_font = font(int(14 * scale), bold=True)
    draw.text((int(32 * scale), int(24 * scale)), "AI ToolKit", font=logo_font, fill=GOLD)

    # Brand micro-mark
    micro = font(int(10 * scale))
    draw.text((int(32 * scale), int(44 * scale)), "PanicProofPrintables Design System", font=micro, fill=CREAM)

    y = int(110 * scale)
    x = int(64 * scale)

    # Category badge
    badge_text = product["badge"]
    badge_font = font(int(12 * scale), bold=True)
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    badge_w = (bbox[2] - bbox[0]) + int(24 * scale)
    badge_h = (bbox[3] - bbox[1]) + int(14 * scale)
    draw_rounded_rect(
        draw,
        [x, y, x + badge_w, y + badge_h],
        radius=int(6 * scale),
        fill=None,
        outline=GOLD,
        width=int(1 * scale),
    )
    draw.text((x + int(12 * scale), y + int(7 * scale)), badge_text, font=badge_font, fill=GOLD)

    y += badge_h + int(18 * scale)

    # Title
    title_font = font(int(42 * scale), bold=True)
    title_lines = textwrap.wrap(product["title"], width=22 if kind == "social" else 34)
    for line in title_lines:
        draw.text((x, y), line, font=title_font, fill=CREAM)
        y += int(52 * scale)

    # Decorative right-side stack suggesting bundled pages/tools
    stack_x = width - int(320 * scale)
    stack_y = int(160 * scale)
    stack_w = int(180 * scale)
    stack_h = int(24 * scale)
    for i in range(5):
        offset = i * int(14 * scale)
        alpha_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        a_draw = ImageDraw.Draw(alpha_layer)
        a_draw.rounded_rectangle(
            [stack_x + offset, stack_y + offset, stack_x + stack_w + offset, stack_y + stack_h + offset],
            radius=int(6 * scale),
            fill=(201, 169, 110, 50),
            outline=(201, 169, 110, 120),
            width=int(1 * scale),
        )
        img = Image.alpha_composite(img.convert("RGBA"), alpha_layer).convert("RGB")
        draw = ImageDraw.Draw(img)

    # Subtitle
    subtitle_font = font(int(20 * scale))
    sub_lines = textwrap.wrap(product["subtitle"], width=45 if kind == "social" else 70)
    for line in sub_lines:
        draw.text((x, y), line, font=subtitle_font, fill=GOLD)
        y += int(28 * scale)

    y += int(24 * scale)

    # Price + save block
    price_font = font(int(52 * scale), bold=True)
    strike_font = font(int(26 * scale))
    save_font = font(int(16 * scale), bold=True)
    price = product["price"]
    strike = product["strike"]
    save = product["save"]

    p_w = draw.textbbox((0, 0), price, font=price_font)[2]
    s_w = draw.textbbox((0, 0), strike, font=strike_font)[2]
    gap = int(14 * scale)
    total_w = p_w + gap + s_w + gap + int(100 * scale)

    # Save pill
    pill_h = int(30 * scale)
    pill_y = y + int(18 * scale)
    pill_w = int(110 * scale)
    pill_x = x + p_w + gap + s_w + gap
    draw_rounded_rect(draw, [pill_x, pill_y, pill_x + pill_w, pill_y + pill_h], radius=int(15 * scale), fill=GOLD)
    draw.text((pill_x + int(18 * scale), pill_y + int(6 * scale)), save, font=save_font, fill=NAVY)

    draw.text((x, y), price, font=price_font, fill=WHITE)
    draw.text((x + p_w + gap, y + int(20 * scale)), strike, font=strike_font, fill=CREAM)
    # strikethrough
    st_y = y + int(33 * scale)
    draw.line([(x + p_w + gap, st_y), (x + p_w + gap + s_w, st_y)], fill=CREAM, width=int(2 * scale))

    y += int(80 * scale)

    # Bullet list
    bullet_font = font(int(17 * scale))
    for bullet in product["bullets"]:
        wrap_w = 32 if kind == "social" else 55 if kind == "etsy" else 60
        lines = textwrap.wrap(bullet, width=wrap_w)
        for i, line in enumerate(lines):
            prefix = "•" if i == 0 else "  "
            draw.text((x, y), f"{prefix} {line}", font=bullet_font, fill=CREAM)
            y += int(26 * scale)
        y += int(6 * scale)

    # CTA hint
    y = height - int(64 * scale)
    cta_font = font(int(13 * scale), bold=True)
    draw.text((x, y), "Instant download  ·  ai toolkit-blog.vercel.app/products", font=cta_font, fill=GOLD)

    return img


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for prod in PRODUCTS:
        prod_dir = os.path.join(OUT_DIR, prod["slug"])
        os.makedirs(prod_dir, exist_ok=True)
        for kind in ("hero", "etsy", "social"):
            img = generate_preview(prod, kind)
            filename = f"{prod['slug']}-preview-{kind}.png"
            path = os.path.join(prod_dir, filename)
            img.save(path, "PNG")
            print(f"Wrote {path}")


if __name__ == "__main__":
    main()
