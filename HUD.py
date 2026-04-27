"""
Program: Alien Invasion - HUD
Author: Gaven Huynh
Purpose: Displays game information such as score, level, and remaining lives.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 27th 2026
"""
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:
    """
    Heads-Up Display that shows score, high score, level, and lives.
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initializes HUD elements and prepares initial visuals.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self) -> None:
        """
        Loads and prepares the life icon image.
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_w, self.settings.ship_h
            ))
        self.life_rect = self.life_image.get_rect()

    def update_scores(self) -> None:
        """
        Updates all score-related displays.
        """
        self._update_score()
        self._update_hi_score()
        self._update_max_score()
    
    def _update_score(self) -> None:
        """
        Updates the current score display.
        """
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True,
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.score_rect.bottom + self.padding

    def _update_max_score(self) -> None:
        """
        Updates the maximum score display.
        """
        max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True,
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding
    
    def _update_hi_score(self) -> None:
        """
        Updates the high score display.
        """
        hi_score_str = f'Hi-Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True,
            self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def update_level(self) -> None:
        """
        Updates the level display.
        """
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True,
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        screen_rect = self.screen.get_rect()

        self.level_rect.right = screen_rect.right - self.padding
        self.level_rect.bottom = screen_rect.bottom - self.padding

    def _draw_lives(self) -> None:
        """
        Draws remaining lives as ship icons.
        """
        screen_rect = self.screen.get_rect()

        current_x = screen_rect.right - self.padding - self.life_rect.width
        current_y = screen_rect.bottom - self.padding - self.life_rect.height

        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x -= (self.life_rect.width + self.padding)

        self.level_rect.bottom = current_y - self.padding
        self.level_rect.right = screen_rect.right - self.padding

    def draw(self) -> None:
        """
        Draws all HUD elements onto the screen.
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
