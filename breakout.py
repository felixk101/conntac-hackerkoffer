
import numpy as np
import time

DSP_W = 128
DSP_H = 64

BR_W = 13

class Game:
    def __init__(self):
        self.display = np.zeros(shape=(DSP_W, DSP_H), dtype=np.int16)
        self.player = Player()
        self.ball = Ball()


        self.bricks = []
        for rowpos in range(5):
            for colpos in range(8):
                self.bricks.append(Brick((colpos * (BR_W+3) + 1 + BR_W/2, 2 + rowpos * 4)))



    def update(self):
        self.ball.pos = self.ball.calc_new_pos()

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
            print("|", end="")
            for pixel in row:
                if pixel == 0:
                    print(" ", end="")
                else:
                    print("X", end="")
            print("|")
        print("-" * 128)


class Entity:
    def __init__(self, pos, width):
        self.pos = pos
        self.width = width
        self.height = 3

    def render(self, display):
        for y in range(int(self.pos[1] - (self.height - 1) / 2),
                           int(self.pos[1] + (self.height - 1) / 2) + 1):
            for x in range(int(self.pos[0] - (self.width - 1) / 2),
                           int(self.pos[0] + (self.width - 1) / 2) + 1):
                try:
                    display[x][y] = 1
                except IndexError:
                    continue


class Player(Entity):
    def __init__(self):
        super().__init__((64, 60), 31)


class Ball(Entity):
    def __init__(self):
        super().__init__((64, 25), 5)
        self.height = self.width
        self.direction = (0, 1)
        self.rotation = 180

    def calc_new_pos(self):
        return (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    @property
    def direction(self):
        return util.rotate(np.array((1.0, 0.0)), self.rotation)

    @direction.setter
    def direction(self, dir) -> None:
        x, y = dir[0], dir[1]
        self.rotation = math.atan2(-y, x) * 180 / math.pi


class Brick(Entity):
    def __init__(self, pos):
        super().__init__(pos, BR_W)


if __name__ == '__main__':
    game = Game()
    while True:
        game.update()
        game.render()
        time.sleep(1)
