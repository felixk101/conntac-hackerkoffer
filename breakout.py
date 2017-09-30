
import numpy as np

class Game:
    def __init__(self):
        self.display = np.zeros(shape=(128, 64), dtype=np.int16)r
        self.player =



    def update(self):
        pass

class Entity:
    def __init__(self, pos, width):
        self.pos = pos
        self.width = width
        self.display = np.zeros(shape=(128, 64), dtype=np.int16)
        self.height = 11

    def render(self):
        for y in range(start=self.pos[1] - (self.height - 1) / 2, stop=self.pos[1] + (self.height - 1) / 2):
            for x in range(start=self.pos[0] - (self.width-1)/2, stop=self.pos[0] + (self.width-1)/2):
                self.display[x, y] = 1


class Player(Entity):
    def __init__(self):
        super().__init__(64, 31)


class Ball(Entity):
    def __init__(self):
        super().__init__((64, 25), 6)
        self.height = self.width


class Brick(Entity):
    def __init__(self, pos):
        super().__init__(pos, 21)


if __name__ == '__main__':
    Game()