"""
Create histograms from a baseline CSV produced by baseline_random.py.

Usage:
    python charts.py baseline.csv
Output:
    figs/score_hist.png
    figs/tile_hist.png
"""

import argparse, pathlib
import pandas as pd
import matplotlib.pyplot as plt

def main(csv_path: str):
    df = pd.read_csv(csv_path)
    pathlib.Path("figs").mkdir(exist_ok=True)

    # Histogram of final scores
    plt.figure()
    df["score"].plot.hist(bins=30, rwidth=0.9)
    plt.title("Random Play Final Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("figs/score_hist.png")
    plt.close()

    # Histogram of max tile reached
    plt.figure()
    df["max_tile"].plot.hist(
        bins=[0, 32, 64, 128, 256, 512, 1024, 2048, 4096],
        rwidth=0.9
    )
    plt.title("Random‑Play Max Tile Reached")
    plt.xlabel("Tile Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("figs/tile_hist.png")
    plt.close()

    print("Charts saved in ./figs/")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", help="CSV produced by baseline_random.py")
    args = ap.parse_args()
    main(args.csv)
