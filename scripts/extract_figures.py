import fitz
import os
import sys

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "../files/papers")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "../images/publications")
os.makedirs(IMAGES_DIR, exist_ok=True)

# Map PDF filename -> output image name
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

def extract_first_figure(pdf_path, out_name):
    doc = fitz.open(pdf_path)
    best = None  # (area, page_num, img_index, xref)

    # Search first 6 pages for the largest embedded image
    for page_num in range(min(6, len(doc))):
        page = doc[page_num]
        for img in page.get_images(full=True):
            xref = img[0]
            # img[2], img[3] = width, height in the PDF
            w, h = img[2], img[3]
            area = w * h
            if area > 10000:  # skip tiny icons/logos
                if best is None or area > best[0]:
                    best = (area, page_num, xref)

    if best is None:
        print(f"  No suitable image found in first 6 pages, rendering page 1")
        # Fall back: render the first page at moderate resolution
        page = doc[0]
        mat = fitz.Matrix(1.5, 1.5)
        pix = page.get_pixmap(matrix=mat)
        out_path = os.path.join(IMAGES_DIR, f"{out_name}.png")
        pix.save(out_path)
        print(f"  Saved page render -> {out_path}")
        return

    _, page_num, xref = best
    base_image = doc.extract_image(xref)
    img_bytes = base_image["image"]
    ext = base_image["ext"]
    out_path = os.path.join(IMAGES_DIR, f"{out_name}.{ext}")
    with open(out_path, "wb") as f:
        f.write(img_bytes)
    print(f"  page {page_num+1}, size {best[0]//1000}K px -> {out_path}")

for pdf_name, out_name in PDFS.items():
    pdf_path = os.path.join(PAPERS_DIR, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"SKIP (not found): {pdf_name}")
        continue
    print(f"Processing {pdf_name} ...")
    try:
        extract_first_figure(pdf_path, out_name)
    except Exception as e:
        print(f"  ERROR: {e}")

print("Done.")
