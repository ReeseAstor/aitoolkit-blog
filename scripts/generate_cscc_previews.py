#!/usr/bin/env python3
"""Generate preview images for AI Customer Support Command Center product."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

SLUG = "ai-customer-support-command-center"

# Brand palette
NAVY = (31, 42, 68)
GOLD = (201, 169, 110)
CREAM = (245, 241, 235)
HONEY = (184, 137, 90)
WHITE = (255, 255, 255)
DARK_TEXT = (30, 30, 30)

# Output directory
OUT_DIR = os.path.join("C:", os.sep, "Users", "sroy2", "projects", "aitoolkit-blog", "assets", "previews", SLUG)
os.makedirs(OUT_DIR, exist_ok=True)

def get_font(size, bold=False):
    """Try to load a system font, fall back to default."""
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()

def draw_rounded_rect(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)

def draw_text_centered(draw, text, y, img_w, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (img_w - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)

def draw_wrapped_text(draw, text, x, y, max_w, font, fill, line_h=None):
    words = text.split()
    lines = []
    cur = []
    for w in words:
        test = ' '.join(cur + [w])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_w and cur:
            lines.append(' '.join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(' '.join(cur))
    if line_h is None:
        bbox = draw.textbbox((0, 0), "Ay", font=font)
        line_h = bbox[3] - bbox[1] + 4
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_h
    return y

# ==========================================
# 1. Hero image (1280x720, 16:9)
# ==========================================
def gen_hero():
    w, h = 1280, 720
    img = Image.new('RGB', (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Gold border
    draw.rounded_rectangle([20, 20, w-20, h-20], radius=15, outline=GOLD, width=3)

    # Top bar
    draw.rectangle([20, 20, w-20, 80], fill=GOLD)
    f_top = get_font(22, bold=True)
    draw_text_centered(draw, "AI ToolKit  |  Digital Product", 40, w, f_top, NAVY)

    # Title
    f_title = get_font(52, bold=True)
    y = 130
    y = draw_wrapped_text(draw, "AI Customer Support", 80, y, w-160, f_title, WHITE, line_h=62)
    y = draw_wrapped_text(draw, "Command Center", 80, y, w-160, f_title, GOLD, line_h=62)
    y += 10
    f_sub = get_font(28, bold=False)
    y = draw_wrapped_text(draw, "2026 Edition", 80, y, w-160, f_sub, CREAM, line_h=36)

    # Stats bar
    y += 20
    draw.rectangle([80, y, w-80, y+100], fill=CREAM)
    f_stat = get_font(20, bold=True)
    f_stat_val = get_font(32, bold=True)
    stats = [("35", "Prompts"), ("12", "Checklists"), ("5", "Tools"), ("$17", "Price")]
    col_w = (w - 160) // 4
    for i, (val, label) in enumerate(stats):
        cx = 80 + i * col_w + col_w // 2
        draw_text_centered(draw, val, y + 20, w, f_stat_val, NAVY)
        draw_text_centered(draw, label, y + 55, w, f_stat, HONEY)
        if i < 3:
            draw.line([80 + (i+1)*col_w, y+20, 80 + (i+1)*col_w, y+80], fill=HONEY, width=2)

    y += 120

    # Tool badges
    f_badge = get_font(16, bold=True)
    tools = ["Copy.ai", "Canva", "Synthesia", "Speechify", "Surfer"]
    badge_y = y
    badge_x = 80
    for tool in tools:
        bbox = draw.textbbox((0, 0), tool, font=f_badge)
        tw = bbox[2] - bbox[0] + 30
        draw_rounded_rect(draw, [badge_x, badge_y, badge_x+tw, badge_y+35], 8, HONEY)
        draw.text((badge_x+15, badge_y+8), tool, font=f_badge, fill=WHITE)
        badge_x += tw + 15

    # Bottom tagline
    y += 60
    f_tag = get_font(22, bold=False)
    draw_text_centered(draw, "Turn a 3-person support team into a self-service content engine", y, w, f_tag, CREAM)

    out = os.path.join(OUT_DIR, f"{SLUG}-preview-hero.png")
    img.save(out, "PNG")
    print(f"Hero: {out}")

# ==========================================
# 2. Etsy main image (2700x2025, 4:3)
# ==========================================
def gen_etsy():
    w, h = 2700, 2025
    img = Image.new('RGB', (w, h), CREAM)
    draw = ImageDraw.Draw(img)

    # Navy header band
    draw.rectangle([0, 0, w, 400], fill=NAVY)
    f_brand = get_font(40, bold=True)
    draw_text_centered(draw, "AI ToolKit  |  Digital Product", 150, w, f_brand, GOLD)

    # Title
    f_title = get_font(90, bold=True)
    y = 480
    y = draw_wrapped_text(draw, "AI Customer Support", 200, y, w-400, f_title, NAVY, line_h=105)
    y = draw_wrapped_text(draw, "Command Center", 200, y, w-400, f_title, GOLD, line_h=105)
    y += 15
    f_sub = get_font(50, bold=False)
    y = draw_wrapped_text(draw, "2026 Edition", 200, y, w-400, f_sub, HONEY, line_h=60)

    # Stats
    y += 40
    draw.rectangle([200, y, w-200, y+250], fill=NAVY)
    f_stat_val = get_font(70, bold=True)
    f_stat_label = get_font(36, bold=True)
    stats = [("35", "Prompts"), ("12", "Checklists"), ("5", "Affiliate Tools"), ("$17", "Price")]
    col_w = (w - 400) // 4
    for i, (val, label) in enumerate(stats):
        cx = 200 + i * col_w + col_w // 2
        bbox = draw.textbbox((0, 0), val, font=f_stat_val)
        tw = bbox[2] - bbox[0]
        draw.text((cx - tw//2, y + 40), val, font=f_stat_val, fill=GOLD)
        bbox2 = draw.textbbox((0, 0), label, font=f_stat_label)
        tw2 = bbox2[2] - bbox2[0]
        draw.text((cx - tw2//2, y + 130), label, font=f_stat_label, fill=CREAM)
        if i < 3:
            draw.line([200 + (i+1)*col_w, y+40, 200 + (i+1)*col_w, y+200], fill=GOLD, width=3)

    y += 300

    # What's inside
    f_section = get_font(44, bold=True)
    draw.text((200, y), "What's Inside:", font=f_section, fill=NAVY)
    y += 70

    f_body = get_font(32, bold=False)
    items = [
        "35 copy-paste AI prompts for help center articles, macros, and email replies",
        "12 weekly production checklists (Monday-Friday + monthly + quarterly)",
        "Tool-stack map: Copy.ai, Canva, Synthesia, Speechify, Surfer (verified pricing)",
        "90-minute help center content workflow: article + screenshots + video + audio + SEO",
        "Free alternatives for every tool in the stack",
        "Format: Instant digital download (PDF + Markdown)",
    ]
    for item in items:
        draw.ellipse([200, y+12, 225, y+37], fill=GOLD)
        y = draw_wrapped_text(draw, item, 260, y, w-460, f_body, DARK_TEXT, line_h=42)
        y += 8

    # Footer
    f_footer = get_font(28, bold=False)
    draw_text_centered(draw, "aitoolkit-blog.vercel.app  |  Personal use license", h-80, w, f_footer, NAVY)

    out = os.path.join(OUT_DIR, f"{SLUG}-preview-etsy.png")
    img.save(out, "PNG")
    print(f"Etsy: {out}")

# ==========================================
# 3. Social / carousel square (1080x1080, 1:1)
# ==========================================
def gen_social():
    w, h = 1080, 1080
    img = Image.new('RGB', (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Gold border
    draw.rounded_rectangle([15, 15, w-15, h-15], radius=12, outline=GOLD, width=4)

    # Top bar
    draw.rectangle([15, 15, w-15, 75], fill=GOLD)
    f_top = get_font(20, bold=True)
    draw_text_centered(draw, "AI ToolKit  |  Digital Product", 35, w, f_top, NAVY)

    # Title
    f_title = get_font(44, bold=True)
    y = 130
    y = draw_wrapped_text(draw, "AI Customer", 60, y, w-120, f_title, WHITE, line_h=52)
    y = draw_wrapped_text(draw, "Support", 60, y, w-120, f_title, WHITE, line_h=52)
    y = draw_wrapped_text(draw, "Command Center", 60, y, w-120, f_title, GOLD, line_h=52)
    y += 10
    f_sub = get_font(26, bold=False)
    y = draw_wrapped_text(draw, "2026 Edition", 60, y, w-120, f_sub, CREAM, line_h=32)

    # Stats box
    y += 15
    draw.rectangle([60, y, w-60, y+180], fill=CREAM)
    f_stat_val = get_font(44, bold=True)
    f_stat = get_font(22, bold=True)
    stats = [("35", "Prompts"), ("12", "Checklists"), ("$17", "Price")]
    col_w = (w - 120) // 3
    for i, (val, label) in enumerate(stats):
        cx = 60 + i * col_w + col_w // 2
        bbox = draw.textbbox((0, 0), val, font=f_stat_val)
        tw = bbox[2] - bbox[0]
        draw.text((cx - tw//2, y + 30), val, font=f_stat_val, fill=NAVY)
        bbox2 = draw.textbbox((0, 0), label, font=f_stat)
        tw2 = bbox2[2] - bbox2[0]
        draw.text((cx - tw2//2, y + 90), label, font=f_stat, fill=HONEY)
        if i < 2:
            draw.line([60 + (i+1)*col_w, y+30, 60 + (i+1)*col_w, y+140], fill=HONEY, width=2)

    y += 210

    # Tool badges
    f_badge = get_font(18, bold=True)
    tools = ["Copy.ai", "Canva", "Synthesia", "Speechify", "Surfer"]
    badge_y = y
    badge_x = 60
    for tool in tools:
        bbox = draw.textbbox((0, 0), tool, font=f_badge)
        tw = bbox[2] - bbox[0] + 24
        draw_rounded_rect(draw, [badge_x, badge_y, badge_x+tw, badge_y+35], 6, HONEY)
        draw.text((badge_x+12, badge_y+8), tool, font=f_badge, fill=WHITE)
        badge_x += tw + 12

    y += 70

    # Tagline
    f_tag = get_font(20, bold=False)
    y = draw_wrapped_text(draw, "Turn a 3-person support team into a self-service content engine that deflects 100-300 tickets per month", 60, y, w-120, f_tag, CREAM, line_h=28)

    y += 20

    # CTA box
    draw.rectangle([60, y, w-60, y+80], fill=GOLD)
    f_cta = get_font(28, bold=True)
    draw_text_centered(draw, "Get It Now -- $17", y + 25, w, f_cta, NAVY)

    y += 110
    f_url = get_font(18, bold=False)
    draw_text_centered(draw, "aitoolkit-blog.vercel.app", y, w, f_url, CREAM)

    out = os.path.join(OUT_DIR, f"{SLUG}-preview-social.png")
    img.save(out, "PNG")
    print(f"Social: {out}")

if __name__ == '__main__':
    gen_hero()
    gen_etsy()
    gen_social()
    print("All previews generated.")
