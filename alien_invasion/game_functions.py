# coding=utf-8
import pygame
import sys


def check_event(ship):
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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.state = "stop"


def update_screen(setting, screen, ship):
    """更新屏幕上的图像"""
    screen.fill(setting.screen_color)  # 设置背景色rgb
    ship.draw()  # 绘制飞船
    pygame.display.flip()  # 让最近绘制的屏幕可见
