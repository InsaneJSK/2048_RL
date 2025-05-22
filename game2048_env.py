import gymnasium as gym
from gymnasium import spaces
import numpy as np
from engine import Game2048


class Game2048Env(gym.Env):
    def __init__(self):
        super().__init__()
        self.game = Game2048()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=15, shape=(4, 4), dtype=np.uint8)

    # reset
    def reset(self, *, seed=None, options=None):
        self.game.reset()
        self.invalid_streak = 0
        return self._get_obs(), {}

    def step(self, action):
        """Take one step in the 2048 environment.
        Reward =  (Δscore)                      <- main task signal
                + 0.10 · log2(max-tile)              <- bigger tiles bonus encouraging pushing towards higher tiles
                + 0.05 · empty_tiles                 <- keep board open, more empty spaces naturally means more merging and easier gameplay
                - 1*invalid streak      if move is invalid          <- penalty so the model stops spamming invalid moves and get truncated
        """
        prev_score  = self.game.score
        prev_empty  = np.count_nonzero(self.game.board == 0)
        prev_max    = self.game.board.max()

        moved = self.game.step(action)

        delta_score  = (self.game.score - prev_score)
        max_tile_log = np.log2(self.game.board.max())
        empty_tiles  = np.count_nonzero(self.game.board == 0)

        reward  = delta_score
        reward += 0.10 * max_tile_log
        reward += 0.05 * empty_tiles

        self.invalid_streak = getattr(self, "invalid_streak", 0)
        if not moved:
            reward = -1.0*self.invalid_streak
            self.invalid_streak += 1
        else:
            self.invalid_streak = 0

        truncated   = self.invalid_streak >= 50
        terminated  = self.game.gameover

        info = {
            "moved":      moved,
            "deltaScore": delta_score,
            "maxTileLog": max_tile_log,
            "emptyTiles": empty_tiles,
            "raw_score":   self.game.score
        }
        return self._get_obs(), reward, terminated, truncated, info

    # utilities
    def _get_obs(self):
        board = self.game.board.copy()
        board[board == 0] = 1
        return np.log2(board).astype(np.uint8)

    @property
    def raw_board(self):
        return self.game.board

"""    # step
    def step(self, action):
        prev = self.game.score
        self.game.step(action)
        reward      = self.game.score - prev
        terminated  = self.game.gameover
        truncated   = False
        info        = {}
        return self._get_obs(), reward, terminated, truncated, info
"""   
