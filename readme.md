# 2048‑RL Playground

This is a simple project for experimenting with **reinforcement learning on the game 2048**.  
So far, it includes:

- `engine.py`: Core 2048 game logic (board movement, scoring, game state)
- `baseline_random.py`: Runs completely random games to get a performance baseline
- `charts.py`: Creates visualizations from baseline scores
- `requirements.txt`: All Python dependencies (lightweight for now)

---

## 🚀 Getting Started

- **Clone the repo**  

```bash
git clone https://github.com/your-username/2048-rl-playground.git
cd 2048-rl-playground
```

- **Set up environment** (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

- **Run a quick test**

```bash
python baseline_random.py --episodes 100 --out baseline.csv
python charts.py baseline.csv
```

## 🎮 engine.py – The Game Engine

A pure Python 2048 implementation with no GUI.
You can control the game using .step(direction) and inspect .board, .score, and .gameover.

Example usage: given in **try_it.py**

## 🎲 baseline_random.py – Random Performance

This script plays N random games and records the final score and max tile in each game.

```bash
python baseline_random.py --episodes 500 --out baseline.csv
```

Output:
A CSV with 3 columns: episode, score, and max_tile.

## 🎲 baseline_heuristic.py – Basic Heuristic

This script plays N games with the rule of doing the first possible action in the order ```["Left", "Down", "Right", "Up"]``` and records the final score and max tile in each game.

```bash
python baseline_heuristic.py --episodes 500 --out heuristic.csv
```

Output:
A CSV with 3 columns: episode, score, and max_tile.

## 📈 charts.py – Visualization

Create quick plots from baseline.csv:

```bash
python charts.py baseline.csv
```

or generate a charts with n different csv as parameters

```bash
python charts.py baseline.csv heuristic.csv
```

It generates:

- figs/score_hist.png – Histogram of final scores
- figs/tile_hist.png – Histogram of highest tiles reached

## 📊 Sample Baseline (Random Agent)

After 500 random games, you might see results like:

| Metric Type   | Typical Value |
| ------------- |:-------------:|
| Avg. Score    |       200-400 |
| Max. Tile     |    around 128 |

## Baseline_heuristic.py

Following a simple heuristic of the first possible move in the order (left, down, right, up)

First few runs showed it having a worse result than the random agent

## Game2048_env.py

Gymnasium-compatible environment made using the game logic in engine.py

## env_test.py

Simple file to try and test Game2048_env.py file

## train_ppo.py

(subject to changes and tweaks)

## evaluate_ppo.py

(subject to changes and tweaks)

## 🛣️ What’s Next?

Coming soon:

- Further polish PPO and track its results
- Train a DQN agent using PyTorch or Stable-Baselines3
- Add a Streamlit UI to watch the trained agent play

## 📜 License

MIT — use it however you like!

## 🙋‍♂️ Author

Built for fun and learning
