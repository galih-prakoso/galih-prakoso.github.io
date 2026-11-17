---
layout: post
lang: en
title: "John's Problem and the Art of Balancing Inventory: An Introduction to the EOQ Model"
date: 2026-11-17 12:00:00 +0300
description: "Optimization in Industrial Engineering, Day #2: how do we decide the most economical order quantity?"
permalink: /blog/2026/johns-problem-eoq-inventory/
tags: optimization eoq inventory-management industrial-engineering supply-chain
categories: optimization-series
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=2">

*Series: Optimization in Industrial Engineering, Day #2. Topic 1.2: John's Problem, Introduction to the EOQ* · [Baca dalam Bahasa Indonesia]({{ '/id/tulisan/2026/masalah-john-model-eoq/' | relative_url }})

<img src="{{ '/assets/img/blog/optimization-day-2-en.svg' | relative_url }}" alt="Illustration of the sawtooth inventory cycle and the EOQ cost trade-off curve" style="max-width: 100%; height: auto; display: block; margin: 1rem auto;">

In our previous discussion, we saw how optimization principles are already woven into our everyday decisions. Today, we will take one step further into one of the most foundational problems in Industrial Engineering and supply chain management: inventory control.

To understand this concept gently and intuitively, let us look at a classic scenario often introduced in textbooks as **John's Problem**.

Imagine John manages a retail store that sells an everyday consumer product. Based on sales records from previous years, John knows that customer demand for this product is steady and predictable throughout the year. On the surface, John's task seems straightforward: he simply needs to order stock from his supplier so that items are always available whenever customers walk in to buy.

However, as soon as John begins tracking his operational expenses, a dilemma emerges that frequently challenges business managers: **how many units should John order each time he places an order with his supplier?**

### Two Extreme Choices That Both Hurt the Bottom Line

If we put ourselves in John's shoes, two extreme strategies immediately come to mind:

- **Option One: Ordering small quantities very frequently.** With this approach, John's warehouse never holds too much stock at once. Storage space stays open, very little cash is tied up in unsold goods, and the risk of damage or obsolescence remains low. Yet, a drawback appears on the other side: every time John places an order, he incurs fixed administrative and shipping (transportation) fees. Ordering too frequently causes total annual shipping costs to skyrocket.
- **Option Two: Ordering massive quantities very rarely.** By ordering six months' or a full year's worth of inventory in a single shipment, John significantly reduces his annual transportation expenses. In return, however, he now needs a much larger storage facility, pays higher electricity, maintenance, and insurance bills, and leaves a substantial amount of capital sitting idle in the warehouse.

Here we encounter the exact essence of optimization discussed on day one. Ordering too little drives up **ordering costs**, whereas ordering too much inflates **holding costs**. Our goal is to find the balanced middle ground where the **total combined cost** reaches its lowest possible point.

### Introducing the Economic Order Quantity (EOQ) Model

In Industrial Engineering, the mathematical approach designed to resolve John's dilemma is known as the **EOQ (Economic Order Quantity)** model. First introduced by Ford W. Harris in 1913, this classical model remains a cornerstone of inventory management today because of its remarkable simplicity and intuition.

To build this model without getting bogged down in heavy calculus derivations, we only need to familiarize ourselves with four basic symbols:

1. **$$D$$ (Annual Demand):** The total number of units required by customers over an entire year.
2. **$$S$$ (Ordering / Setup Cost):** The fixed cost incurred every time we place and receive an order, regardless of the shipment size.
3. **$$H$$ (Holding Cost):** The cost to store one unit of inventory in the warehouse for one full year (covering space, utilities, insurance, and capital cost).
4. **$$Q$$ (Order Quantity):** The number of units we decide to order each time we replenish stock. This $$Q$$ is our **decision variable**.

If we observe how inventory levels in John's warehouse behave over time, they follow a distinct **sawtooth pattern**. The moment a shipment arrives, stock jumps to its peak level of $$Q$$. As customers purchase the product steadily over time, inventory drops linearly until it reaches $$0$$, right when the next delivery arrives. Because stock moves smoothly from $$Q$$ down to $$0$$, the average inventory sitting in the warehouse at any given time is simply half the order size, written as $$\frac{Q}{2}$$.

Following this logic, the annual inventory cost affected by our decision consists of two competing components:

- **Annual Ordering Cost:** Found by multiplying the number of orders placed per year ($$\frac{D}{Q}$$) by the fixed cost per order ($$S$$), giving $$\frac{D}{Q} \cdot S$$. As $$Q$$ increases, this cost **decreases**.
- **Annual Holding Cost:** Found by multiplying the average inventory level ($$\frac{Q}{2}$$) by the annual storage cost per unit ($$H$$), giving $$\frac{Q}{2} \cdot H$$. As $$Q$$ increases, this cost **increases**.

When we combine both cost curves into a single total cost objective function, $$TC(Q) = \frac{D}{Q}S + \frac{Q}{2}H$$, the resulting graph forms a smooth **U-shaped curve**. Interestingly, the very bottom of this U-curve occurs at the exact point where **annual ordering cost equals annual holding cost**. Mathematically, the optimal order quantity ($$Q^*$$) is given by the clean formula:

$$Q^* = \sqrt{\frac{2DS}{H}}$$

### A Simple Numerical Walkthrough for John's Store

To see how this works in practice, let us plug concrete numbers into John's store operations:

- Annual demand ($$D$$) = 1,000 units per year.
- Fixed ordering and shipping cost ($$S$$) = USD 50 per order.
- Annual holding cost ($$H$$) = USD 4 per unit per year.

Applying the EOQ formula above, we can directly determine the most economical order size for John:

$$Q^* = \sqrt{\frac{2 \times 1000 \times 50}{4}} = \sqrt{\frac{100000}{4}} = \sqrt{25000} \approx 158 \text{ units}$$

Let us compare how much John saves by following this optimal decision versus guessing his order quantities:

| Decision Scenario | Order Size (Q) | Orders per Year | Annual Ordering Cost | Annual Holding Cost | **Total Variable Cost** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Too small (frequent orders) | 50 units | 20 orders | USD 1,000 | USD 100 | **USD 1,100** |
| **Optimal (EOQ Model)** | **158 units** | **≈ 6.3 orders** | **USD 316** | **USD 316** | **USD 632** |
| Too large (rare orders) | 500 units | 2 orders | USD 100 | USD 1,000 | **USD 1,100** |

The comparison table reveals a striking insight. Whether John orders too little (50 units) or too much (500 units), he ends up spending USD 1,100 per year on logistics and storage. By ordering around 158 units per shipment, however, his total cost drops to USD 632 per year, a savings of more than 40% achieved purely by finding the right ordering rhythm.

### Bridging Classical Theory to Real-World Complexity

Through John's Problem, we see our optimization framework in action: we define a **decision variable** ($$Q$$) and an **objective function** ($$TC(Q)$$) to minimize total operational costs.

Of course, in real-world industrial settings, John's situation can quickly grow more intricate. What happens if the supplier offers **volume discounts** when John purchases larger batches? Or what if John's warehouse has a strict **storage capacity constraint** that cannot be exceeded?

Once these real-world complexities enter the picture, a single closed-form algebraic formula like the basic EOQ is no longer enough to solve the problem directly. That is precisely where numerical search techniques and modern optimization algorithms come into play, topics we will gradually explore in the upcoming posts of this series.

---

### Reference

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.2: John's Problem, Introduction to the EOQ, pp. 3–7). Springer Nature.
