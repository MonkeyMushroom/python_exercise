# coding=utf-8
import pygame
import sys

from bullet import Bullet
from alien import Alien


def check_event(setting, screen, ship, bullets):
    """监听键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击关闭按钮退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # 点击Esc退出
                sys.exit()
            elif event.key == pygame.K_LEFT:  # 通过左右键改变飞船状态
                ship.state = "left"
            elif event.key == pygame.K_RIGHT:
                ship.state = "right"
            elif event.key == pygame.K_UP:
                ship.state = "up"
            elif event.key == pygame.K_DOWN:
                ship.state = "down"
            elif event.key == pygame.K_SPACE:  # 空格键发射子弹
                bullet = Bullet(setting, screen, ship)  # 创建一颗子弹，并将其加入到编组bullets中
                bullets.add(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.state = "stop"


def update_bullet(bullets, aliens):
    """更新子弹位置，并删除屏幕外的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检测是否有子弹击中了外星人，即两个元素编组的碰撞，三四参数True表示删除碰撞元素，返回一个字典
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_screen(setting, screen, ship, bullets, aliens):
    """更新屏幕上的图像"""
    screen.fill(setting.screen_color)  # 设置背景色rgb
    ship.draw_ship()  # 绘制飞船
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # 绘制子弹
    for alien in aliens.sprites():
        alien.draw_alien()  # 绘制外星人
    pygame.display.flip()  # 让最近绘制的屏幕可见


def create_aliens(setting, screen, aliens):
    """创建外星人群"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    space = 2 * alien_width
    number = int((setting.screen_width - space) / alien_width)
    for i in range(number):
        alien = Alien(screen)
        alien.rect.centerx = alien.screen_rect.width / number + i * alien_width
        aliens.add(alien)


def game_success(setting, screen, x, y):
    """绘制游戏胜利文本"""
    font_obj = pygame.font.Font('asset/impact.ttf', setting.text_size)  # 通过字体文件获得字体对象
    text_surface_obj = font_obj.render("MISSION COMPLETE!", True, setting.text_color, setting.screen_color)  # 配置要显示的文字
    text_rect_obj = text_surface_obj.get_rect()  # 获得要显示的对象的rect
    text_rect_obj.center = (x, y)  # 设置显示对象的坐标
    screen.blit(text_surface_obj, text_rect_obj)  # 绘制字
    pygame.display.flip()
