import gym
from gym import error, spaces, utils
from gym.utils import seeding


class XPL(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        print("init xpl")

    def step(self, action):
        print("step")

    def reset(self):
        print("reset")
        # Set simulation speed for faster training

        # Reset airplane

    def render(self, mode="human"):
        print("render")

    def quit(self):
        print("quit")
