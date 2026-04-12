import sys
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True
        self.clock = pygame.time.Clock()

    def run_game(self):
        # Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
