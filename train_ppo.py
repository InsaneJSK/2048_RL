"""
Train PPO agent on 2048

Usage:
    python train_ppo.py --timesteps 100000 --save trained_ppo.zip
    (Optional) Add --tensorboard to log training metrics.
"""

import os
import argparse
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv, VecMonitor
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import ProgressBarCallback
from game2048_env import Game2048Env

def make_env():
    def _init():
        env = Game2048Env()
        env = Monitor(env)  # Track episode stats
        return env
    return _init

def main(timesteps: int, save_path: str, use_tb: bool):
    num_envs = 4  # parallel envs for better CPU usage
    log_dir = "./ppo_logs"
    os.makedirs(log_dir, exist_ok=True)

    env = SubprocVecEnv([make_env() for _ in range(num_envs)])
    env = VecMonitor(env)

    print("Training PPO...")
    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
        n_steps=2048,
        batch_size=256,
        gae_lambda=0.95,
        gamma=0.99,
        learning_rate=3e-4,
        tensorboard_log=log_dir if use_tb else None,
        device="auto"
    )

    model.learn(total_timesteps=timesteps, progress_bar=True)
    model.save(save_path)
    print(f"✅ Model saved to {save_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--timesteps", type=int, default=100000, help="Total training timesteps")
    ap.add_argument("--save", default="trained_ppo.zip", help="Path to save trained model")
    ap.add_argument("--tensorboard", action="store_true", help="Enable TensorBoard logging")
    args = ap.parse_args()

    main(args.timesteps, args.save, args.tensorboard)
