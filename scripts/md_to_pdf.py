#!/usr/bin/env python3
"""
AI ToolKit — Markdown to PDF converter for digital products.
Usage: py scripts/md_to_pdf.py --input path/to/file.md --output path/to/file.pdf --title "Title"
"""
import argparse
import os
import re
import markdown
from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, title="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.doc_title = title

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "", 8)
            self.set_text_color(120, 120, 140)
            self.cell(0, 10, self.doc_title, ln=True, align="L")
            self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 140)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def clean_markdown(text):
    # Convert markdown to HTML, then strip tags for plain text conversion
    html = markdown.markdown(text, extensions=["fenced_code", "tables"])
    # Replace code blocks with a visual block marker
    html = re.sub(r"<pre><code>(.*?)</code></pre>", r"<div class=\"code\">\1</div>", html, flags=re.S)
    return html


def strip_tags(html):
    # Simple tag stripper
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"</p>", "\n\n", text)
    text = re.sub(r"</h[123456]>", "\n\n", text)
    text = re.sub(r"</li>", "\n", text)
    text = re.sub(r"</tr>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text


def sanitize_for_pdf(text):
    # FPDF only supports Latin-1 characters by default with Helvetica
    # Replace common unicode chars
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u201c": '"',
        "\u201d": '"',
        "\u2018": "'",
        "\u2019": "'",
        "\u2022": "- ",
        "\u2705": "[X]",
        "\u2713": "[X]",
        "\ud83e\udd16": "",
        "\u2192": "->",
        "\u2026": "...",
        "\u2014": "-",
        "`": "'",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    # Remove any remaining non-Latin1 glyphs
    text = text.encode("latin-1", "replace").decode("latin-1")
    # Normalize whitespace
    text = text.replace("\t", "    ")
    return text


def escape_line(text):
    # Collapse runs of whitespace and strip
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def md_to_pdf(input_path, output_path, title):
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = clean_markdown(md_text)
    text = strip_tags(html)
    text = sanitize_for_pdf(text)

    pdf = PDF(title=title)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Title page
    if len(title) > 40:
        title_font_size = 18
    else:
        title_font_size = 24
    pdf.set_font("Helvetica", "B", title_font_size)
    pdf.set_text_color(30, 30, 40)
    pdf.cell(0, 20, sanitize_for_pdf(title), new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(80, 80, 100)
    pdf.multi_cell(0, 8, "AI ToolKit Digital Product\nPersonal use only. Do not redistribute.", align="C")
    pdf.add_page()

    # Body
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 40)

    body_width = pdf.w - (pdf.l_margin + pdf.r_margin)

    lines = text.split("\n")
    for raw_line in lines:
        line = escape_line(raw_line)
        stripped = line.strip()
        if not stripped:
            pdf.ln(3)
            continue

        # Headings
        if stripped.startswith("# "):
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_text_color(60, 60, 90)
            pdf.ln(5)
            pdf.multi_cell(body_width, 8, stripped[2:])
            pdf.ln(2)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(30, 30, 40)
        elif stripped.startswith("## "):
            pdf.set_font("Helvetica", "B", 13)
            pdf.set_text_color(60, 60, 90)
            pdf.ln(4)
            pdf.multi_cell(body_width, 7, stripped[3:])
            pdf.ln(1)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(30, 30, 40)
        elif stripped.startswith("### "):
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(60, 60, 90)
            pdf.multi_cell(body_width, 6, stripped[4:])
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(30, 30, 40)
        elif stripped.startswith("- ") or stripped.startswith("* "):
            pdf.set_x(pdf.l_margin + 5)
            pdf.multi_cell(body_width - 10, 6, f"- {stripped[2:]}")
        elif re.match(r"^\d+\.\s", stripped):
            pdf.set_x(pdf.l_margin + 5)
            pdf.multi_cell(body_width - 10, 6, stripped)
        elif stripped.startswith("```"):
            continue
        else:
            pdf.multi_cell(body_width, 6, stripped)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    md_to_pdf(args.input, args.output, args.title)
