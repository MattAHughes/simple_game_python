# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:16:56 2021

@author: Vitamin-C
"""
import ctypes

class Settings():
    """A class to store the settings of Alien Invasion -- the game."""
    
    def __init__(self):
        """Initializes the main game's static settings."""
        # Screen settings
        try:
            user32 = ctypes.windll.user32
            screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
            self.screen_width = screensize[0]
            self.screen_height = int(float(screensize[1] - 0.05 * screensize[0]))
        except:
            self.screen_width = screensize[0]
            self.screen_height = int(float(screensize[1] - 0.1 * screensize[0]))
        self.bg_colour = (230, 230, 230)
          
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10
        # We define fleet direction with a +- 1 modifier
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)