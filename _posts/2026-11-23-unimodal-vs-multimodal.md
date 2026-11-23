---
layout: post
lang: en
title: "One Peak or Many? Understanding Unimodal and Multimodal Problems"
date: 2026-11-23 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #5: why the number of peaks in an objective function decides whether a simple method is enough."
og_image: /assets/img/blog/optimization-day-5-en.png
permalink: /blog/2026/unimodal-vs-multimodal/
tags: optimization unimodal multimodal local-optimum industrial-engineering
categories: optimization-series
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=15">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="en" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/share-buttons.js' | relative_url }}?v=2" defer></script>
<script src="{{ '/assets/js/code-view.js' | relative_url }}?v=1" defer></script>

*Series: Optimization in Industrial Engineering, Day #5. Topic: Modality (Unimodal vs. Multimodal)* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/satu-puncak-vs-banyak-puncak/' | relative_url }})

The previous post showed that once the relationship among variables becomes curved, the landscape of the objective function can turn wavy. The next question is more specific: **how many peaks (or valleys) does that landscape have?** The answer decides whether a simple method is enough or whether a smarter tool is needed.

---

### Climbing One Hill vs. Crossing a Mountain Range

Consider a hiker who must reach the highest point, but thick fog lets them see only the ground under their feet. The strategy is simple: always step in the uphill direction, and stop when no direction goes higher.

- On a **single hill**, this strategy always works. Wherever the hiker starts, every climb leads to the only summit, which is therefore the highest one.
- In a **mountain range with many peaks**, the same strategy can be deceptive. The hiker may stop on top of a small hill because every nearby direction goes down, while a much higher summit stands behind the next valley.

This "always go uphill" strategy is exactly how gradient methods work (*gradient ascent* for maximization, *gradient descent* for minimization). At each point, the method computes the steepest uphill direction and steps that way. It was briefly mentioned in Day #4.

---

### Definition: Unimodal and Multimodal

In optimization, a problem is **multimodal** when its objective function has more than one locally optimal solution (*local optima*). The best of them is, by definition, the **global optimum**. A **unimodal** problem, in contrast, has only one peak (for maximization) or one valley (for minimization), so its local optimum is also the global one.

The reference book of this series links unimodality to **convex** functions. That link should be read carefully: a convex function is always unimodal, but not every unimodal function is convex. A curve can have a single peak without having the shape of a smooth bowl. The difference between convex and non-convex problems gets its own post next.

<img src="{{ '/assets/img/blog/optimization-day-5-en.svg' | relative_url }}" alt="Comparison of a unimodal landscape with a single peak and a multimodal landscape whose local peak traps a gradient method" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Figure 1. Unimodal landscape: every uphill path ends at the same summit (left). Multimodal landscape: the result depends on the starting point, and the hiker can stop on a local peak (right).</em></p>

---

### A Concrete Example: The Peaks Function

The reference book uses the **Peaks** function, a two-variable function often used to test optimization algorithms. It has three peaks within $$-3 \le x_1, x_2 \le 3$$. Numerical computation for this post gives:

| Peak | Location $$(x_1, x_2)$$ | Height $$f(x_1, x_2)$$ |
| :--- | :--- | :--- |
| Global optimum | $$(-0.009,\ 1.581)$$ | 8.11 |
| Local optimum 1 | $$(-0.460,\ -0.629)$$ | 3.78 |
| Local optimum 2 | $$(1.286,\ -0.005)$$ | 3.59 |

Following the book's idea of running the gradient method from different starting points, we try two of them on the Peaks function (computed with the script at the end of this post). From $$(-1, 1)$$, the search reaches the highest peak. From $$(0, 0)$$, the search stops at a local peak, less than half as high as the global one. Same algorithm, same function, only the starting point differs. This is the signature of a multimodal problem: **the result of a local method depends on where it starts.**

---

### Where Multimodality Appears in Industrial Engineering

Multimodal problems are not only mathematical test functions. The reference book notes that the **EOQ** (*Economic Order Quantity*) model from Day #2 becomes multimodal when suppliers offer **volume discounts**. The total cost curve is no longer a smooth curve with a single valley. It breaks at every order quantity where a new price applies, so several valleys appear. A gradient method that starts near one valley can stop there and miss an order quantity that is actually cheaper.

Another common case is combinatorial problems such as production scheduling or arranging parts on a machine. Swapping the order of two jobs can raise or lower the cost irregularly, so the landscape is full of small hills.

---

### Dimensionality Makes It Harder

Besides the number of peaks, the reference book also highlights **dimensionality**, the number of independent decision variables. John's EOQ problem has a single variable (the order quantity $$Q$$), while the Peaks function has two. When one supplier cannot meet all the demand and the order must be split among several suppliers, the number of variables grows. The more dimensions, the larger the search space to explore, a phenomenon known as the *curse of dimensionality*. A problem that is both multimodal and high-dimensional is the hardest kind for classical methods.

---

### So Which Method Fits?

| Problem Type | Reasonable Method | Note |
| :--- | :--- | :--- |
| Unimodal | Gradient methods (*gradient descent/ascent*) | Fast and reliable; the starting point matters little. |
| Multimodal, low-dimensional | Gradient methods from many starting points (*multi-start*) | Helps, but does not guarantee the global optimum. |
| Multimodal, high-dimensional | Metaheuristics: *Simulated Annealing*, *Particle Swarm Optimization*, evolutionary algorithms | No optimality guarantee, but far less likely to get stuck on a local peak. |

The reference book shows that probability-based methods, such as *random search* and *Particle Swarm Optimization*, find the highest peak of the Peaks function regardless of the starting point. These methods will be covered one by one later in the series.

Before choosing an algorithm, start with a simple question: is the landscape of this problem likely to have one peak, or many? The answer often settles half of the work.

---

### Python Script

The peaks table in this post can be reproduced with the Python script below. It also runs a plain gradient ascent from several starting points and draws the result on a contour map. It needs Python 3.9+ with `numpy` and `matplotlib`. The script carries the author's copyright notice (© 2026 Galih Prakoso, MIT License), which must be kept in any copy or modification.

<div class="code-view" data-src="{{ '/assets/code/day-5-peaks.py' | relative_url }}"><a href="{{ '/assets/code/day-5-peaks.py' | relative_url }}">day-5-peaks.py</a></div>

---

### Reference

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 2, Section 2.8: Modality and Dimensionality, pp. 39–41; Chapter 3, Section 3.4: Maximizing the Peaks Function, pp. 55–62). Springer Nature.

