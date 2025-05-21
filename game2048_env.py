import gym
from gym import spaces
import numpy as np
from engine import Game2048

class Game2048Env(gym.Env):
    def __init__(self):
        super(Game2048Env, self).__init__()
        self.game = Game2048()
        self.action_space = spaces.Discrete(4)  # 0 = up, 1 = down, 2 = left, 3 = right

        # Observation = 4x4 grid, each tile = log2(tile_value), 0 if empty
        self.observation_space = spaces.Box(low=0, high=15, shape=(4, 4), dtype=np.uint8)

    def reset(self):
        self.game.reset()
        return self._get_obs()

    def step(self, action):
        prev_score = self.game.score
        self.game.step(action)
        reward = self.game.score - prev_score
        obs = self._get_obs()
        done = self.game.gameover
        info = {}
        return obs, reward, done, info

    def render(self, mode='human'):
        self.game.print_board()

    def _get_obs(self):
        board = self.game.board.copy()
        board[board == 0] = 1  # so log2(0) becomes 0
        return np.log2(board).astype(np.uint8)

