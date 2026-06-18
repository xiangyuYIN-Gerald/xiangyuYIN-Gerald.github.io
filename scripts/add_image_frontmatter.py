import os
import re

PUB_DIR = os.path.join(os.path.dirname(__file__), "../_publications")

# Map publication filename stem -> image path
IMAGE_MAP = {
    "2026-03-01-proground-probe-gradient-reranking": "/images/publications/proground.png",
    "2026-02-01-fragile-by-design": "/images/publications/fragile-by-design.png",
    "2026-01-01-falcon-activation-manipulation-llm": "/images/publications/falcon-neurips.png",
    "2025-12-01-gatedfwa-linear-flash-windowed-attention": "/images/publications/gatedfwa.png",
    "2025-10-01-cumulative-consensus-score": "/images/publications/cumulative-consensus-score.png",
    "2025-03-13-taiji-textual-anchoring-jailbreak": "/images/publications/taiji.png",
    "2025-03-08-cetad-certified-toxicity-aware-distance": "/images/publications/cetad.png",
    "2025-02-01-black-box-evaluation-bev-detection": "/images/publications/bev-black-box.png",
    "2024-10-16-robust-rl-llm-data-synthesis-autonomous-driving": "/images/publications/rapid.png",
    "2024-09-01-continuous-geometry-aware-graph-diffusion": "/images/publications/continuous-geometry-aware.jpeg",
    "2024-06-01-boosting-adversarial-training-fisher-rao": "/images/publications/fisher-rao-cvpr2024.png",
    "2024-05-21-tiny-refinements-elicit-resilience": "/images/publications/tiny-refinements.jpeg",
    "2024-02-01-representation-based-robustness-gcrl": "/images/publications/rerorgcrl.png",
    "2024-01-01-dimba-black-box-attack": "/images/publications/dimba.jpeg",
    "2021-01-01-temple-learning-template-of-transitions": "/images/publications/temple-aaai2021.png",
}

for fname in os.listdir(PUB_DIR):
    if not fname.endswith(".md"):
        continue
    stem = fname[:-3]
    image = IMAGE_MAP.get(stem)
    if not image:
        continue

    path = os.path.join(PUB_DIR, fname)
    with open(path) as f:
        content = f.read()

    # Skip if image already set
    if "image:" in content:
        print(f"SKIP (already has image): {fname}")
        continue

    # Insert image: line before closing ---
    content = re.sub(r"(---\n)([\s\S]*?)(---\n)",
                     lambda m: m.group(1) + m.group(2) + f"image: \"{image}\"\n" + m.group(3),
                     content, count=1)
    with open(path, "w") as f:
        f.write(content)
    print(f"Updated: {fname}")

print("Done.")
