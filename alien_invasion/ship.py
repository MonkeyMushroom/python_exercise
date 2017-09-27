# coding=utf-8
import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - self.rect.width / 2
        self.rect.bottom = self.screen_rect.bottom

        self.state = "stop"  # 移动状态
        self.speed = 1  # 移动速度

    def draw_ship(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def move(self):
        """通过飞船状态移动飞船"""
        if self.state == "left" and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1 * self.speed
        elif self.state == "right" and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1 * self.speed
        elif self.state == "up" and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1 * self.speed
        elif self.state == "down" and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1 * self.speed
        else:
            pass
