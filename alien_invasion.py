import sys

import pygame

from settings import Settings
from game_stats import GameStats
from alien import Alien
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    #Initialize game and create a screen object. 
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Make a play button.
    play_button = Button(ai_settings, screen, "PLAY")
    #Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Make an Alien
    alien = Alien(ai_settings, screen)

    #start the main loop for the game.
    while True:
        gf.check_events (ai_settings,stats, play_button, sb, screen, ship, bullets, aliens)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship,  aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        

        #get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #make the most recently drawn screen visible.
        pygame.display.flip()

run_game()