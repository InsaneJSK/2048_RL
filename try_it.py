from engine import Game2048

g = Game2048()
g.print_board()

while not g.gameover:
    g.step(g.random_action())  # 0 = up, 1 = down, 2 = left, 3 = right
    g.print_board()
    print("Score:", g.score)
