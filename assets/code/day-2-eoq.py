"""
Optimization in Industrial Engineering | Day 2: John's Problem and the EOQ model
=====================================================================
Companion script for the blog post series at https://galih-prakoso.github.io/

Copyright (c) 2026 Galih Prakoso <galih.prakoso3003@gmail.com>

MIT License. Permission is granted, free of charge, to use, copy, modify, merge,
publish and distribute this script, PROVIDED THAT the copyright notice above and
this permission notice are included in all copies or substantial portions of it.
THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Requires: Python 3.9+, numpy, matplotlib      Run:  python day-2-eoq.py   [--no-plot] [--save out.png]
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


# ---- Data from the post: John's store -------------------------------------
D = 1000   # annual demand (units / year)
S = 50     # ordering cost (USD / order)
H = 4      # holding cost (USD / unit / year)


def ordering_cost(Q):
    return D / Q * S


def holding_cost(Q):
    return Q / 2 * H


def total_cost(Q):
    return ordering_cost(Q) + holding_cost(Q)


def eoq():
    """Economic Order Quantity: Q* = sqrt(2DS/H)."""
    return float(np.sqrt(2 * D * S / H))


def comparison_table(order_sizes):
    rows = []
    for label, Q in order_sizes:
        rows.append([label, Q, f"{D / Q:.1f}", f"USD {ordering_cost(Q):,.0f}",
                     f"USD {holding_cost(Q):,.0f}", f"USD {total_cost(Q):,.0f}"])
    return rows


def plot(q_star):
    Q = np.linspace(20, 600, 500)
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(Q, ordering_cost(Q), "--", label="Ordering cost  D/Q * S")
    ax.plot(Q, holding_cost(Q), "--", label="Holding cost  Q/2 * H")
    ax.plot(Q, total_cost(Q), lw=2.5, label="Total cost  TC(Q)")
    ax.axvline(q_star, color="green", ls=":")
    ax.plot([q_star], [total_cost(q_star)], "o", color="green")
    ax.annotate(f"Q* = {q_star:.0f} units\nTC = USD {total_cost(q_star):,.0f}",
                (q_star, total_cost(q_star)), xytext=(q_star + 40, total_cost(q_star) + 350))
    ax.set_xlabel("Order quantity Q (units)")
    ax.set_ylabel("Annual cost (USD)")
    ax.set_ylim(0, 2000)
    ax.set_title("EOQ: the cost trade-off  (" + CREDIT + ")", fontsize=8)
    ax.legend()
    ax.grid(alpha=0.3)
    return fig


def main():
    args = parse_args()
    print(CREDIT, "\n")
    q_star = eoq()
    print(f"EOQ  Q* = sqrt(2*{D}*{S}/{H}) = {q_star:.2f}  ->  round to {round(q_star)} units\n")
    q_opt = round(q_star)
    rows = comparison_table([("Too small", 50), ("Optimal (EOQ)", q_opt), ("Too large", 500)])
    print_table(["Scenario", "Q", "Orders/yr", "Ordering", "Holding", "Total"], rows)
    saving = 1 - total_cost(q_opt) / total_cost(50)
    print(f"\nSaving versus ordering 50 or 500 units: {saving:.1%}")
    if not args.no_plot or args.save:
        finish(plot(q_star), args)


if __name__ == "__main__":
    main()
