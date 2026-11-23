"""
Optimization in Industrial Engineering | Day 3: Anatomy of an optimization model: the catering example
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, matplotlib      Run:  python day-3-catering-model.py   [--idr] [--no-plot] [--save out.png]
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt

CREDIT = "(c) 2026 Galih Prakoso - MIT License - https://galih-prakoso.github.io/"


def print_table(headers, rows):
    """Print a simple aligned text table."""
    cells = [[str(c) for c in r] for r in rows]
    widths = [max(len(h), *(len(r[i]) for r in cells)) for i, h in enumerate(headers)]
    line = "  ".join(h.ljust(w) for h, w in zip(headers, widths))
    print(line)
    print("-" * len(line))
    for r in cells:
        print("  ".join(c.ljust(w) for c, w in zip(r, widths)))


def finish(fig, args):
    """Save and/or show the figure depending on the command-line options."""
    if args.save:
        fig.savefig(args.save, dpi=150, bbox_inches="tight")
        print("Plot saved to", args.save)
    if not args.no_plot and not args.save:
        plt.show()


def parse_args():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--no-plot", action="store_true", help="print the table only")
    ap.add_argument("--save", metavar="FILE", help="save the plot to FILE instead of showing it")
    ap.add_argument("--idr", action="store_true", help="use the rupiah figures of the Indonesian post")
    return ap.parse_args()

from itertools import combinations

# ---- The model from the post -------------------------------------------------
#   decision variables : x1 = Standard Boxes, x2 = Premium Boxes
#   objective          : maximize Z = 4 x1 + 7 x2                 (profit, USD)
#   constraints        : 6 x1 + 10 x2 <= 600                      (ingredient budget, USD)
#                        4 x1 + 12 x2 <= 480                      (kitchen time, minutes)
#                        x1, x2 >= 0
# The Indonesian post uses rupiah (run with --idr): profit 10,000 / 18,000 per box
# and ingredient cost 15,000 / 25,000 per box with a 1,500,000 budget.
PROFIT = np.array([4.0, 7.0])
LIMITS = [("Ingredient budget", np.array([6.0, 10.0]), 600.0),
          ("Kitchen time", np.array([4.0, 12.0]), 480.0)]
MONEY = "USD "


def use_rupiah():
    """Switch the model to the rupiah figures used in the Indonesian post."""
    global PROFIT, LIMITS, MONEY
    PROFIT = np.array([10000.0, 18000.0])
    LIMITS = [("Ingredient budget", np.array([15000.0, 25000.0]), 1500000.0),
              ("Kitchen time", np.array([4.0, 12.0]), 480.0)]
    MONEY = "Rp "


def constraint_matrix():
    A = [a for _, a, _ in LIMITS] + [np.array([-1.0, 0.0]), np.array([0.0, -1.0])]
    b = [r for _, _, r in LIMITS] + [0.0, 0.0]
    return np.array(A), np.array(b)


def vertices():
    A, b = constraint_matrix()
    pts = []
    for i, j in combinations(range(len(A)), 2):
        M = A[[i, j]]
        if abs(np.linalg.det(M)) < 1e-12:
            continue
        p = np.round(np.linalg.solve(M, b[[i, j]]), 9) + 0.0
        if np.all(A @ p <= b + 1e-9) and not any(np.allclose(p, q) for q in pts):
            pts.append(p)
    return pts


def plot(verts, best):
    x1 = np.linspace(0, 110, 400)
    fig, ax = plt.subplots(figsize=(7, 6))
    for name, a, r in LIMITS:
        ax.plot(x1, (r - a[0] * x1) / a[1], label=f"{name}: ${a[0]:,.0f}x_1 + {a[1]:,.0f}x_2 \\leq {r:,.0f}$".replace(",", "\\,"))
    poly = np.array(sorted(verts, key=lambda p: np.arctan2(p[1] - 15, p[0] - 15)))
    ax.fill(poly[:, 0], poly[:, 1], alpha=0.25, label="Feasible region")
    z = PROFIT @ best
    ax.plot(x1, (z - PROFIT[0] * x1) / PROFIT[1], "k--", lw=1, label=f"Best profit line Z = {MONEY}{z:,.0f}")
    ax.plot(*best, "o", ms=12, mfc="none", mec="green", mew=2)
    ax.set_xlim(0, 110); ax.set_ylim(0, 75)
    ax.set_xlabel("x1  (Standard Boxes)"); ax.set_ylabel("x2  (Premium Boxes)")
    ax.set_title("Feasible region of the catering model\n" + CREDIT, fontsize=8)
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    return fig


def main():
    args = parse_args()
    if args.idr:
        use_rupiah()
    print(CREDIT, "\n")
    verts = vertices()
    rows = [[f"({p[0] + 0.0:.0f}, {p[1] + 0.0:.0f})", f"{MONEY}{PROFIT @ p:,.0f}"] for p in verts]
    print_table(["Corner point (x1, x2)", "Daily profit Z"], rows)
    best = max(verts, key=lambda p: PROFIT @ p)
    print(f"\nOptimum: x1 = {best[0] + 0.0:.0f}, x2 = {best[1] + 0.0:.0f}, Z = {MONEY}{PROFIT @ best:,.0f}\n")
    print("Constraint check at the optimum:")
    for name, a, r in LIMITS:
        use = a @ best
        print(f"  {name:<18} uses {use:11,.0f} of {r:,.0f}  ->  {'binding' if abs(use - r) < 1e-9 else 'slack'}")
    if not args.no_plot or args.save:
        finish(plot(verts, best), args)


if __name__ == "__main__":
    main()
