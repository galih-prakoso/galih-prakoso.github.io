---
layout: post
lang: en
title: "Why Straight Lines and Curves Change How Problems Are Solved: Linear vs. Non-Linear Optimization"
date: 2026-11-21 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #4: how does a straight line versus a curve change the way we solve a problem?"
og_image: /assets/img/blog/optimization-day-4-en.png
permalink: /blog/2026/linear-vs-non-linear-optimization/
tags: optimization linear-programming non-linear-programming industrial-engineering algorithms
categories: optimization-series
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=14">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="en" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/share-buttons.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/code-view.js' | relative_url }}?v=1" defer></script>

*Series: Optimization in Industrial Engineering, Day #4. Topic: Linear vs. Non-Linear Optimization* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/optimasi-linear-vs-non-linear/' | relative_url }})

The previous post covered how decision variables, an objective function, and constraints form the basic structure of an optimization problem. When we step further into real-world applications, the next crucial question arises: **what is the shape of the relationship among the variables?** Is it a straight line (linear) or a curve (non-linear)?

The difference resembles a straight highway versus a winding mountain road. On the highway, once the speed is known, the travel time can be calculated exactly, and every extra kilometre adds the same amount of time. On the mountain road, climbs, bends and descents break that proportion, and a stretch that is going downhill does not necessarily lead to the lowest point of the valley.

This simple distinction fundamentally changes the mathematical difficulty, the type of algorithm required, and the guarantee of finding the best solution.

---

### Linear Optimization (Linear Programming / LP)

An optimization problem is classified as **Linear Programming (LP)** when both its objective function and all of its constraints satisfy two key properties:

1. **Proportionality:** Any change in a decision variable causes a constant, proportional change in both the objective function and the constraints. For example, if producing 1 unit costs USD 10, producing 100 units will cost exactly USD 1,000.
2. **Additivity:** The total contribution of all variables is the direct sum of each variable's individual contribution, without multiplicative interactions.

#### Geometric Properties and LP Solutions

Geometrically, linear constraints enclose a **feasible region** that forms a convex polygon in two dimensions, or a convex polyhedron in higher dimensions. The boundaries of this region are crisp, straight lines.

The most notable property of linear optimization is that **the optimal solution always resides at one of the vertices (corner points) of the feasible region**. This neat geometric structure allows classical algorithms such as the *Simplex Method* or the *Interior Point Method* to find the global optimal solution deterministically and efficiently, even for problems involving millions of variables.

Consider, for example, a manufacturing plant producing two product lines, $$x_1$$ and $$x_2$$, with unit profits of USD 50 and USD 40 respectively. If machine capacity and raw material availability follow the linear constraints $$2x_1 + x_2 \le 100$$ and $$x_1 + 2x_2 \le 80$$, the objective function is written as:

$$\text{Maximize } Z = 50x_1 + 40x_2$$

Solving this problem means evaluating the corner points of the feasible region, which guarantees that the true best decision is found. Here, the corner points $$(0,0)$$, $$(50,0)$$, $$(40,20)$$, and $$(0,40)$$ give $$Z = 0$$, $$2{,}500$$, $$2{,}800$$, and $$1{,}600$$, so the optimum is to produce 40 units of $$x_1$$ and 20 units of $$x_2$$.

---

### Non-Linear Optimization (Non-Linear Programming / NLP)

Conversely, a problem is classified as **Non-Linear Programming (NLP)** if the objective function, or at least one constraint, contains a non-linear relationship. Non-linear behavior frequently stems from physical geometry, quadratic distance measures, exponential growth, logarithmic diminishing returns, or interactions between decision variables.

For example, when determining the location of a new facility, the Euclidean distance between the facility and each demand point is calculated using the square root formula $$\sqrt{(x_1 - a_i)^2 + (x_2 - b_i)^2}$$. The squared terms and the square root automatically turn the problem into a non-linear one.

#### The Local Optimum Trap in NLP

Replacing straight lines with curves drastically transforms the solution landscape. The feasible region of an NLP problem is no longer confined to flat-faced polygons. It can have curved boundaries, disconnected feasible islands, or wavy surfaces with multiple peaks and valleys.

This structural shift introduces the major challenge of non-linear optimization:

- **Local Optimum:** A point that outperforms all of its immediate neighbors, but is not the best score across the whole landscape.
- **Global Optimum:** The absolute best point across the entire feasible region.

Derivative-based algorithms (such as *Gradient Descent* or *Sequential Quadratic Programming*, SQP) can stop at a local optimum. In a minimization problem, *Gradient Descent* stops in a local valley because no nearby direction goes lower, even though a deeper valley exists elsewhere. In a maximization problem, the same trap appears as a local peak, as in Figure 1.

<img src="{{ '/assets/img/blog/optimization-day-4-en.svg' | relative_url }}" alt="Linear vs. non-linear optimization: a convex feasible region with its optimum at a vertex, versus a multi-peak landscape with local optima traps" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Figure 1. A linear feasible region forming a convex polygon (left) versus a non-linear multi-peak landscape with a local optimum trap (right).</em></p>

---

### Industrial Engineering Case Comparison

The table below shows how linear and non-linear assumptions differ across practical engineering contexts:

| Comparison Dimension | Linear Optimization (LP) | Non-Linear Optimization (NLP) |
| :--- | :--- | :--- |
| **Mathematical Form** | All functions $$f(x)$$ and $$g(x)$$ are first-degree ($$ax_1 + bx_2$$). | Involves $$x^2$$, $$\sqrt{x}$$, $$\log(x)$$, $$x_1 \cdot x_2$$, or exponentials. |
| **Feasible Region Shape** | Convex polygon or polyhedron with straight borders. | Curved boundaries, non-convex regions, or wavy surfaces. |
| **Optimal Solution Location** | Always at a vertex (corner point). | Can occur anywhere: in the interior, along a curved boundary, or at a crest. |
| **Solution Guarantee** | A global optimum is guaranteed. | High risk of getting trapped in a local optimum. |
| **IE Application Examples** | Production planning, blending models, workforce allocation. | Facility location (Euclidean distance), portfolio variance, chemical process control. |

---

### Bridging Models to Solution Methods

Distinguishing between LP and NLP dictates the algorithmic strategy of an industrial engineer:

1. If the formulation is strictly linear (LP), commercial solvers such as CPLEX, Gurobi, or GLPK can solve problems with millions of variables in seconds.
2. If the model is non-linear but convex, *Interior Point* or *SQP* algorithms can still reach the global optimum efficiently.
3. If the model is non-linear and non-convex (*multimodal*), metaheuristic approaches such as *Genetic Algorithms* (GA), *Particle Swarm Optimization* (PSO), or *Simulated Annealing* (SA) become essential for exploring the landscape and escaping local traps.
4. If the problem is so large or combinatorial (for example scheduling, routing, or nesting problems that are *NP-hard*) that exact methods cannot finish within a reasonable time, *heuristics* are used. They do not guarantee the global optimum, but they quickly produce good feasible solutions, which is often the practical trade-off in real industrial settings.

Understanding the structural difference between LP and NLP is a foundational step before moving on to formulation techniques and algorithm selection in the upcoming posts.

---

### Python Script

The corner points, the optimum, and the feasible-region plot in this post can be reproduced with the Python script below. It finds the vertices by intersecting the constraint lines. It needs Python 3.9+ with `numpy` and `matplotlib`. The script carries the author's copyright notice (© 2026 Galih Prakoso, MIT License), which must be kept in any copy or modification.

<div class="code-view" data-src="{{ '/assets/code/day-4-linear-vertices.py' | relative_url }}"><a href="{{ '/assets/code/day-4-linear-vertices.py' | relative_url }}">day-4-linear-vertices.py</a></div>

---

### Reference

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.1: What and Where Do We Optimize, p. 3). Springer Nature.
