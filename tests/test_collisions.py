import os
import pygame
import sys

# Ensure SDL doesn't try to open a real window for tests
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from main import PySpaceInvaders
from spaceship import Spaceship
from alien import Aliens
from tools import MovingDirection


pygame.init()


def test_missile_hits_alien():
    game = PySpaceInvaders()

    # Choose one alien
    assert len(game.aliens.alien_list) > 0
    alien = game.aliens.alien_list[0]

    # Position missile so it overlaps with that alien rect
    missile_rect = pygame.Rect(alien.rect.centerx - 2, alien.rect.centery - 2, 4, 4)
    game.spaceship.missile.launch(missile_rect)

    # Force collision check
    game._collide_missile_and_aliens()

    # After collision, alien should be exploded and missile inactive
    assert alien.is_exploded or alien.delay_since_explosion > 0
    assert not game.spaceship.missile.is_active


def test_missile_hits_saucer():
    game = PySpaceInvaders()

    saucer = game.aliens.saucer
    # Launch saucer centered in screen
    saucer.launch((10, 10), MovingDirection.RIGHT)

    missile_rect = pygame.Rect(saucer.rect.centerx - 2, saucer.rect.centery - 2, 4, 4)
    game.spaceship.missile.launch(missile_rect)

    # Force collision check
    game._collide_missile_and_saucer()

    assert saucer.is_exploded
    assert not game.spaceship.missile.is_active
