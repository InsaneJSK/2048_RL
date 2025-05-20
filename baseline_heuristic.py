"""
Play N games of 2048 using a simple heuristic agent and save the results to CSV.

Usage:
    python baseline_heuristic.py --episodes 500 --out heuristic.csv
"""

import argparse, csv
import numpy as np
from collections import Counter
from engine import Game2048

# Action constants
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
MOVE_ORDER = [LEFT, UP, RIGHT, DOWN]

class HeuristicAgent:
    def select_action(self, game: Game2048) -> int:
        for action in MOVE_ORDER:
            test_game = Game2048()
            test_game.board = game.board.copy()
            test_game.score = game.score
            test_game.step(action)
            if not np.array_equal(test_game.board, game.board):
                return action
        return 0

def run_heuristic_game():
    game = Game2048()
    agent = HeuristicAgent()

    while not game.gameover:
        action = agent.select_action(game)
        game.step(action)

    return game.score, int(game.board.max())

def main(episodes: int, out_path: str):
    scores = []
    max_tiles = []

    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["episode", "score", "max_tile"])
        writer.writeheader()

        for ep in range(episodes):
            score, max_tile = run_heuristic_game()
            scores.append(score)
            max_tiles.append(max_tile)

            writer.writerow({
                "episode": ep,
                "score": score,
                "max_tile": max_tile
            })

            if (ep + 1) % 50 == 0:
                print(f"[{ep+1}/{episodes}] score={score}, max_tile={max_tile}")

    print(f"\nSaved the results to {out_path}")
    print(f"Average Score: {np.mean(scores):.2f}")
    print(f"Most Common Max Tile: {Counter(max_tiles).most_common(1)[0][0]}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=100,
                    help="number of games to play using the heuristic agent")
    ap.add_argument("--out", default="heuristic.csv",
                    help="output CSV file path")
    args = ap.parse_args()
    main(args.episodes, args.out)
