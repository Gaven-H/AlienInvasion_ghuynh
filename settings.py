"""
Program: Alien Invasion - Settings
Author: Gaven Huynh
Purpose: Is the central hub for all "settings" for the game where values
can be configured to change the feel of the game.
Starter Code: Built upon starter code and assets provided by the class
then fully fleshed out by me in a different repo. That was imported
into this repo for further editing to make it more my own.
Date: April 13th 2026
"""
from pathlib import Path

class Settings:
    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 10

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 15
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5