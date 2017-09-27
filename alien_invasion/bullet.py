# coding=utf-8
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ship, *groups):
        super(Bullet, self).__init__(*groups)
        self.screen = screen
        self.width = 2
        self.height = 12
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed = 1  # 移动速度

    def update(self, *args):
        self.rect.top -= 1 * self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.width)
