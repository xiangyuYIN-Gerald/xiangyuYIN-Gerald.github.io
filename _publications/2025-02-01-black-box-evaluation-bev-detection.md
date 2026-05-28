---
title: "A Black-Box Evaluation Framework for Semantic Robustness in Bird's Eye View Detection"
authors: "Fu Wang, Yanghao Zhang, Xiangyu Yin, Guangliang Cheng, Zeyu Fu, Xiaowei Huang, Wenjie Ruan"
collection: publications
category: conferences
date: 2025-02-01
venue: "AAAI Conference on Artificial Intelligence 2025"
image: "/images/publications/bird_eye.png"
---

We address robustness concerns in camera-based Bird's Eye View (BEV) perception systems used in autonomous driving. Our black-box evaluation framework adversarially optimizes three semantic perturbations—geometric transformation, color shifting, and motion blur—to test model vulnerability. We introduce a smoothed distance-based surrogate function to replace the mAP metric and present SimpleDIRECT, a deterministic optimisation algorithm that utilises observed slopes to guide the optimisation process. Benchmarking ten recent BEV models, we find that PolarFormer demonstrates superior robustness while BEVDet shows significant vulnerability, with precision reduced to zero under adversarial perturbations.
