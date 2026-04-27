"""
Program: Alien Invasion - Game Stats
Author: Gaven Huynh
Purpose: Contains the volitile data of the game.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 20th 2026
"""
# from pathlib import Path
import json
# from alien_invasion import AlienInvasion

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
    

class GameStats():
    def __init__(self, game) -> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.ships_left = self.settings.starting_ship_count
        self.reset_stats()
    
    def init_saved_scores(self) -> None:
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file
        
    def save_scores(self) -> None:
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self) -> None:
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions)
        # update max_score
        self._update_max_score()
        # update hi_score
        self._update_hi_score()

    def _update_max_score(self) -> None:
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_hi_score(self) -> None:
        if self.score > self.hi_score:
            self.hi_score = self.score
            # print(f'High: {self.hi_score}')


    def _update_score(self, collisions) -> None:
        for alian in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Basic: {self.score}')

    def update_level(self) -> None:
        self.level += 1
        # print(self.level)