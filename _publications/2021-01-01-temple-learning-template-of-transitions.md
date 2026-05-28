---
title: "Temple: Learning Template of Transitions for Sample Efficient Multi-task RL"
authors: "Yanchao Sun, Xiangyu Yin, Furong Huang"
collection: publications
category: conferences
date: 2021-01-01
venue: "AAAI Conference on Artificial Intelligence 2021"
image: "/images/publications/temple-aaai2021.png"
---

Transferring knowledge among various environments is important for efficiently learning multiple tasks online. Most existing methods directly use previously learned models or optimal policies to learn new tasks, but these may be inefficient when the underlying models or optimal policies are substantially different across tasks. We propose Template Learning (TempLe), a PAC-MDP method for multi-task reinforcement learning applicable to tasks with varying state/action spaces without prior knowledge of inter-task mappings. TempLe gains sample efficiency by extracting similarities of transition dynamics across tasks even when their underlying models or optimal policies have limited commonalities. We present two algorithms for an online and a finite-model setting respectively, proving that TempLe achieves much lower sample complexity than single-task learners or state-of-the-art multi-task methods. Systematic experiments show that TempLe universally outperforms state-of-the-art multi-task methods in various settings and regimes.
