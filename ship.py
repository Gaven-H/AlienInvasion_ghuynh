"""
Program: Alien Invasion - Ship
Author: Gaven Huynh
Purpose: Contains the class "Ship" which governs the behavior of the
player model. It handles loading the ship, movement, positioning and
interacting with the Arsenal (bullets) of the game.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 13th 2026
"""
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """
    Represents the player's ship, including movement and rendering.
    """
    def __init__(self, game: "AlienInvasion", arsenal: "Arsenal") -> None:
        """
        Initializes the ship, loads its image, and sets its starting position.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = self.screen.get_rect()
        
        self.image= pygame.image.load(self.settings.ship_file)
        self.image= pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
             )
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundries.midleft
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midleft = self.boundries.midleft
        self.x = float(self.rect.x)

    def update(self) -> None:
        """
        Updates the ship's position and its arsenal.
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Updates the vertical movement of the ship
        and keeps it within screen boundries.
        """
        temp_speed = self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= temp_speed
        
        if self.moving_down and self.rect.bottom < self.boundries.bottom:
            self.y += temp_speed
        
        self.rect.y = self.y

    def draw (self) -> None:
        """
        Draws the ship and its bullets on the screen.
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire_method(self) -> bool:
        """
        fires a bullet if the limit has not been reached and returns bool:
        True if a bullet was fired or False otherwise.
        """
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group) -> bool:
        """
        Checks collision with aliens.
        """
        if pygame.sprite.spritecollideany(self, other_group):
            return True
        return False