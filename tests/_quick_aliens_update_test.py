import pygame
from alien import Aliens
pygame.init()
aliens = Aliens()
aliens.update(100)
print('Aliens rect', aliens.rect)
print('Aliens laser count', len(aliens.lasers))
print('Aliens movement direction', aliens.movement_direction)