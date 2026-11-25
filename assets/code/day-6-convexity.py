"""
Optimization in Industrial Engineering | Day 6: Convex vs. non-convex: the chord test
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, matplotlib      Run:  python day-6-convexity.py   [--no-plot] [--save out.png]
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


# ---- Part A: the chord test on one-variable functions ------------------------
# A function f is convex on an interval if, for every pair of points a < b and every
# 0 <= t <= 1:   f(t*a + (1-t)*b) <= t*f(a) + (1-t)*f(b)
# i.e. the chord between two points of the graph never goes below the graph.
D, S, H = 1000.0, 50.0, 4.0          # annual demand, order cost, holding cost (Day 2)


def f_square(q):
    return (q - 300.0) ** 2 / 1000.0


def f_eoq(q):
    """Day 2 total cost without purchase price: ordering + holding."""
    return S * D / q + H * q / 2.0


def f_eoq_discount(q):
    """EOQ plus purchase cost with a volume discount (ILLUSTRATIVE prices, not from the book):
    USD 10 per unit below 400 units per order, USD 9.5 per unit from 400 units on."""
    q = np.asarray(q, dtype=float)
    price = np.where(q < 400.0, 10.0, 9.5)
    return price * D + S * D / q + H * q / 2.0


FUNCS = [("(Q - 300)^2 / 1000", f_square),
         ("EOQ cost (Day 2)", f_eoq),
         ("EOQ with volume discount", f_eoq_discount)]
LO, HI = 50.0, 800.0


def chord_violations(f, n_pairs=20000, seed=1):
    """Fraction of random chords that dip BELOW the graph (0 means 'looks convex')
    and the second difference minimum (negative means the curve bends downward somewhere)."""
    rng = np.random.default_rng(seed)
    a = rng.uniform(LO, HI, n_pairs)
    b = rng.uniform(LO, HI, n_pairs)
    t = rng.uniform(0.0, 1.0, n_pairs)
    mid = t * a + (1 - t) * b
    chord = t * f(a) + (1 - t) * f(b)
    bad = np.mean(f(mid) > chord + 1e-9)
    q = np.linspace(LO, HI, 3001)
    h = q[1] - q[0]
    d2 = np.diff(f(q), 2) / h ** 2
    return bad, d2.min()


# ---- Part B: Hillier & Lieberman's non-convex feasible region ----------------
#   maximize Z = 3 x1 + 5 x2
#   subject to  x1 <= 4,   2 x2 <= 14,   8 x1 - x1^2 + 14 x2 - x2^2 <= 49,   x1, x2 >= 0
def feasible(x1, x2):
    return (x1 >= -1e-9) & (x2 >= -1e-9) & (x1 <= 4 + 1e-9) & (2 * x2 <= 14 + 1e-9) \
        & (8 * x1 - x1 ** 2 + 14 * x2 - x2 ** 2 <= 49 + 1e-9)


def objective(x1, x2):
    return 3 * x1 + 5 * x2


def local_maxima(step=0.01, radius=0.3):
    """Grid search: a feasible grid point is a local maximum if no feasible grid point
    within `radius` has a larger Z. Returns a list of (x1, x2, Z)."""
    xs = np.arange(0.0, 4.0 + step / 2, step)
    ys = np.arange(0.0, 7.0 + step / 2, step)
    X, Y = np.meshgrid(xs, ys)
    F = feasible(X, Y)
    Z = np.where(F, objective(X, Y), -np.inf)
    k = int(round(radius / step))
    found = []
    idx = np.argwhere(F & (Z >= Z.max() - 20))
    for i, j in idx:
        i0, i1 = max(0, i - k), min(Z.shape[0], i + k + 1)
        j0, j1 = max(0, j - k), min(Z.shape[1], j + k + 1)
        if Z[i, j] >= Z[i0:i1, j0:j1].max() - 1e-12:
            found.append((X[i, j], Y[i, j], Z[i, j]))
    # keep one representative per cluster (distance > 1)
    reps = []
    for p in sorted(found, key=lambda r: -r[2]):
        if all(np.hypot(p[0] - r[0], p[1] - r[1]) > 1.0 for r in reps):
            reps.append(p)
    return reps


def plot(maxima):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.8))
    q = np.linspace(LO, HI, 800)
    for name, f in FUNCS:
        y = f(q)
        ax[0].plot(q, (y - y.min()) / (y.max() - y.min()), label=name)
    a, b = 120.0, 700.0
    for name, f in FUNCS:
        y = f(q)
        lo, hi = y.min(), y.max()
        ax[0].plot([a, b], [(f(a) - lo) / (hi - lo), (f(b) - lo) / (hi - lo)], "k:", lw=0.8)
    ax[0].set_xlabel("order quantity Q")
    ax[0].set_ylabel("cost (rescaled to [0, 1])")
    ax[0].set_title("Chord test (dotted chords between Q=120 and Q=700)")
    ax[0].legend(fontsize=8)

    xs = np.linspace(0, 4.2, 500)
    ys = np.linspace(0, 7.4, 500)
    X, Y = np.meshgrid(xs, ys)
    ax[1].contourf(X, Y, feasible(X, Y).astype(float), levels=[0.5, 1.5], colors=["#bfdbfe"])
    ax[1].contour(X, Y, 8 * X - X ** 2 + 14 * Y - Y ** 2, levels=[49], colors="#1e3a8a")
    ax[1].plot([0, 4], [7, 3], "r--", lw=1.2, label="segment (0,7)-(4,3) leaves the region")
    for x1, x2, z in maxima:
        ax[1].plot(x1, x2, "o", ms=8)
        ax[1].annotate("(%.0f, %.0f) Z=%.0f" % (x1, x2, z), (x1, x2), textcoords="offset points", xytext=(8, 6))
    ax[1].set_xlabel("x1")
    ax[1].set_ylabel("x2")
    ax[1].set_title("Hillier & Lieberman: non-convex feasible region")
    ax[1].legend(fontsize=8, loc="lower left")
    fig.suptitle("Day 6: convex vs. non-convex\n" + CREDIT, fontsize=10)
    fig.tight_layout()
    return fig


def main():
    args = parse_args()
    print("Part A: chord test on [%g, %g] (fraction of chords below the graph; min second difference)" % (LO, HI))
    rows = []
    for name, f in FUNCS:
        bad, d2 = chord_violations(f)
        rows.append((name, "%.4f" % bad, "%.2e" % d2, "convex" if bad == 0 and d2 >= -1e-9 else "NOT convex"))
    print_table(["Function", "Bad chords", "min f''", "Verdict"], rows)

    print("\nPart B: Hillier & Lieberman example, max Z = 3 x1 + 5 x2")
    mid = (2.0, 5.0)
    print("Midpoint of (0, 7) and (4, 3) is", mid, "-> feasible?", bool(feasible(*mid)),
          "(constraint value %.0f > 49)" % (8 * 2 - 4 + 14 * 5 - 25))
    maxima = local_maxima()
    print_table(["x1", "x2", "Z", "Status"],
                [("%.2f" % x1, "%.2f" % x2, "%.0f" % z, "global maximum" if i == 0 else "local maximum only")
                 for i, (x1, x2, z) in enumerate(maxima)])
    print("\n" + CREDIT)
    if args.no_plot and not args.save:
        return
    finish(plot(maxima), args)


if __name__ == "__main__":
    main()
