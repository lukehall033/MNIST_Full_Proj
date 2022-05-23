import pygame as pg

class Game:

    def __init__(self):
        pg.display.init()
        self.window = pg.display.set_mode((400, 400))
        pg.display.set_caption("MNIST Test")

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
        pg.quit()
        quit()

game = Game()
game.run()