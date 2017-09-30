
import numpy as np
import time

DSP_W = 128
DSP_H = 64

class Game:
    def __init__(self):
        self.display = np.zeros(shape=(DSP_W, DSP_H), dtype=np.int16)
        self.player = Player()
        self.ball = Ball()
        self.bricks = [Brick()]



    def update(self):
        pass

    def render(self):
        for pixel in self.display:
            if 0:
                print("O")
            else:
                print("X")

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
    game = Game()
    while True:
        game.render()
        time.sleep(0.05)
