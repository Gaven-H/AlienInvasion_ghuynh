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
from button import Button
from HUD import HUD

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
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(1)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False

    def run_game(self) -> None:
        """
        Starts and runs the main game loop.
        """
        # Game Loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self) -> None:
        """
        Handles all collision logic:
        - Ship colliding with aliens
        - Aliens reaching left side (lose condition)
        - Bullets hitting aliens
        """
        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            #subtract one life
        #check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_left():
            self._check_game_status()
        #check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(250)
            self.game_stats.update(collisions)
            self.HUD.update_scores()
        
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # update game stats level
            self.game_stats.update_level()
            # update HUD view
            self.HUD.update_level()
        
    def _check_game_status(self):
        """
        Handles logic when the player loses a life.
        """
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

        print(self.game_stats.ships_left)
    
    def restart_game(self) -> None:
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _reset_level(self) -> None:
        """
        Resets the level by clearing bullets and respawning aliens.
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self) -> None:
        """
        Draws all elements and updates the display.
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self) -> None:
        """
        Processes all user input events such as key presses and quitting out.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()
            
    def _check_button_clicked(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

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
            self.game_stats.save_scores() 
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    """
    Entry point of the program. Creates and runs the game instance.
    """
    ai = AlienInvasion()
    ai.run_game()
