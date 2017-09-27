# coding=utf-8
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions


def run_game():
    pygame.init()  # 初始化游戏
    pygame.display.set_caption("Alien Invasion")  # 设置标题
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # 设置屏幕大小，获取screen对象
    ship = Ship(screen)  # 创建一艘飞船
    bullets = Group()

    while True:  # 开启游戏主循环
        game_functions.check_event(screen, ship, bullets)  # 监听键盘和鼠标事件
        ship.move()
        bullets.update(screen)
        game_functions.update_screen(setting, screen, ship, bullets)  # 更新屏幕上的图像


run_game()
