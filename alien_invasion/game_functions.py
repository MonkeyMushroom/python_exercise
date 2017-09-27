# coding=utf-8
import pygame
import sys

from bullet import Bullet


def check_event(screen, ship, bullets):
    """监听键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 通过左右键改变飞船状态
            if event.key == pygame.K_LEFT:
                ship.state = "left"
            elif event.key == pygame.K_RIGHT:
                ship.state = "right"
            elif event.key == pygame.K_UP:
                ship.state = "up"
            elif event.key == pygame.K_DOWN:
                ship.state = "down"
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(screen, ship)
                bullets.add(bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.state = "stop"


def update_screen(setting, screen, ship, bullets):
    """更新屏幕上的图像"""
    screen.fill(setting.screen_color)  # 设置背景色rgb
    ship.draw_ship()  # 绘制飞船
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # 绘制子弹
    pygame.display.flip()  # 让最近绘制的屏幕可见
