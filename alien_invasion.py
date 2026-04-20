"""
Program: Alien Invasion
Author: Gaven Huynh
Purpose: Contains the main game loop and controls for the game "Alien Invasion."
It initializes pygame, handles inputs, loads the settings, renders the screen,
and updates game objects. The bread and butter of the program.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 13th 2026
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep

class AlienInvasion:
    """
    Main class that manages the game initialization, execution
    event handling and screen updates.
    """
    def __init__(self) -> None:
        """
        Initializes the game, loads settings, creates the screen,
        loads assets, and initializes the ship.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))

    def run_game(self) -> None:
        """
        Starts and runs the main game loop.
        """
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:
        """
        Draws all visual elements to the screen and updates the display.
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        """
        Processes all user input events such as key presses and quitting out.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event) -> None:
        """
        Handles key release events to stop ship movement.
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event) -> None:
        """
        Handles key press events to control movement and firing.
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
                if self.ship.fire_method():
                    self.laser_sound.play()
                    self.laser_sound.fadeout(250)
        
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    """
    Entry point of the program. Creates and runs the game instance.
    """
    ai = AlienInvasion()
    ai.run_game()
