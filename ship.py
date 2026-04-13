import pygame
from settings import Settings

class Ship:
    from alien_invasion import AlienInvasion

    def __init__(self, game: AlienInvasion) -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        self.image= pygame.image.load(self.settings.ship_file)
        self.image= pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
             )