"""
Optimization in Industrial Engineering | Day 4: Linear vs. non-linear: vertices of the feasible region
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, matplotlib      Run:  python day-4-linear-vertices.py   [--no-plot] [--save out.png]
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
    return ap.parse_args()

from itertools import combinations

# ---- Linear program from the post -------------------------------------------
#   maximize  Z = 50 x1 + 40 x2      (profit per unit, USD)
#   subject to 2 x1 +   x2 <= 100    (machine capacity)
#                x1 + 2 x2 <=  80    (raw material)
#                x1, x2 >= 0
C_OBJ = np.array([50.0, 40.0])
A = np.array([[2.0, 1.0], [1.0, 2.0], [-1.0, 0.0], [0.0, -1.0]])   # last two rows: x >= 0
B = np.array([100.0, 80.0, 0.0, 0.0])


def feasible(p, tol=1e-9):
    return bool(np.all(A @ p <= B + tol))


def vertices():
    """Intersect every pair of constraint lines; keep the feasible intersections."""
    pts = []
    for i, j in combinations(range(len(A)), 2):
        M = A[[i, j]]
        if abs(np.linalg.det(M)) < 1e-12:
            continue                      # parallel lines never meet
        p = np.round(np.linalg.solve(M, B[[i, j]]), 9) + 0.0
        if feasible(p) and not any(np.allclose(p, q) for q in pts):
            pts.append(p)
    return pts


def plot(verts, best):
    x1 = np.linspace(0, 60, 400)
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot(x1, 100 - 2 * x1, label="2x1 + x2 = 100")
    ax.plot(x1, (80 - x1) / 2, label="x1 + 2x2 = 80")
    poly = np.array(sorted(verts, key=lambda p: np.arctan2(p[1] - 20, p[0] - 20)))
    ax.fill(poly[:, 0], poly[:, 1], alpha=0.25, label="Feasible region")
    z_star = C_OBJ @ best
    for z, style in ((0.55 * z_star, ":"), (0.8 * z_star, ":"), (z_star, "--")):
        ax.plot(x1, (z - C_OBJ[0] * x1) / C_OBJ[1], "k" + style, lw=1)
    for p in verts:
        ax.plot(*p, "ko")
        ax.annotate(f"({p[0] + 0.0:.0f}, {p[1] + 0.0:.0f})  Z={C_OBJ @ p:,.0f}", p, xytext=(5, 6), textcoords="offset points", fontsize=8)
    ax.plot(*best, "o", ms=12, mfc="none", mec="green", mew=2)
    ax.set_xlim(0, 60); ax.set_ylim(0, 60)
    ax.set_xlabel("x1"); ax.set_ylabel("x2")
    ax.set_title("The optimum sits at a vertex  (" + CREDIT + ")", fontsize=8)
    ax.legend(loc="upper right"); ax.grid(alpha=0.3)
    return fig


def main():
    args = parse_args()
    print(CREDIT, "\n")
    verts = vertices()
    rows = [[f"({p[0] + 0.0:.0f}, {p[1] + 0.0:.0f})", f"{C_OBJ @ p:,.0f}"] for p in verts]
    print_table(["Corner point (x1, x2)", "Z = 50 x1 + 40 x2"], rows)
    best = max(verts, key=lambda p: C_OBJ @ p)
    print(f"\nOptimum: x1 = {best[0] + 0.0:.0f}, x2 = {best[1] + 0.0:.0f}, Z = {C_OBJ @ best:,.0f}")
    if not args.no_plot or args.save:
        finish(plot(verts, best), args)


if __name__ == "__main__":
    main()
