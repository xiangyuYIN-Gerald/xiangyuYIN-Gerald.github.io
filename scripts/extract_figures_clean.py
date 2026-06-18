"""Extract the first real figure image from each PDF, composite onto white background."""
import fitz
import os
from PIL import Image
import io

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "../files/papers")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "../images/publications")
os.makedirs(IMAGES_DIR, exist_ok=True)

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

def composite_on_white(img_bytes, ext):
    """Load image bytes, composite onto white if it has alpha channel."""
    img = Image.open(io.BytesIO(img_bytes))
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        white = Image.new("RGBA", img.size, (255, 255, 255, 255))
        white.paste(img, mask=img.split()[3])
        img = white.convert("RGB")
    else:
        img = img.convert("RGB")
    return img

def extract_first_figure(pdf_path, out_name):
    doc = fitz.open(pdf_path)
    out_path = os.path.join(IMAGES_DIR, f"{out_name}.png")

    # Search first 6 pages, pick the FIRST image above size threshold
    for page_num in range(min(6, len(doc))):
        images = doc[page_num].get_images(full=True)
        for img in images:
            xref = img[0]
            w, h = img[2], img[3]
            if w * h < 40000:   # skip tiny icons/logos
                continue
            base = doc.extract_image(xref)
            try:
                result = composite_on_white(base["image"], base["ext"])
                result.save(out_path)
                print(f"  page {page_num+1}, {w}x{h}px -> {out_path} ({os.path.getsize(out_path)//1024}KB)")
                return
            except Exception as e:
                print(f"  page {page_num+1} image failed ({e}), trying next")
                continue

    print(f"  No embedded figure found — skipping {out_name}")

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
