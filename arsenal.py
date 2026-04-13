"""
Program: Alien Invasion - Arsenal
Author: Gaven Huynh
Purpose: This file contains the Arsenal class which has everything to
do with the player bullets in the game. From creation, positioning,
removing them, as well as drawing them; it handles all of the bullet logic.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 13th 2026
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """
    Manages a collection of bullets fired by the ship.
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Initializes the arsenal and bullet group.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal (self) -> None:
        """
        Updates all bullets and removes those off-screen.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """
        Removes bullets that have moved off the right side of the screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.game.screen.get_rect().right:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """
        Draws all bullets to the screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
        
    def fire_bullet(self) -> bool:
        """
        Creates and adds a new bullet if under the limit and returns bool:
        True if a bullet was created and False otherwise.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False