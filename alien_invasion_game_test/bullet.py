# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:00:27 2021

@author: Vitamin-C
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets from the ship."""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)
        
        self. color = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """Moves the bullet in a straight line up the screen."""
        # Uses decimal position
        self.y -= self.speed_factor
        # To update the bullet position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draws the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
    