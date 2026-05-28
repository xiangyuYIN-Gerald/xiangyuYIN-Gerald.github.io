---
title: "Tiny Refinements Elicit Resilience: Toward Efficient Prefix-Model Against LLM Red-Teaming"
authors: "Jiaxu Liu, Xiangyu Yin, Sihao Wu, Jianhong Wang, Meng Fang, Xinping Yi, Xiaowei Huang"
collection: publications
category: manuscripts
date: 2024-05-21
venue: "arXiv preprint arXiv:2405.12604"
image: "/images/publications/tiny-refinements.jpeg"
---

We present a plug-and-play prefix module that reconstructs input prompts using fewer than 30 additional tokens to mitigate toxic outputs from large language models. The sentinel model addresses parameter inefficiency and limited model accessibility for fine-tuning large target models. We employ interleaved training using Proximal Policy Optimization to jointly optimize both red team and sentinel models, incorporating a value head-sharing mechanism inspired by multi-agent centralized critic approaches. Testing across text-to-text and text-to-image applications demonstrates effectiveness against larger models including Llama-2, GPT-3.5, and Stable Diffusion, positioning the framework as a practical safety enhancement for a wide range of applications.
