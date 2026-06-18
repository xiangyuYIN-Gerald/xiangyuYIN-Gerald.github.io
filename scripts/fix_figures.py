import fitz
import os

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "../files/papers")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "../images/publications")

def render_page(pdf_name, out_name, page_num=0, scale=2.0):
    pdf_path = os.path.join(PAPERS_DIR, pdf_name)
    out_path = os.path.join(IMAGES_DIR, f"{out_name}.png")
    doc = fitz.open(pdf_path)
    page = doc[page_num]
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat)
    pix.save(out_path)
    print(f"Rendered page {page_num+1} of {pdf_name} -> {out_path} ({os.path.getsize(out_path)//1024}KB)")

# bev-black-box: render page 1 (index 0) which likely has the overview figure
render_page("bev-black-box.pdf", "bev-black-box", page_num=0, scale=2.0)

# rerorgcrl: render page 1 (index 0)
render_page("rerorgcrl.pdf", "rerorgcrl", page_num=0, scale=2.0)

print("Done.")
