---
title: "Probabilistic Certification of Non-Toxicity in Vision-Language Models via Visual Embedding Smoothing"
authors: "Xiangyu Yin, Jiaxu Liu, Zhen Chen, Jinwei Hu, Yi Dong, Xiaowei Huang, Wenjie Ruan"
collection: publications
category: manuscripts
date: 2025-03-08
venue: "arXiv preprint arXiv:2503.10661"
image: "/images/publications/procert.png"
---

Vision-Language Models (VLMs) are increasingly deployed in safety-critical applications but remain susceptible to jailbreak attacks that induce toxic outputs. While existing defence mechanisms for VLMs, such as model fine-tuning and response evaluation, have shown empirical effectiveness, they are predominantly heuristic, lack theoretical non-toxicity guarantees, and can be bypassed by novel jailbreak techniques. To address these limitations, we introduce a toxicity-aware distance metric that jointly incorporates toxicity scores and semantic similarity, overcoming the inadequacies of each measure in isolation. Building upon this metric, we propose a regression-based probabilistic certification framework for VLMs via randomized smoothing, providing formal guarantees of non-toxic output generation under both Gaussian (ℓ₂) and Laplacian (ℓ₁) perturbations. Distinct from prior randomized smoothing approaches that inject noise in the pixel space, our method injects noise directly into the visual embedding space, enabling robust certification against both adversarial and structure-based jailbreak attacks. Extensive experiments on MiniGPT-4, Qwen2-VL, and CogVLM validate the proposed framework across diverse model architectures, noise scales, and toxicity thresholds, consistently demonstrating strong empirical alignment with theoretical certification guarantees.
