import sys
from source.level import *
from source.button import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((game_settings["width"], game_settings["height"]))
        pygame.display.set_caption(game_settings["title"])
        self.clock = pygame.time.Clock()

        # creating level object
        self.level = Level(self.screen)

    # method to run the game
    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.level.update()
            pygame.display.update()
            self.clock.tick(game_settings["fps"])


if __name__ == '__main__':
    game = Game()
    game.update()
