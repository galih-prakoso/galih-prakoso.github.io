---
layout: post
lang: en
title: "Whole or Fraction? Understanding Integer Programming"
date: 2026-11-27 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #7: why a rounded LP answer can violate a constraint or fall far from the optimum."
og_image: /assets/img/blog/optimization-day-7-en.png
permalink: /blog/2026/integer-programming/
tags: optimization integer-programming branch-and-bound lp-relaxation industrial-engineering
categories: optimization-series
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=16">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="en" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/share-buttons.js' | relative_url }}?v=4" defer></script>
<script src="{{ '/assets/js/code-view.js' | relative_url }}?v=1" defer></script>

*Series: Optimization in Industrial Engineering, Day #7. Topic: Integer Programming* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/integer-programming/' | relative_url }})

In the previous post ([Day #6]({{ '/blog/2026/convex-vs-non-convex/' | relative_url }})), we discussed when a problem is safe to solve with a local method. This time we look at a different obstacle: **decision variables that must be whole numbers**. A workshop cannot build 2.25 cabinets, and a factory cannot buy 3.75 machines. Problems like this are called **Integer Programming (IP)**.

### What Is Integer Programming?

IP is a linear programming problem with the added requirement that some or all variables must take integer values. Three forms are common:

| Form | Variable rule | Example decision |
| :--- | :--- | :--- |
| Pure IP | All variables are integers | Number of machines to buy |
| Mixed IP | Some integer, some may be fractional | Number of trucks (integer) and liters of fuel (fractional) |
| Binary IP | Variables are only 0 or 1 | Build a plant in a given city or not |

The catering model in [Day #3]({{ '/blog/2026/anatomy-of-an-optimization-model/' | relative_url }}) also used integer variables (number of meals), and its optimum happened to fall on the integer point $$(75,\ 15)$$. That does not always happen, as the following example shows.

### Example: A Furniture Workshop

Suppose a workshop makes two products. Each cabinet (x₁) earns USD 5,000 and each table (x₂) earns USD 8,000. The workshop has 6 workers and 45 boards. Each product uses 1 worker. Each cabinet uses 5 boards and each table uses 9 boards. The model can be written as follows:

$$\max\; Z = 5x_1 + 8x_2 \quad \text{subject to}\quad x_1 + x_2 \le 6,\;\; 5x_1 + 9x_2 \le 45,\;\; x_1, x_2 \ge 0\text{ and integer}$$

If the integer requirement is dropped, the LP optimum is at the corner $$(2.25,\ 3.75)$$ with $$Z = 41.25$$. That answer cannot be built. So what if we round it?

<img src="{{ '/assets/img/blog/optimization-day-7-en.svg' | relative_url }}" alt="Comparison of the fractional LP optimum with integer points in the feasible region of a furniture workshop" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Figure 1. Left: LP reaches a corner of the feasible region. Right: only integer points may be chosen.</em></p>

| Method | Point | Status | Z |
| :--- | :--- | :--- | ---: |
| Round to nearest | (2, 4) | Violates the board constraint (5·2 + 9·4 = 46 > 45) | - |
| Round down | (2, 3) | Feasible | 34 |
| True integer optimum | (0, 5) | Feasible | 40 |

Rounding to the nearest integer gives an infeasible answer, and rounding down leaves Z = 34 even though Z = 40 is achievable. The integer optimum is even located far from the LP optimum. Therefore, **rounding an LP answer is not a reliable method**.

Hillier and Lieberman point out these two pitfalls: a rounded LP answer is not necessarily feasible, and even if it is feasible, it is not necessarily optimal. Rounding can still work well for a smooth one-variable problem, such as John's case in Cuevas et al., where 44.72 gallons is rounded to 45. For problems with several variables and constraints, that rule cannot be trusted.

### Finding the Integer Optimum: Branch and Bound

The most common method is **branch and bound**. The idea is simple:

1. Solve the LP without the integer requirement (the **LP relaxation**). Its value is an upper bound: no integer answer can beat 41.25.
2. If a variable is fractional, say x₁ = 2.25, split the problem into two branches: x₁ ≤ 2 and x₁ ≥ 3. No integer point is lost, because no integer lies between 2 and 3.
3. Solve the LP on each branch, then repeat the splitting.
4. Whenever an integer answer is found, keep it as the best so far. Any branch whose LP bound is no better than that answer is stopped (*pruned*).

In this example, the Python script finishes in 9 nodes. The first integer answer (2, 3) is worth 34, then (1, 4) appears with 37, and finally (0, 5) with 40. The branch x₁ ≥ 3 is stopped because its LP bound is only 39.

### Where Does This Appear in Industrial Engineering?

Integer decisions are everywhere in industry: number of machines, number of operators, facility locations (yes or no), job sequences, and production lot sizes. Some of them are sources of the non-convexity mentioned in [Day #6]({{ '/blog/2026/convex-vs-non-convex/' | relative_url }}), because the set of integer points is not a convex set. As a result, IP is generally much harder to solve than an LP of the same size. This difficulty is one reason metaheuristics are discussed later in this series.

### So What Is It Good For?

There are three practical lessons. First, always check whether the decision variables must be integers before trusting an LP answer. Second, the LP relaxation value is still useful as a bound: the gap between 41.25 and 40 tells us how far the integer answer is from the best possible bound. Third, do not simply round. Use an IP solver or branch and bound so the answer is guaranteed feasible and optimal.

---

### Python Script

The workshop example in this post can be reproduced with the following Python script. It prints the LP relaxation, the rounding results, the integer optimum found by exhaustive search, and every branch-and-bound node, then plots the integer points. It requires Python 3.9+ with `numpy`, `scipy`, and `matplotlib`. The script carries the author's copyright notice (© 2026 Galih Prakoso, MIT License), which must be kept in every copy or modification.

<div class="code-view" data-src="{{ '/assets/code/day-7-integer-programming.py' | relative_url }}"><a href="{{ '/assets/code/day-7-integer-programming.py' | relative_url }}">day-7-integer-programming.py</a></div>

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.4: Solving John's Problem Using the Gradient Descent Method with Matlab, pp. 10 and 12). Springer Nature.

Hillier, F. S., & Lieberman, G. J. (2010). *Introduction to Operations Research* (9th ed.; Chapter 11: Integer Programming, pp. 464–465; Section 11.5: Some Perspectives on Solving Integer Programming Problems, pp. 487–490; Section 11.6: The Branch-and-Bound Technique and Its Application to Binary Integer Programming, p. 491). McGraw-Hill.
