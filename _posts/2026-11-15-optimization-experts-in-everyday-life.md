---
layout: post
lang: en
title: "Without Realizing It, We Are 'Optimization Experts' in Everyday Life"
date: 2026-11-15 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #1: what and where do we optimize?"
permalink: /blog/2026/optimization-experts-in-everyday-life/
tags: optimization industrial-engineering decision-making mathematical-modeling
categories: optimization-series
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=7">

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>

*Series: Optimization in Industrial Engineering, Day #1. Topic 1.1: What and Where Do We Optimize?* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/ahli-optimasi-kehidupan-sehari-hari/' | relative_url }})

In everyday life, we are frequently faced with multiple choices that often make reaching a decision challenging. For example, when planning to buy a house, a dilemma arises between choosing a spacious home far from the workplace or a smaller house located right near the city center. Of course, this decision is further complicated by the funds available. Another example appears when selecting a vehicle: buyers have to weigh the purchase price, fuel efficiency, driving comfort, and after-sales service.

The same pattern emerges when choosing food, clothing, computers, a career, or even a city to live in. Naturally, people always prefer the best possible options. However, because real-world decisions operate under limited resources and constraints, it is impossible to get the absolute best in every single aspect at once. Instead, people settle on the **optimal option**: the most reasonable decision after carefully weighing priorities, resources, and constraints. This everyday decision-making process is what is known as **optimization**.

### Understanding "Trade-Offs" Through Vehicle Design

From an engineering standpoint, optimization can also be understood as deciding what cost or sacrifice one is willing to accept in order to obtain a desired benefit. Clear evidence of this appears in how automotive engineers design four distinct types of vehicles:

- **Sports Cars:** When the goal is to maximize acceleration, designers maximize engine power while minimizing vehicle weight through a compact body. The trade-off is that drivers accept higher fuel consumption and more expensive maintenance.
- **Fuel-Efficient Cars:** Conversely, to minimize fuel consumption, cars are typically built smaller with low-power engines, sacrificing high acceleration in the process.
- **Large Family Cars:** Here, engineers aim to maintain a balance between acceleration and fuel economy while meeting a strict constraint: carrying multiple passengers, often requiring three rows of seats.
- **Cargo Trucks:** Trucks are equipped with very powerful engines to haul heavy cargo, yet because of their massive size, they end up with the lowest acceleration in practice.

<img src="{{ '/assets/img/blog/optimization-day-1-en.svg' | relative_url }}" alt="Illustration of optimization concepts in everyday life and engineering" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Figure 1. Comparison of trade-offs in everyday decisions, four automotive engineering designs, and the three pillars of optimization modeling.</em></p>

This raises an interesting question: *would it be possible to design a cargo truck with the acceleration of a sports car?* Technically, yes, by manufacturing an enormous engine. However, manufacturers choose not to do this because calculations show that production costs would be far too high and sales volume would be low. Simply put, such a design would not be optimal.

On the consumer side, the exact same optimization logic applies. Many people intentionally avoid spending too much of their budget on a car so they can allocate those financial resources toward other expenses they consider more important or enjoyable.

### Translating Real-World Problems into Mathematical Models

In Industrial Engineering and Management, optimization serves as a core tool for strategic decision-making. Common examples include minimizing the production cost of a product while maintaining a specific quality level, maximizing company profits under budget constraints, or allocating employees to different tasks as efficiently as possible.

To solve these physical, real-world situations systematically, they must first be expressed in mathematical terms, a process known as **modeling**. In general, every optimization model consists of three main components:

1. **Decision Variables:** The independent inputs that can be controlled or adjusted (such as x₁, x₂, …, xₙ), like engine size or order quantity.
2. **Objective Function:** The primary performance measure f(x) to be maximized (such as profit or acceleration) or minimized (such as cost or waiting time), which depends on the decision variables.
3. **Constraints:** The real-world limitations or conditions that bound decisions, such as budget caps, storage capacity, or seating requirements.

The goal of an optimization algorithm is not merely to find the minimum or maximum value of the objective function, but to determine the **exact values of the decision variables** that produce that optimal outcome. As we move forward in this series, upcoming posts will gradually explore different types of optimization problems, ranging from linear to nonlinear, convex to non-convex, and single-peak (*unimodal*) to multi-peak (*multimodal*), in a clear and approachable manner.

---

### Reference

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.1: What and Where Do We Optimize, pp. 1–3). Springer Nature.
