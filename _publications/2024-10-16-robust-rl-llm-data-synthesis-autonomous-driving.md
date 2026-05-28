---
title: "Robust RL with LLM-Driven Data Synthesis and Policy Adaptation for Autonomous Driving"
authors: "Sihao Wu, Jiaxu Liu, Xiangyu Yin, Guangliang Cheng, Xingyu Zhao, Meng Fang, Xinping Yi, Xiaowei Huang"
collection: publications
category: manuscripts
date: 2024-10-16
venue: "arXiv preprint arXiv:2410.12568"
image: "/images/publications/rapid.png"
---

We present RAPID, a framework that integrates large language models into reinforcement learning for autonomous driving. RAPID combines three key elements: using offline data from an LLM-based driving agent to distill expert knowledge into faster RL policies, introducing robust distillation techniques to preserve both performance and robustness from the LLM teacher, and employing a mix-of-policy strategy with a policy adapter for joint decision-making during online fine-tuning. Extensive experiments demonstrate that RAPID successfully integrates LLM knowledge into scaled RL policies in a way that is efficient, adaptable, and robust while reducing knowledge loss under distribution shift.
