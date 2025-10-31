import numpy as np

def roll_the_dice():
    return np.random.randint(1, 7)


def special_roll():
    return np.random.randint(0, 3)

def generate_surprises():
    special_tiles = np.random.choice(np.arange(1, 101), 10)
    return special_tiles