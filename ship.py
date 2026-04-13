import pygame
from settings import Settings

class Ship:
    from alien_invasion import AlienInvasion

    def __init__(self, game: AlienInvasion) -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen