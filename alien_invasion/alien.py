import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, *groups):
        super(Alien, self).__init__(*groups)
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('drawable/alien.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
