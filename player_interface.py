import random
from abc import ABC, abstractmethod


class Player(ABC):
    
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position
