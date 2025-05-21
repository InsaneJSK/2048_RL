from game2048_env import Game2048Env

env = Game2048Env()
obs = env.reset()
done = False
total_reward = 0

while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    total_reward += reward
    env.render()

print(f"Total reward: {total_reward}")
