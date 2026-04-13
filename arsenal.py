import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class ShipArsenal:
    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings