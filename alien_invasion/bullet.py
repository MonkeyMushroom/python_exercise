# coding=utf-8
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting, screen, ship, *groups):
        super(Bullet, self).__init__(*groups)
        self.setting = setting
        self.screen = screen

        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed = 1  # 移动速度

    def update(self):
        self.rect.top -= 1 * self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.setting.bullet_color, self.rect, self.setting.bullet_width)
