import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class ShipArsenal:
    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal (self) -> None:
        self.arsenal.update()

    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()