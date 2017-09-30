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
    bullets = Group()  # 创建一个用于存储子弹的编组
    aliens = Group()  # 创建外星人编组
    game_functions.create_aliens(setting, screen, aliens)

    while True:  # 开启游戏主循环
        game_functions.check_event(setting, screen, ship, bullets)  # 监听键盘和鼠标事件
        ship.move()
        game_functions.update_bullet(bullets, aliens)
        game_functions.update_screen(setting, screen, ship, bullets, aliens)  # 更新屏幕上的图像
        if not aliens:  # 屏幕上没有外星人时，游戏结束
            game_functions.game_success(setting, screen, screen.get_rect().centerx, screen.get_rect().centery)


run_game()
