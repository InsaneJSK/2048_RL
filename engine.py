import numpy as np
import matplotlib.pyplot as plt
class Game2048:

    def __init__(self, size=4):
        self.size = size
        self.score = 0
        self.gameover = False
        self.reset()

    def reset(self):
        self.board = np.zeros((4, 4))
        self.score = 0
        self.spawn()
        self.spawn()

    """def step(self, dir):
        # dir: 0 = up, 1 = down, 2 = left, 3 = right
        original_board = self.board.copy()

        self.board = self._move(dir)

        if not np.array_equal(original_board, self.board):
            self.spawn()
        self.is_game_over()
"""
    def step(self, dir):
        original_board = self.board.copy()
        self.board = self._move(dir)

        moved = not np.array_equal(original_board, self.board)

        if moved:
            self.spawn()
        self.is_game_over()

        return moved


    def print_board(self):
        print(self.board)

    def spawn(self):
        empty = list(zip(*np.where(self.board == 0)))
        if empty:
            i, j = empty[np.random.randint(len(empty))]
            self.board[i, j] = 2 if np.random.random() < 0.9 else 4
    
    def _move(self, dir):
        board = self.board.copy()
        board = np.rot90(board, -dir)  # rotate so we always move left
        for i in range(4):
            board[i] = self._merge_row(board[i])
        board = np.rot90(board, dir)  # rotate back
        return board

    def _merge_row(self, row):
        non_zero = row[row != 0]
        merged = []
        skip = False
        i = 0
        while i < len(non_zero):
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged.append(2 * non_zero[i])
                self.score += 2 * non_zero[i]
                i += 2
            else:
                merged.append(non_zero[i])
                i += 1
        merged += [0] * (len(row) - len(merged))
        return np.array(merged)

    def is_game_over(self):
        # any zero → not over
        if np.any(self.board == 0):
            self.gameover = False
            return

        original_score = self.score          
        for dir in range(4):
            if not np.array_equal(self.board, self._move(dir)):
                self.score = original_score
                self.gameover = False
                return
        self.score = original_score
        self.gameover = True
    
    def random_action(self):
        self.step(np.random.randint(0, 4))
