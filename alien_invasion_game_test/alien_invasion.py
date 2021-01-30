# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:59:20 2021

@author: Vitamin-C
"""
import pygame
from settings import Settings # local settings.py module
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import os

"""This is the basic form of a game created using pygame."""

def run_game():
    # Initialise pygame, settings, and screen object.
    os.chdir('D:\\Projects\\python_work\\alien_invasion_game_test')
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
        ) # Potentially work in checking screen resolution
    pygame.display.set_caption("Alien Invasion")
    
    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group for the ships bullets
    bullets = Group()
    # Make an alien group
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game
    while True:
        # Check for events to respond to
        gf.check_events(ai_settings, screen, stats, sb, play_button, 
                        ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, 
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)
    
run_game()


