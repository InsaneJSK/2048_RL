"""
charts.py
---------
Plot score and max-tile histograms for one (or many) CSV files
produced by baseline scripts (random, heuristic, RL, etc.).

Usage:
    python charts.py baseline.csv heuristic.csv ppo.csv
"""

import argparse, pathlib, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path

def plot_scores(datasets):
    plt.figure()
    for label, df in datasets:
        df["score"].plot.hist(
            bins=30, alpha=0.5, label=label, rwidth=0.9
        )
    plt.title("Final Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figs/score_hist.png")
    plt.close()

def plot_tiles(datasets):
    plt.figure()
    bins = [0, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    for label, df in datasets:
        df["max_tile"].plot.hist(
            bins=bins, alpha=0.5, label=label, rwidth=0.9
        )
    plt.title("Highest Tile Reached")
    plt.xlabel("Tile Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figs/tile_hist.png")
    plt.close()

def main(csv_paths):
    Path("figs").mkdir(exist_ok=True)

    datasets = []
    for csv_path in csv_paths:
        label = pathlib.Path(csv_path).stem  # filename without extension
        df = pd.read_csv(csv_path)
        datasets.append((label, df))

    plot_scores(datasets)
    plot_tiles(datasets)
    print("Charts saved to ./figs/")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Overlay histograms for multiple 2048‑agent CSVs"
    )
    ap.add_argument(
        "csvs",
        nargs="+",
        help="One or more CSV files produced by baseline or RL scripts",
    )
    args = ap.parse_args()
    main(args.csvs)
