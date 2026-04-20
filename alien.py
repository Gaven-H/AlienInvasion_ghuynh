"""
Program: Alien Invasion - Alien
Author: Gaven Huynh
Purpose: Represents the individual enemy aliens that move towards the ship.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 20th 2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """
    Represents a single alien enemy.
    """
    def __init__(self, fleet: "AlienFleet", x: float, y: float) -> None:
        """
        Initializes alien at the given position
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image= pygame.image.load(self.settings.alien_file)
        self.image= pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
             )
        
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        """
        Moves aliens vertically depending on the direction.
        """
        self.y += self.settings.fleet_speed * self.fleet.fleet_direction
        self.rect.y = int(self.y)
        self.rect.x = int(self.x)

    def check_edges(self) -> bool:
        """
        Checks if the alien has reached the top or bottom edge of the screen.
        """
        return (self.rect.top <= self.boundries.top
                or self.rect.bottom >= self.boundries.bottom)

    def draw_alien(self) -> None:
        """
        Draws the alien on the screen.
        """
        self.screen.blit(self.image, self.rect)