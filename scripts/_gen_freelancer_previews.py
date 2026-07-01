"""Generate hero/etsy/social preview images for ai-freelancer-stack-playbook."""
from PIL import Image, ImageDraw, ImageFont
import os

NAVY = (31, 42, 68)       # #1f2a44
GOLD = (201, 169, 110)     # #c9a96e
CREAM = (245, 241, 235)   # #f5f1eb
HONEY = (184, 137, 90)    # #b8895a
DARK = (28, 28, 32)
LIGHT_NAVY = (44, 60, 92)

PRODUCT = {
    "slug": "ai-freelancer-stack-playbook",
    "title_line_1": "The AI Freelancer Stack",
    "title_line_2": "2026 Playbook",
    "subtitle": "5-Function System + 30-Day Rollout + 40+ Prompts",
    "price": "$22",
    "tagline": "Run a One-Person Business on AI",
}

def load_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\verdana.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_hero():
    # 1280x720 hero / Gumroad cover
    img = Image.new("RGB", (1280, 720), CREAM)
    d = ImageDraw.Draw(img)
    # Navy left panel
    d.rectangle([0, 0, 540, 720], fill=NAVY)
    # Gold accent stripe
    d.rectangle([540, 0, 552, 720], fill=GOLD)
    # Right panel background
    d.rectangle([552, 0, 1280, 720], fill=CREAM)

    # Decorative "5-Function Stack" diagram in left panel
    cx = 270
    cy = 360
    functions = ["LAND", "DELIVER", "BILL", "GROW", "REUSE"]
    for i, fn in enumerate(functions):
        y = cy - 220 + i * 100
        # Circle
        d.ellipse([cx - 30, y - 30, cx + 30, y + 30], fill=GOLD)
        # Number
        num_font = load_font(28, bold=True)
        d.text((cx - 8, y - 18), str(i + 1), font=num_font, fill=NAVY)
        # Label
        lbl_font = load_font(22, bold=True)
        d.text((cx + 50, y - 12), fn, font=lbl_font, fill=CREAM)
        # Connector line
        if i < len(functions) - 1:
            d.line([(cx, y + 30), (cx, y + 70)], fill=CREAM, width=3)

    # Title (right panel)
    f1 = load_font(60, bold=True)
    f2 = load_font(60, bold=True)
    f3 = load_font(28)
    f4 = load_font(34, bold=True)
    f5 = load_font(22)

    d.text((600, 180), PRODUCT["title_line_1"], font=f1, fill=NAVY)
    d.text((600, 250), PRODUCT["title_line_2"], font=f2, fill=GOLD)
    d.text((600, 340), PRODUCT["subtitle"], font=f3, fill=DARK)

    # Price tag
    d.rectangle([600, 420, 760, 490], fill=NAVY)
    d.text((625, 432), PRODUCT["price"], font=f4, fill=CREAM)

    # Tagline
    d.text((600, 520), PRODUCT["tagline"], font=f5, fill=HONEY)

    # Brand mark
    d.text((600, 640), "AI ToolKit", font=load_font(18, bold=True), fill=NAVY)

    out_dir = f"assets/previews/{PRODUCT['slug']}"
    os.makedirs(out_dir, exist_ok=True)
    img.save(f"{out_dir}/{PRODUCT['slug']}-preview-hero.png", "PNG", optimize=True)
    print(f"hero saved -> {out_dir}/{PRODUCT['slug']}-preview-hero.png")

def draw_etsy():
    # 2700x2025 Etsy main image
    img = Image.new("RGB", (2700, 2025), CREAM)
    d = ImageDraw.Draw(img)

    # Top navy band
    d.rectangle([0, 0, 2700, 380], fill=NAVY)
    # Gold divider
    d.rectangle([0, 380, 2700, 396], fill=GOLD)

    f_brand = load_font(70, bold=True)
    f_year = load_font(60, bold=True)
    f_title1 = load_font(120, bold=True)
    f_title2 = load_font(120, bold=True)
    f_sub = load_font(50)
    f_bullet = load_font(44, bold=True)
    f_price = load_font(110, bold=True)
    f_tag = load_font(40)

    # Brand + year
    d.text((120, 130), "AI TOOLKIT", font=f_brand, fill=GOLD)
    d.text((120, 220), "2026 EDITION", font=f_year, fill=CREAM)

    # Big title
    d.text((120, 480), "The AI Freelancer", font=f_title1, fill=NAVY)
    d.text((120, 620), "Stack Playbook", font=f_title2, fill=GOLD)

    # Subtitle
    d.text((120, 800), "5-Function System + 30-Day Rollout", font=f_sub, fill=DARK)
    d.text((120, 870), "+ 40+ Copy-Paste Prompts", font=f_sub, fill=DARK)

    # Bullets
    bullets = [
        "Pick the right tool for each of 5 functions",
        "30-day rollout plan you can print and follow",
        "40+ prompts for Copy.ai, Canva, Synthesia, Speechify",
        "Stack audit worksheet + pricing calculator",
        "What NOT to AI (the 7 reputation risks)",
    ]
    for i, b in enumerate(bullets):
        # Gold checkmark
        d.ellipse([120, 1040 + i * 100, 165, 1085 + i * 100], fill=GOLD)
        d.text((195, 1045 + i * 100), b, font=f_bullet, fill=NAVY)

    # Price box
    d.rectangle([120, 1640, 700, 1830], fill=NAVY)
    d.text((180, 1670), "$22", font=f_price, fill=GOLD)
    d.text((180, 1780), "PDF + Markdown", font=f_tag, fill=CREAM)

    # Right-side decorative stack diagram
    cx = 2200
    cy = 1200
    functions = ["LAND", "DELIVER", "BILL", "GROW", "REUSE"]
    for i, fn in enumerate(functions):
        y = cy - 360 + i * 160
        d.ellipse([cx - 60, y - 60, cx + 60, y + 60], fill=GOLD)
        nf = load_font(54, bold=True)
        d.text((cx - 16, y - 32), str(i + 1), font=nf, fill=NAVY)
        lf = load_font(46, bold=True)
        d.text((cx + 100, y - 24), fn, font=lf, fill=NAVY)
        if i < len(functions) - 1:
            d.line([(cx, y + 60), (cx, y + 100)], fill=NAVY, width=8)

    out_dir = f"assets/previews/{PRODUCT['slug']}"
    os.makedirs(out_dir, exist_ok=True)
    img.save(f"{out_dir}/{PRODUCT['slug']}-preview-etsy.png", "PNG", optimize=True)
    print(f"etsy saved -> {out_dir}/{PRODUCT['slug']}-preview-etsy.png")

def draw_social():
    # 1080x1080 social square
    img = Image.new("RGB", (1080, 1080), NAVY)
    d = ImageDraw.Draw(img)

    # Gold border
    d.rectangle([30, 30, 1050, 1050], outline=GOLD, width=8)

    f_brand = load_font(36, bold=True)
    f_title1 = load_font(72, bold=True)
    f_title2 = load_font(72, bold=True)
    f_sub = load_font(32)
    f_price = load_font(96, bold=True)
    f_tag = load_font(28)
    f_stat = load_font(48, bold=True)

    # Brand
    d.text((80, 100), "AI TOOLKIT", font=f_brand, fill=GOLD)
    d.text((80, 150), "2026 PLAYBOOK", font=load_font(28, bold=True), fill=CREAM)

    # Title
    d.text((80, 280), "The AI Freelancer", font=f_title1, fill=CREAM)
    d.text((80, 360), "Stack", font=f_title2, fill=GOLD)

    # Subtitle
    d.text((80, 480), "5 Functions. 30 Days. 40+ Prompts.", font=f_sub, fill=CREAM)
    d.text((80, 520), "One system for a one-person business.", font=f_sub, fill=CREAM)

    # Stat callouts
    stats = [
        ("5", "FUNCTIONS"),
        ("30", "DAY PLAN"),
        ("40+", "PROMPTS"),
    ]
    for i, (val, lbl) in enumerate(stats):
        x = 80 + i * 320
        y = 620
        d.rectangle([x, y, x + 280, y + 180], fill=CREAM)
        d.text((x + 90, y + 25), val, font=f_stat, fill=NAVY)
        d.text((x + 50, y + 110), lbl, font=load_font(20, bold=True), fill=HONEY)

    # Price
    d.rectangle([80, 850, 460, 990], fill=GOLD)
    d.text((140, 870), "$22", font=f_price, fill=NAVY)
    d.text((140, 970), "PDF + Markdown", font=f_tag, fill=NAVY)

    # Footer
    d.text((700, 920), "aitoolkit-blog.vercel.app", font=f_tag, fill=CREAM)

    out_dir = f"assets/previews/{PRODUCT['slug']}"
    os.makedirs(out_dir, exist_ok=True)
    img.save(f"{out_dir}/{PRODUCT['slug']}-preview-social.png", "PNG", optimize=True)
    print(f"social saved -> {out_dir}/{PRODUCT['slug']}-preview-social.png")

if __name__ == "__main__":
    draw_hero()
    draw_etsy()
    draw_social()
    print("done")
