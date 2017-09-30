
import numpy as np
import time

DSP_W = 128
DSP_H = 64

class Game:
    def __init__(self):
        self.display = np.zeros(shape=(DSP_W, DSP_H), dtype=np.int16)
        self.player = Player()
        self.ball = Ball()
        self.bricks = [Brick((10, 10))]



    def update(self):
        pass

    def render(self):
        new_display = np.zeros(shape=(DSP_W, DSP_H), dtype=np.int16)
        self.player.render(new_display)
        self.ball.render(new_display)
        for brick in self.bricks:
            brick.render(new_display)
        self.display = new_display
        self.print_display()

    def print_display(self):
        print('\n'*80) # prints 80 line breaks
        print("-" * 128)
        for row in self.display.T:
            for pixel in row:
                if pixel == 0:
                    print(" ", end="")
                else:
                    print("X", end="")
            print("")
        print("-" * 128)


class Entity:
    def __init__(self, pos, width):
        self.pos = pos
        self.width = width
        self.height = 11

    def render(self, display):
        for y in range(start=self.pos[1] - (self.height - 1) / 2, stop=self.pos[1] + (self.height - 1) / 2):
            for x in range(start=self.pos[0] - (self.width-1)/2, stop=self.pos[0] + (self.width-1)/2):
                display[x][y] = 1


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
    game = Game()
    while True:
        game.render()
        time.sleep(1)
