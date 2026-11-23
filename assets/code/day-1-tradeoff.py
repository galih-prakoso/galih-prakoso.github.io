"""
Optimization in Industrial Engineering | Day 1: Trade-offs: what and where do we optimize?
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, matplotlib      Run:  python day-1-tradeoff.py   [--no-plot] [--save out.png]
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


# ILLUSTRATIVE numbers only (they are NOT from the reference book): they are chosen
# to show how the best engine size changes with the objective, as in the post.
MASS_KG = 1200.0


def accel_time(power_kw):
    """0-100 km/h time (s): more power -> shorter time. Illustrative model."""
    return 4.0 + 0.5 * MASS_KG / power_kw


def fuel_use(power_kw):
    """Fuel use (L/100 km): more power -> more fuel. Illustrative model."""
    return 4.0 + 0.045 * power_kw


def normalise(v):
    return (v - v.min()) / (v.max() - v.min())


def best_design(weight_on_acceleration, powers):
    """Decision variable: engine power. Objective: weighted, normalised cost to MINIMIZE."""
    t = normalise(accel_time(powers))
    f = normalise(fuel_use(powers))
    score = weight_on_acceleration * t + (1 - weight_on_acceleration) * f
    i = int(np.argmin(score))
    return powers[i], accel_time(powers[i]), fuel_use(powers[i])


def plot(powers, picks):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(accel_time(powers), fuel_use(powers), lw=2, label="All engine sizes (trade-off curve)")
    for w, p, t, f in picks:
        ax.plot([t], [f], "o")
        ax.annotate(f"w={w:.1f}  {p:.0f} kW", (t, f), xytext=(6, 6), textcoords="offset points", fontsize=8)
    ax.set_xlabel("0-100 km/h time (s)  - lower is better")
    ax.set_ylabel("Fuel use (L/100 km)  - lower is better")
    ax.set_title("You cannot win on both axes  (" + CREDIT + ")", fontsize=8)
    ax.grid(alpha=0.3)
    ax.legend()
    return fig


def main():
    args = parse_args()
    print(CREDIT, "\n")
    print("Illustrative trade-off: decision variable = engine power (kW)\n")
    powers = np.linspace(40, 300, 261)
    picks, rows = [], []
    for w in (0.1, 0.3, 0.5, 0.7, 0.9):
        p, t, f = best_design(w, powers)
        picks.append((w, p, t, f))
        rows.append([f"{w:.1f}", f"{p:.0f} kW", f"{t:.1f} s", f"{f:.1f} L/100km"])
    print_table(["Weight on acceleration", "Best power", "0-100 time", "Fuel use"], rows)
    print("\nThe 'best' design changes with what we choose to optimize.")
    if not args.no_plot or args.save:
        finish(plot(powers, picks), args)


if __name__ == "__main__":
    main()
