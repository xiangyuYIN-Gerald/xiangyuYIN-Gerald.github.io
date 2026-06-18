"""Render the page containing the FIRST significant figure, with white background."""
import fitz
import os

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "../files/papers")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "../images/publications")

PDFS = {
    "proground.pdf": "proground",
    "fragile-by-design.pdf": "fragile-by-design",
    "falcon-neurips.pdf": "falcon-neurips",
    "gatedfwa.pdf": "gatedfwa",
    "cumulative-consensus-score.pdf": "cumulative-consensus-score",
    "bev-black-box.pdf": "bev-black-box",
    "taiji.pdf": "taiji",
    "cetad.pdf": "cetad",
    "rapid.pdf": "rapid",
    "continuous-geometry-aware.pdf": "continuous-geometry-aware",
    "tiny-refinements.pdf": "tiny-refinements",
    "fisher-rao-cvpr2024.pdf": "fisher-rao-cvpr2024",
    "rerorgcrl.pdf": "rerorgcrl",
    "dimba.pdf": "dimba",
    "temple-aaai2021.pdf": "temple-aaai2021",
}

def find_first_figure_page(doc, max_pages=6, min_area=30000):
    """Return page_num of the first page that contains a significant image."""
    for page_num in range(min(max_pages, len(doc))):
        for img in doc[page_num].get_images(full=True):
            w, h = img[2], img[3]
            if w * h >= min_area:
                return page_num
    return 0  # fallback to page 1

def render_page_white(doc, page_num, scale=2.0):
    page = doc[page_num]
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat, alpha=False, colorspace=fitz.csRGB)
    return pix

for pdf_name, out_name in PDFS.items():
    pdf_path = os.path.join(PAPERS_DIR, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"SKIP: {pdf_name}")
        continue

    out_path = os.path.join(IMAGES_DIR, f"{out_name}.png")
    doc = fitz.open(pdf_path)
    page_num = find_first_figure_page(doc)
    pix = render_page_white(doc, page_num, scale=2.0)
    pix.save(out_path)
    print(f"  {pdf_name}: page {page_num+1} -> {os.path.getsize(out_path)//1024}KB")

print("Done.")
