"""
Optimization in Industrial Engineering | Day 7: Integer programming: why rounding fails
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, scipy, matplotlib
Run:  python day-7-integer-programming.py   [--no-plot] [--save out.png]

Illustrative numbers (not from a book). Workshop problem:
    maximize  Z = 5*x1 + 8*x2
    s.t.      x1 +   x2 <= 6      (workers available)
              5*x1 + 9*x2 <= 45  (wood boards available)
              x1, x2 >= 0 and INTEGER
"""

import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

CREDIT = "(c) 2026 Galih Prakoso - MIT License - https://galih-prakoso.github.io/"
C = np.array([5.0, 8.0])
A = np.array([[1.0, 1.0], [5.0, 9.0]])
B = np.array([6.0, 45.0])


def print_table(headers, rows):
    """Print a simple aligned text table."""
    cells = [[str(c) for c in r] for r in rows]
    widths = [max(len(h), *(len(r[i]) for r in cells)) for i, h in enumerate(headers)]
    line = "  ".join(h.ljust(w) for h, w in zip(headers, widths))
    print(line)
    print("-" * len(line))
    for r in cells:
        print("  ".join(c.ljust(w) for c, w in zip(r, widths)))


def solve_lp(bounds):
    """Solve the LP relaxation with the given (lower, upper) bounds on x1, x2."""
    res = linprog(-C, A_ub=A, b_ub=B, bounds=bounds, method="highs")
    if res.status != 0:
        return None
    return res.x, -res.fun


def feasible(x1, x2):
    return x1 >= 0 and x2 >= 0 and np.all(A @ np.array([x1, x2]) <= B + 1e-9)


def enumerate_integer_points():
    """Brute force: every integer feasible point and its objective value."""
    pts = [(i, j, int(C @ [i, j])) for i in range(0, 10) for j in range(0, 10) if feasible(i, j)]
    return sorted(pts, key=lambda p: -p[2])


def branch_and_bound():
    """Depth-first branch and bound. Returns the log of nodes and the best solution."""
    log, best = [], (None, -math.inf)
    stack = [("root", [(0, None), (0, None)])]
    n = 0
    while stack:
        name, bounds = stack.pop()
        n += 1
        sol = solve_lp(bounds)
        if sol is None:
            log.append((n, name, "-", "-", "infeasible"))
            continue
        x, z = sol
        if z <= best[1] + 1e-9:
            log.append((n, name, f"({x[0]:.3f}, {x[1]:.3f})", f"{z:.3f}", "pruned (bound <= best)"))
            continue
        frac = [k for k in range(2) if abs(x[k] - round(x[k])) > 1e-6]
        if not frac:
            best = (np.round(x).astype(int), z)
            log.append((n, name, f"({int(round(x[0]))}, {int(round(x[1]))})", f"{z:.3f}", "integer -> new best"))
            continue
        k = frac[0]
        log.append((n, name, f"({x[0]:.3f}, {x[1]:.3f})", f"{z:.3f}", f"branch on x{k+1}"))
        lo, hi = bounds[k]
        down, up = list(bounds), list(bounds)
        down[k] = (lo, math.floor(x[k]))
        up[k] = (math.ceil(x[k]), hi)
        stack.append((f"{name} / x{k+1}>={math.ceil(x[k])}", up))
        stack.append((f"{name} / x{k+1}<={math.floor(x[k])}", down))
    return log, best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-plot", action="store_true")
    ap.add_argument("--save", default=None)
    args = ap.parse_args()
    print(CREDIT)

    x_lp, z_lp = solve_lp([(0, None), (0, None)])
    print(f"\nLP relaxation: x = ({x_lp[0]:.3f}, {x_lp[1]:.3f}), Z = {z_lp:.3f}")

    print("\nRounding the LP answer:")
    rows = []
    for name, p in [("round to nearest", (round(x_lp[0]), round(x_lp[1]))),
                    ("round down", (math.floor(x_lp[0]), math.floor(x_lp[1])))]:
        ok = feasible(*p)
        rows.append((name, p, "feasible" if ok else "INFEASIBLE", int(C @ p) if ok else "-"))
    print_table(["rule", "point", "status", "Z"], rows)

    pts = enumerate_integer_points()
    print(f"\nTrue integer optimum (brute force over {len(pts)} feasible integer points):")
    print_table(["x1", "x2", "Z"], pts[:5])
    gap = z_lp - pts[0][2]
    print(f"LP bound {z_lp:.3f} - integer optimum {pts[0][2]} = {gap:.3f}")

    print("\nBranch and bound:")
    log, best = branch_and_bound()
    print_table(["node", "branch", "LP solution", "Z", "decision"], log)
    print(f"Best integer solution: x = ({int(best[0][0])}, {int(best[0][1])}), Z = {best[1]:.0f}")

    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    xs = np.linspace(0, 9, 200)
    ax.fill_between(xs, 0, np.minimum(np.minimum(6 - xs, (45 - 5 * xs) / 9), 9).clip(min=0), alpha=0.15, color="tab:blue")
    ax.plot(xs, 6 - xs, color="tab:blue", label="$x_1 + x_2 = 6$")
    ax.plot(xs, (45 - 5 * xs) / 9, color="tab:orange", label="$5x_1 + 9x_2 = 45$")
    gx, gy = np.meshgrid(range(0, 10), range(0, 10))
    ok = np.array([[feasible(i, j) for i in range(10)] for j in range(10)])
    ax.scatter(gx[ok], gy[ok], s=28, color="gray", label="integer points", clip_on=False, zorder=4)
    ax.scatter(*x_lp, color="red", s=70, zorder=5, label=f"LP optimum ({x_lp[0]:.2f}, {x_lp[1]:.2f})")
    ax.scatter(*best[0], color="green", s=90, marker="*", zorder=6, label=f"IP optimum {tuple(int(v) for v in best[0])}")
    ax.set_xlim(-0.3, 7)
    ax.set_ylim(-0.3, 7)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.legend(fontsize=8)
    ax.set_title("Integer feasible points vs. LP optimum")
    ax.text(0.99, 0.01, CREDIT, transform=ax.transAxes, ha="right", fontsize=6, color="gray")
    if args.save:
        fig.savefig(args.save, dpi=150, bbox_inches="tight")
        print("Plot saved to", args.save)
    if not args.no_plot and not args.save:
        plt.show()


if __name__ == "__main__":
    main()
