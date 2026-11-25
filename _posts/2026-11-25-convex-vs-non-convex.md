---
layout: post
lang: en
title: "Bowl or Egg Carton? Understanding Convex and Non-Convex Problems"
date: 2026-11-25 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #6: why convexity lets us trust a local optimum as the global optimum."
og_image: /assets/img/blog/optimization-day-6-en.png
permalink: /blog/2026/convex-vs-non-convex/
tags: optimization convex non-convex local-optimum industrial-engineering
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

*Series: Optimization in Industrial Engineering, Day #6. Topic: Convexity (Convex vs. Non-Convex)* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/convex-vs-non-convex/' | relative_url }})

In the previous post ([Day #5]({{ '/blog/2026/unimodal-vs-multimodal/' | relative_url }})), we saw that an objective function can have many local maximum or minimum points. The next question: **is there a property we can check up front to be sure there is only one minimum point?** That property is called **convexity**. The result of the check decides whether an optimization problem can be solved with certainty or must be handled with care.

---

### A Marble in a Bowl vs. a Marble in an Egg Carton

Suppose a marble is dropped into a smooth bowl. Wherever the marble lands, it rolls down and stops at the bottom of the bowl. There is nowhere else to stop.

Now drop the same marble into an egg carton. The marble stops in the nearest dimple from where it landed, even though a deeper dimple may be just a few centimeters away.

The bowl is a picture of a **convex** problem (for minimization), while the egg carton is a **non-convex** problem. A rolling marble behaves like the gradient method: it only knows the slope right beneath it.

---

### Convex Functions

According to Hillier and Lieberman, a function $$f(x)$$ is **convex** if the line segment connecting any two points on its graph (called a *chord*) lies **on or above** the graph. In other words, a convex curve only bends upward, like a bowl. For functions with a second derivative, there is a quick test:

| Condition (for all $$x$$) | Status of $$f(x)$$ |
| :--- | :--- |
| $$f''(x) \ge 0$$ | Convex (curves upward or does not curve) |
| $$f''(x) \le 0$$ | Concave (curves downward or does not curve) |
| Sign of $$f''(x)$$ varies | Neither convex nor concave |

A linear function has $$f''(x) = 0$$ everywhere, so it satisfies both conditions in the table. This means a linear function is both convex and concave: its chords lie exactly on the line itself.

Convex functions also have two properties that are useful in practice. First, **the sum of convex functions is also convex**, so a total cost built from several convex cost components stays convex. Second, for maximization we look for a **concave** objective function, because the negative of a convex function is concave.

<img src="{{ '/assets/img/blog/optimization-day-6-en.svg' | relative_url }}" alt="Comparison of a convex bowl where every starting point reaches the same minimum point and a wavy non-convex curve where the starting point decides which minimum point is reached" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Figure 1. Convex function: every starting point rolls to the same minimum point, and every chord lies above the curve (left). Non-convex function: a chord can cut below the curve, and the marble stops in the nearest dimple (right).</em></p>

---

### The Feasible Region Must Be Convex Too

So far we have only discussed the objective function. Yet most industrial problems have constraints, and those constraints form the **feasible region**, the set of all decisions we are allowed to choose. For the convexity guarantee to hold, this region must also be a **convex set**: if we pick any two feasible decisions, every decision between them must be feasible as well. A region with an inward dent fails this test, because two points on the edges of the dent are joined by a line that partly leaves the region. Two facts are worth remembering:

- The feasible region of **every linear programming problem is a convex set**. This is one reason LP problems are relatively easy to solve with results that can be trusted.
- In a non-linear problem with constraints $$g_i(x) \le b_i$$, the feasible region is a convex set when every $$g_i(x)$$ is a convex function.

A problem whose objective function is convex (for minimization) and whose feasible region is convex is called a **convex programming problem**. For convex programming problems, the Kuhn–Tucker optimality conditions are not only necessary but also sufficient for a global minimum (Rao). In other words, no relative minimum or *saddle point* can trap the search.

---

### Example: When the Region Curves

Hillier and Lieberman modify their classic two-product problem as follows. The goal is to maximize $$Z = 3x_1 + 5x_2$$ subject to:

- $$x_1 \le 4$$
- $$2x_2 \le 14$$
- $$8x_1 - x_1^2 + 14x_2 - x_2^2 \le 49$$ (non-linear)
- $$x_1, x_2 \ge 0$$

The non-linear constraint makes the feasible region non-convex. As a test, take two feasible points, $$(0, 7)$$ and $$(4, 3)$$. Their midpoint is $$(2, 5)$$, and it violates the constraint because $$8(2) - 2^2 + 14(5) - 5^2 = 57 > 49$$, so it lies outside the feasible region.

As a result, this problem has **two local maximum points**:

| Point $$(x_1, x_2)$$ | $$Z = 3x_1 + 5x_2$$ | Status |
| :--- | :--- | :--- |
| $$(0,\ 7)$$ | 35 | Global maximum |
| $$(4,\ 3)$$ | 27 | Local maximum only |

The objective function is linear, so very simple, yet a single curved constraint is enough to create a trap. A local search that arrives at $$(4, 3)$$ finds no better neighbor and stops, even though $$Z$$ is still 8 short of the best answer.

---

### Where This Appears in Industrial Engineering

The basic **EOQ** model from [Day #2]({{ '/blog/2026/johns-problem-eoq-inventory/' | relative_url }}) is a good convex example. Its total cost is a convex curve with a single minimum point, so gradient descent finds the best order quantity from any starting point. Once volume discounts are added (as in [Day #5]({{ '/blog/2026/unimodal-vs-multimodal/' | relative_url }})), the cost curve breaks and convexity is lost. The script at the end of this post tests both cases with the chord test (the discount prices are only illustrative).

Other common sources of non-convexity in industrial problems are fixed setup costs, economies of scale, integer decisions (2.4 trucks is not a possible choice), and sequence-dependent decisions, such as the order of jobs on a machine.

---

### So What Is It Good For?

| | Convex problem | Non-convex problem |
| :--- | :--- | :--- |
| Local optimum | Always the global optimum | May be only local |
| Starting point | Barely matters | Can decide the result |
| Typical methods | Gradient methods, KKT conditions, LP solvers | Multi-start, branch-and-bound, metaheuristics |
| Proof of optimality | Available | Usually unavailable, or very expensive |

In real problems, it is often hard to be sure that the whole objective function and every constraint are convex. A good habit is to check each building block, that is, each cost term and each constraint. If all of them are convex, the whole problem is convex and a simple method can be trusted. If even one of them curves the wrong way, treat the answer of a local method as a candidate, not a certainty.

---

### Python Script

The chord test and the Hillier and Lieberman example in this post can be reproduced with the Python script below. It prints a table of test results for three one-variable functions (including EOQ), finds the local maximum points of the two-product example, and plots both. It needs Python 3.9+ with `numpy` and `matplotlib`. The script carries the author's copyright notice (© 2026 Galih Prakoso, MIT License), which must be kept in any copy or modification.

<div class="code-view" data-src="{{ '/assets/code/day-6-convexity.py' | relative_url }}"><a href="{{ '/assets/code/day-6-convexity.py' | relative_url }}">day-6-convexity.py</a></div>

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.1: What and Where Do We Optimize, p. 3; Chapter 2, Section 2.5: Plotting Partial Costs and the Total Cost, p. 28). Springer Nature.

Hillier, F. S., & Lieberman, G. J. (2010). *Introduction to Operations Research* (9th ed.; Chapter 12, Section 12.2: Graphical Illustration of Nonlinear Programming Problems, pp. 542–547; Appendix 2: Convexity, pp. 993–996). McGraw-Hill.

Rao, S. S. (2009). *Engineering Optimization: Theory and Practice* (4th ed.; Chapter 2, Section 2.6: Convex Programming Problem, p. 104). John Wiley & Sons.
