---
layout: post
lang: en
title: "Anatomy of an Optimization Model: Breaking Down Variables, Objectives, and Constraints"
date: 2026-11-19 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #3: how do we turn a real-world problem into a mathematical model?"
permalink: /blog/2026/anatomy-of-an-optimization-model/
tags: optimization mathematical-modeling decision-variables industrial-engineering operations-research
categories: optimization-series
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=11">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="en" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>

*Series: Optimization in Industrial Engineering, Day #3. Topic: General Formulation of an Optimization Problem* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/anatomi-model-optimasi/' | relative_url }})

After seeing how cost-balancing principles work in retail inventory control in the previous post, a practical question naturally follows: **how is a real-world story translated into a set of equations that can be solved systematically?**

In Industrial Engineering, translating a physical situation into symbolic language is called **mathematical modeling**. For beginners, rows of letters like $$x$$, $$y$$, and inequality signs in textbooks can look intimidating at first glance. In reality, these symbols are simply a compact shorthand for telling a very logical story.

### Three Core Building Blocks Behind Every Model

Regardless of how intricate an industrial system may be, from airline crew scheduling to global supply chain design, every optimization model is built from three interconnected components: **decision variables** acting as control levers, **constraints** representing real-world rules and limits, and an **objective function** defining the ultimate target.

<img src="{{ '/assets/img/blog/optimization-day-3-en.svg' | relative_url }}" alt="Anatomy of an optimization model: decision variables, constraints, and objective function" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Figure 1. The three-stage workflow of building a mathematical optimization model.</em></p>

As shown in the diagram above, the decision-making flow always begins by choosing values for the controllable variables, filtering those choices through resource limitations, and finally evaluating the resulting performance on the objective function.

### An Everyday Analogy: Planning a Home Catering Menu

To make the relationship between these three blocks feel concrete, consider, for example, a home-based catering owner who is planning tomorrow's lunch production. The kitchen offers two daily meal boxes: a **Standard Box** and a **Premium Box**.

Every evening, the owner must decide how many portions of each menu to cook the next morning so that daily profit is maximized without exceeding the available grocery budget and kitchen working hours. Breaking this everyday scenario down into the anatomy of an optimization model reveals a clear structure:

1. **Decision Variables: "What Can Be Controlled?"**

   Decision variables represent the quantities whose values are free to be chosen by the decision-maker. In this catering scenario, the controllable levers are the number of portions cooked for each meal option:

   - $$x_1$$ = number of **Standard Boxes** to prepare.
   - $$x_2$$ = number of **Premium Boxes** to prepare.

2. **Objective Function: "What Is the Main Target?"**

   The objective function measures the primary performance goal to be **maximized** (such as profit or efficiency) or **minimized** (such as production cost or waiting time). Suppose each Standard Box yields a net profit of USD 4 and each Premium Box yields USD 7. Total daily profit ($$Z$$) is expressed as:

   $$\max Z = 4x_1 + 7x_2$$

3. **Constraints: "What Are the Rules and Limits?"**

   Without any limits, the caterer would simply cook millions of Premium Boxes to earn infinite profit. In practice, however, limited resources bound what is physically possible:

   - **Ingredient budget constraint:** Ingredients cost USD 6 per Standard Box and USD 10 per Premium Box, while the daily shopping budget is capped at USD 600:

     $$6x_1 + 10x_2 \le 600$$

   - **Kitchen time constraint:** Preparing a Standard Box takes 6 minutes and a Premium Box takes 10 minutes, while effective daily kitchen time is limited to 8 hours (480 minutes):

     $$6x_1 + 10x_2 \le 480$$

   - **Non-negativity constraint:** Negative meal portions do not exist in the real world, requiring $$x_1 \ge 0$$ and $$x_2 \ge 0$$.

### Reading Standard Textbook Notation Without Confusion

Whenever optimization literature is opened, those three building blocks are usually summarized into a single compact template:

$$\begin{aligned} \text{Optimize} \quad & f(\mathbf{x}) \\ \text{Subject to} \quad & g_i(\mathbf{x}) \le b_i, \quad i = 1, 2, \dots, m \\ & \mathbf{x} \in \mathcal{S} \end{aligned}$$

The bold letter $$\mathbf{x}$$ is simply shorthand for the collection of decision variables ($$x_1, x_2, \dots, x_n$$), the function $$f(\mathbf{x})$$ represents the goal to maximize or minimize, and $$g_i(\mathbf{x}) \le b_i$$ lists all the rules that must be respected. Meanwhile, $$\mathcal{S}$$ denotes the **feasible region**: the set of all combinations that satisfy every single constraint simultaneously.

Once this foundational anatomy is clear, any optimization problem, no matter how large, becomes much easier to dissect. Notice that in the catering example above, every equation involved simple straight-line multiplications without curves or exponents. In real engineering systems, however, relationships between variables often bend and curve, a distinction we will explore in the next post on **Linear vs. Non-Linear** problems.

---

### Reference

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.1: What and Where Do We Optimize, pp. 2–3). Springer Nature.
