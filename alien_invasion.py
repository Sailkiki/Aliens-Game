import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    while True:
        gf.check_events()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让绘制的屏幕可见
        pygame.display.flip()


run_game()
