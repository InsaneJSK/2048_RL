"""
Play N completely random games of 2048 and save the results to CSV.

Usage:
    python baseline_random.py --episodes 500 --out baseline.csv
"""

import argparse, csv
import numpy as np
from collections import Counter
from engine import Game2048

def run_random_game():
    g = Game2048()
    while not g.gameover:
        g.step(np.random.randint(0, 4))  # random move: 0–3
    return g.score, g.board.max()

def main(episodes: int, out_path: str):
    scores = []
    max_tiles = []

    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["episode", "score", "max_tile"])
        writer.writeheader()

        for ep in range(episodes):
            score, max_tile = run_random_game()
            scores.append(score)
            max_tiles.append(max_tile)

            writer.writerow({
                "episode": ep,
                "score": score,
                "max_tile": max_tile
            })

            if (ep + 1) % 50 == 0:
                print(f"[{ep+1}/{episodes}] score={score}, max_tile={max_tile}")

    print(f"Saved the results to {out_path}")
    print(f"Average Score: {np.mean(scores):.2f}")
    print(f"Most Common Max Tile: {Counter(max_tiles).most_common(1)[0][0]}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=100,
                    help="number of random games to play")
    ap.add_argument("--out", default="baseline.csv",
                    help="output CSV path")
    args = ap.parse_args()
    main(args.episodes, args.out)
