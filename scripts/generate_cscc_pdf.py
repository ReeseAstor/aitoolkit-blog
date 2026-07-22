#!/usr/bin/env python3
"""Generate PDF from the AI Customer Support Command Center markdown."""

import re
import sys
from fpdf import FPDF

class SafePDF(FPDF):
    def safe(self, text):
        return (text
            .replace('\u2014', ' -- ').replace('\u2013', ' - ')
            .replace('\u2018', "'").replace('\u2019', "'")
            .replace('\u201c', '"').replace('\u201d', '"')
            .replace('\u2026', '...').replace('\u00a0', ' ')
            .replace('\u2022', ' - ').replace('\u25cf', ' - ')
            .replace('\u2192', '->').replace('\u2190', '<-')
            .replace('\u2014', '--')
        )

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, self.safe(f'AI Customer Support Command Center (2026 Edition) - Page {self.page_no()}'), 0, 0, 'C')

    def h1(self, text):
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(31, 42, 68)  # navy
        self.multi_cell(0, 10, self.safe(text))
        self.ln(4)

    def h2(self, text):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(201, 169, 110)  # gold
        self.multi_cell(0, 8, self.safe(text))
        self.ln(2)

    def h3(self, text):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(31, 42, 68)
        self.multi_cell(0, 7, self.safe(text))
        self.ln(1)

    def body(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5, self.safe(text))
        self.ln(1)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        x = self.get_x()
        self.cell(5, 5, '-')
        self.multi_cell(0, 5, self.safe(text))
        self.ln(0.5)

    def code_block(self, text):
        self.set_font('Courier', '', 7)
        self.set_text_color(50, 50, 50)
        self.set_fill_color(245, 241, 235)  # cream
        max_chars = 110
        page_w = self.w - 2 * self.l_margin
        lines = text.split('\n')
        for line in lines:
            # Reset x to left margin for each line
            self.set_x(self.l_margin)
            # Split long lines at char level
            chunk = line[:max_chars]
            remaining = line[max_chars:]
            while chunk:
                self.cell(page_w, 3.5, self.safe(chunk), 0, 1, 'L', fill=True)
                chunk = remaining[:max_chars]
                remaining = remaining[max_chars:]
        self.ln(2)

    def table_row(self, cells, widths=None):
        self.set_font('Helvetica', '', 8)
        self.set_text_color(40, 40, 40)
        if widths is None:
            page_width = self.w - 2 * self.l_margin
            col_w = page_width / len(cells)
            widths = [col_w] * len(cells)
        for i, cell in enumerate(cells):
            self.cell(widths[i], 6, self.safe(cell)[:40], 1, 0, 'L')
        self.ln()

    def hr(self):
        self.set_draw_color(201, 169, 110)
        self.set_line_width(0.5)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(3)


def md_to_pdf(input_path, output_path, title):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pdf = SafePDF()
    pdf.set_title(title)
    pdf.set_author('AI ToolKit')
    pdf.add_page()

    lines = content.split('\n')
    in_code = False
    code_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Handle code blocks
        if stripped.startswith('```'):
            if in_code:
                # End code block
                pdf.code_block('\n'.join(code_buffer))
                code_buffer = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Skip empty lines
        if not stripped:
            pdf.ln(2)
            i += 1
            continue

        # Headers
        if stripped.startswith('# ') and not stripped.startswith('## '):
            pdf.h1(stripped[2:])
        elif stripped.startswith('## '):
            pdf.h2(stripped[3:])
        elif stripped.startswith('### '):
            pdf.h3(stripped[4:])
        elif stripped.startswith('---'):
            pdf.hr()
        elif stripped.startswith('- [ ]'):
            pdf.bullet('[ ] ' + stripped[6:])
        elif stripped.startswith('- '):
            pdf.bullet(stripped[2:])
        elif stripped.startswith('|') and '|' in stripped[1:]:
            # Table row - skip table formatting, just render as text
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if cells and not all(c.startswith('-') for c in cells):
                pdf.table_row(cells)
        elif stripped.startswith('**') and stripped.endswith('**') and stripped.count('**') == 2:
            pdf.h3(stripped[2:-2])
        else:
            pdf.body(stripped)

        i += 1

    # Handle any remaining code buffer
    if code_buffer:
        pdf.code_block('\n'.join(code_buffer))

    pdf.output(output_path)
    print(f"PDF generated: {output_path}")
    print(f"Pages: {pdf.page_no()}")

if __name__ == '__main__':
    input_path = r"C:\Users\sroy2\projects\aitoolkit-blog\content\products\ai-customer-support-command-center.md"
    output_path = r"C:\Users\sroy2\projects\aitoolkit-blog\content\products\ai-customer-support-command-center.pdf"
    md_to_pdf(input_path, output_path, "AI Customer Support Command Center (2026 Edition)")
