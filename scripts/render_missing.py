"""For PDFs with only vector figures, render the page that first contains a figure caption."""
import fitz
import os
import re

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "../files/papers")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "../images/publications")

# pdf -> (out_name, which page index to render)
# Manually identified from the PDFs by looking for "Figure 1" caption
MISSING = {
    "gatedfwa.pdf":   ("gatedfwa",   1),   # Figure 1 on page 2
    "bev-black-box.pdf": ("bev-black-box", 3),  # Figure 1 on page 4
    "rerorgcrl.pdf":  ("rerorgcrl",  1),   # Figure 1 on page 2
}

for pdf_name, (out_name, page_idx) in MISSING.items():
    pdf_path = os.path.join(PAPERS_DIR, pdf_name)
    out_path = os.path.join(IMAGES_DIR, f"{out_name}.png")
    doc = fitz.open(pdf_path)
    page = doc[page_idx]
    mat = fitz.Matrix(2.0, 2.0)
    pix = page.get_pixmap(matrix=mat, alpha=False, colorspace=fitz.csRGB)
    pix.save(out_path)
    print(f"{pdf_name}: rendered page {page_idx+1} -> {os.path.getsize(out_path)//1024}KB")

print("Done.")
