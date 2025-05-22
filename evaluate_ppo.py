"""
evaluate.py
-----------
Evaluate a trained PPO model on 2048 and save per-episode results to CSV.

Usage:
    python evaluate_ppo.py --model ppo_model.zip --episodes 20 --out ppo.csv
"""

import argparse
import numpy as np
import csv
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from game2048_env import Game2048Env
from tqdm import trange


def run_episode(model, env, max_moves=2000):
    obs, _ = env.reset()
    done = False
    moves = 0

    while not done and moves < max_moves:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        if info["moved"]:
            moves+=1
    total_reward = info["raw_score"]
    max_tile = env.unwrapped.raw_board.max()
    return total_reward, max_tile, moves, done


def main(model_path, episodes, out_path):
    env = Monitor(Game2048Env())
    model = PPO.load(model_path)

    scores, tiles, lengths, terminated_flags = [], [], [], []

    for _ in trange(episodes, desc="Evaluating episodes"):
        score, tile, moves, done = run_episode(model, env)
        scores.append(score)
        tiles.append(tile)
        lengths.append(moves)
        terminated_flags.append(int(done))

    # Save to CSV
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["score", "max_tile", "moves", "terminated"])
        writer.writerows(zip(scores, tiles, lengths, terminated_flags))

    print("\n===== Summary =====")
    print(f"Saved results to: {out_path}")
    print(f"Average score     : {np.mean(scores):.2f}")
    print(f"Score stdev       : {np.std(scores):.2f}")
    print(f"Average max tile  : {np.mean(tiles):.1f}")
    print(f"Best max tile     : {np.max(tiles)}")
    print(f"Average moves/ep  : {np.mean(lengths):.1f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="Path to .zip model")
    ap.add_argument("--episodes", type=int, default=20, help="How many episodes to run")
    ap.add_argument("--out", default="ppo_eval.csv", help="Path to output CSV")
    args = ap.parse_args()

    main(args.model, args.episodes, args.out)
