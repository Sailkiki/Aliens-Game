import sys
import pygame

from settings import Settings


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:
        screen.fill(ai_settings.bg_color)
        # 监视键盘和鼠标事件

        # 让绘制的屏幕可见
        pygame.display.flip()


run_game()
