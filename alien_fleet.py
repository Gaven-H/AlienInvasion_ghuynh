"""
Program: Alien Invasion - Alien Fleet
Author: Gaven Huynh
Purpose: Manages updating, spawning and collision of alien fleets.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 20th 2026
"""
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """
    Manages all aliens in the game.
    """
    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes the fleet.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
    
    def create_fleet(self) -> None:
        """
        Creates a centered grid-style formation of aliens,
        spawned on the right side of the screen.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.game.settings.screen_w
        screen_h = self.game.settings.screen_h

        fleet_cols, fleet_rows = self.calculate_fleet_size(
            alien_w, screen_w, alien_h, screen_h
            )
       
        x_offset, y_offset = self.calculate_offset(
            alien_w, alien_h, screen_w, screen_h, fleet_cols, fleet_rows
            )

        self._create_rectangle_fleet(
            alien_w, alien_h, fleet_cols, fleet_rows, x_offset, y_offset
            )

    def _create_rectangle_fleet(
            self, alien_w, alien_h, fleet_cols, fleet_rows, x_offset, y_offset
            ):
        """
        Creates a grid of aliens starting on the right side.
        """
        for row in range(fleet_rows):
            for col in range(fleet_cols):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offset(
            self, alien_w, alien_h, screen_w, screen_h, fleet_cols, fleet_rows
            ):
        """
        Centers the fleet vertically and places it on the right side.
        """
        fleet_width = fleet_cols * alien_w
        fleet_height = fleet_rows * alien_h

        x_offset = screen_w - fleet_width - alien_w
        y_offset = (screen_h - fleet_height) // 2

        return int(x_offset), int(y_offset)

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h) -> any:
        """
        Calculates how many aliens fit horizontally and vertically.
        """
        fleet_cols = (screen_w // alien_w)/2
        fleet_rows = (screen_h // alien_h)

        if fleet_cols % 2 == 0:
            fleet_cols -=1

        if fleet_rows % 2 == 0:
            fleet_rows -= 1

        return int(fleet_cols), int(fleet_rows)
    
    def _create_alien(self, current_x: int, current_y: int):
        """
        Creates a single alien and adds it to the fleet.
        """
        new_alien = Alien(self, current_x, current_y)
     
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
       """
        If any alien hits top/bottom:
        - shift fleet left
        - reverse vertical direction
        """
       alien: Alien
       for alien in self.fleet:
           if alien.check_edges():
               self._alien_fleet_move_left()
               self.fleet_direction *= -1
               break
    
    def _alien_fleet_move_left(self) -> None:
        """
        Moves all aliens left when edge is hit.
        """
        for alien in self.fleet:
            alien.x -= self.settings.fleet_drop_speed
            alien.rect.x = int(alien.x)

    def update_fleet(self) -> None:
        """
        Updates alien movement and checks for boundary collisions.
        """
        self._check_fleet_edges()
        self.fleet.update()
    
    def draw(self) -> None:
        """
        Draws all aliens on screen.
        """
        aline = 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """
        Handles bullet-alien collisions.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_left(self) -> bool:
        """
        Checks if any alien reaches the left edge (loss condition).
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
    
    def check_destroyed_status(self):
        """
        Checks if all aliens have been destroyed.
        """
        return not self.fleet