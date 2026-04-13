"""
Program: Alien Invasion - Bullet
Author: Gaven Huynh
Purpose: Contains the Bullet class which represents the projectile
shot out by the player to destroy invaders. They are initialized at
the front of the ship and are made to move from one side of the screen 
to the other.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 13th 2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """
    Represents a single bullet fired by the ship.
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Initializes the bullet at the ship's starting position.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image= pygame.image.load(self.settings.bullet_file)
        self.image= pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
             )
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = self.image.get_rect()
        self.rect.centery = game.ship.rect.centery
        self.rect.left = game.ship.rect.right
        self.x = float(self.rect.x)

    def update(self):
        """
        Moves the bullet horizontally across the screen.
        """
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """
        Draws the bullet on the screen.
        """
        self.screen.blit(self.image, self.rect)