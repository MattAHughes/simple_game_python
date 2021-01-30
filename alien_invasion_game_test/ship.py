# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:35:07 2021

@author: Vitamin-C
"""

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Contains the information and behaviour of the ship object."""
    
    def __init__(self, ai_settings, screen):
        """Initializes the ship and its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
        # Store the decimal value of the ships center as a float so we can modify speed easily
        self.center = float(self.rect.centerx)
            
        # Initialize movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ships position based on the movement flag and pixel center value."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update the ship rect from self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship at its current location using pygam blit."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx