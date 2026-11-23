"""
Optimization in Industrial Engineering | Day 5: Unimodal vs. multimodal: the Peaks function
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, matplotlib      Run:  python day-5-peaks.py   [--no-plot] [--save out.png]
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


def peaks(x, y):
    """MATLAB's classic 'Peaks' test function (maximization)."""
    return (3 * (1 - x) ** 2 * np.exp(-x ** 2 - (y + 1) ** 2)
            - 10 * (x / 5 - x ** 3 - y ** 5) * np.exp(-x ** 2 - y ** 2)
            - np.exp(-(x + 1) ** 2 - y ** 2) / 3)


def gradient(p, h=1e-6):
    """Central-difference gradient of peaks at point p = (x, y)."""
    x, y = p
    return np.array([(peaks(x + h, y) - peaks(x - h, y)) / (2 * h),
                     (peaks(x, y + h) - peaks(x, y - h)) / (2 * h)])


def gradient_ascent(start, step=0.01, max_iter=20000, tol=1e-7):
    """Plain gradient ascent with a fixed step. Returns the whole path."""
    p = np.array(start, dtype=float)
    path = [p.copy()]
    for _ in range(max_iter):
        g = gradient(p)
        if np.linalg.norm(g) < tol:
            break
        p = p + step * g
        path.append(p.copy())
    return np.array(path)


def find_peaks(lo=-3.0, hi=3.0, n=601, min_height=0.5):
    """Locate local maxima on a grid (the Peaks function has three in [-3, 3]^2)."""
    g = np.linspace(lo, hi, n)
    X, Y = np.meshgrid(g, g)
    Z = peaks(X, Y)
    found = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if Z[i, j] > min_height and Z[i, j] >= Z[i - 1:i + 2, j - 1:j + 2].max():
                found.append((X[i, j], Y[i, j], Z[i, j]))
    refined = []
    for x, y, _ in found:                      # polish each grid maximum with gradient ascent
        end = gradient_ascent((x, y), step=0.005)[-1]
        refined.append((end[0], end[1], float(peaks(*end))))
    return sorted(refined, key=lambda t: -t[2])


def which_peak(p, known):
    d = [np.hypot(p[0] - k[0], p[1] - k[1]) for k in known]
    return int(np.argmin(d))


def plot(known, runs):
    g = np.linspace(-3, 3, 300)
    X, Y = np.meshgrid(g, g)
    fig, ax = plt.subplots(figsize=(7.5, 6.5))
    cs = ax.contourf(X, Y, peaks(X, Y), levels=25, cmap="viridis", alpha=0.85)
    fig.colorbar(cs, ax=ax, label="f(x1, x2)")
    for k, (x, y, z) in enumerate(known):
        ax.plot(x, y, "w*", ms=14)
        ax.annotate("global" if k == 0 else f"local {k}", (x, y), xytext=(6, 6), textcoords="offset points", color="w")
    for label, path in runs:
        ax.plot(path[:, 0], path[:, 1], "-", lw=1.8, color="orange")
        ax.plot(*path[0], "o", color="red")
        ax.annotate(label, path[0], xytext=(5, -12), textcoords="offset points", color="w", fontsize=8)
    ax.set_xlabel("x1"); ax.set_ylabel("x2")
    ax.set_title("Same method, different start, different peak  (" + CREDIT + ")", fontsize=8)
    return fig


def main():
    args = parse_args()
    print(CREDIT, "\n")
    known = find_peaks()
    rows = [["global" if k == 0 else f"local {k}", f"({x:.3f}, {y:.3f})", f"{z:.2f}"]
            for k, (x, y, z) in enumerate(known)]
    print("Peaks of the function on [-3, 3] x [-3, 3]:\n")
    print_table(["Peak", "Location (x1, x2)", "Height f"], rows)

    starts = [(-1, 1), (0, 0), (1, -1), (-1, -2), (-0.5, -1)]
    runs, rows = [], []
    for s in starts:
        path = gradient_ascent(s)
        end = path[-1]
        k = which_peak(end, known)
        runs.append((f"start {s}", path))
        rows.append([str(s), f"({end[0]:.3f}, {end[1]:.3f})", f"{peaks(*end):.2f}", "global" if k == 0 else f"local {k}"])
    print("\nGradient ascent (fixed step 0.01) from different starting points:\n")
    print_table(["Start", "Ends at", "Height", "Peak reached"], rows)
    print("\nThe outcome depends on where the search starts: the mark of a multimodal problem.")
    if not args.no_plot or args.save:
        finish(plot(known, runs), args)


if __name__ == "__main__":
    main()
