
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

    def render(self):
        pass




class Player(Entity):
    def __init__(self, pos, width):
        super().__init__(pos, width)
        self.size = np.array((31, 11))
        self.pos = 64

class Ball(Entity):
    def __init__(self, pos):
        super().__init__(pos, 6)

    def render(self):
        pass


class Brick(Entity):
    def __init__(self, pos, width):
        super().__init__(pos, width)


if __name__ == '__main__':
    Game()