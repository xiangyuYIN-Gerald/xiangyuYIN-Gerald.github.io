---
title: "Boosting Adversarial Training via Fisher-Rao Norm-based Regularization"
authors: "Xiangyu Yin, Wenjie Ruan"
collection: publications
category: conferences
date: 2024-06-01
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2024"
image: "/images/publications/fisher-rao-cvpr2024.png"
---

We address the challenge of maintaining standard generalization performance in adversarially-trained neural networks. Using the Fisher-Rao norm as a geometrically invariant complexity metric, we derive bounds on Rademacher complexity for ReLU-activated networks and identify a complexity variable that correlates with the generalization gap between adversarial and standard training. Based on these theoretical insights, we introduce Logit-Oriented Adversarial Training (LOAT), a regularization framework that reduces the robustness-accuracy trade-off with minimal computational overhead. LOAT demonstrates consistent improvements across multiple established adversarial training algorithms including PGD-AT, TRADES, MART, and DM-AT on various architectures.
