---
title: "Cumulative Consensus Score: A Label-Free Signal for Monitoring Object Detectors in Deployment"
authors: "Avinaash Manoharan, Xiangyu Yin, Domenik Helm, Chih-Hong Cheng"
collection: publications
category: conferences
date: 2026-10-16
venue: "IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) 2027 — Accepted"
image: "/images/publications/cumulative.png"
---

We introduce the Cumulative Consensus Score (CCS), a method for evaluating object detection models without ground-truth annotations. CCS applies test-time data augmentation to each image and measures the spatial consistency of predicted bounding boxes across augmented views using Intersection over Union. The approach achieves over 90% congruence with F1-score, Probabilistic Detection Quality, and Optimal Correction Cost in controlled experiments. Operating in a model-agnostic manner across single-stage and two-stage detectors, CCS works at the case level to identify underperforming scenarios and provides a robust foundation for DevOps-style continuous monitoring of object detectors in real-world deployment.
