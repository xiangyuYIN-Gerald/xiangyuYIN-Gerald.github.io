---
title: "ProGRank: Probe-Gradient Reranking to Defend Dense-Retriever RAG from Corpus Poisoning"
authors: "Xiangyu Yin, Yi Qi, Chih-Hong Cheng"
collection: publications
category: conferencepapers
date: 2026-09-01
venue: "European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML-PKDD 2026)"
image: "/images/publications/proground.png"
---

Retrieval-Augmented Generation (RAG) improves the reliability of large language model applications by grounding generation in retrieved evidence, but it also introduces a new attack surface: corpus poisoning. We propose ProGRank, a defense mechanism that operates at the retriever level without requiring retraining. The approach stress-tests each query–passage pair under mild randomized perturbations and extracts probe gradients from the retriever's parameters to identify potentially poisoned content. By combining representational consistency and dispersion risk metrics in a reranking step, ProGRank provides stronger defence performance and a favorable robustness–utility trade-off, while remaining effective against adaptive attacks across multiple datasets and retriever architectures.
