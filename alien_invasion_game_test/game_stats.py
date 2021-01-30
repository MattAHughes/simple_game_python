# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:31:51 2021

@author: Vitamin-C
"""

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # High scores never are reset
        self.high_score = 0
        # Define the current high score of all time.
        with open('current_highest_score.txt', 'r') as hs:
            self.data = hs.readlines()
            self.user_high_score = int(float(self.data[0]))    
        
        
    def reset_stats(self):
        """Initialize statistics that can change during a game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        # Create a game flag to give a game over.
        self.game_active = True

