---
title: "GatedFWA: Linear Flash Windowed Attention with Gated Associative Memory"
authors: "Jiaxu Liu, Yuhe Bai, Xiangyu Yin, Christos-Savvas Bouganis"
collection: publications
category: manuscripts
date: 2025-12-01
venue: "arXiv preprint arXiv:2512.07782"
image: "/images/publications/gated.png"
---

Modern autoregressive models rely on attention, yet the Softmax full attention in Transformers scales quadratically with sequence length. While Sliding Window Attention (SWA) improves efficiency, its difference-style update under an Associative Memory interpretation renders the training objective effectively unbounded. We propose GatedFWA, which preserves SWA's efficiency while stabilizing memory updates and making gradient flow controllable through a learnable decay bias accumulated as per-token/head gates in attention logits. The implementation includes a fused one-pass gate preprocessing and a FlashAttention-compatible kernel. Experiments demonstrate competitive throughput with negligible overhead and better use of global context on language modeling tasks, with seamless integration with token compression methods.
