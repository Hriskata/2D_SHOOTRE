import pygame
from source.settings import *


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.life_bar_rect = pygame.Rect(10, 10, ui_settings["health_bar_width"], ui_settings["bar_height"])

    # draw bars rects
    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, ui_settings["ui_bg_color"], self.life_bar_rect)

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)

    # display bar rect
    def display(self, player):
        self.show_bar(player.get_life(), player_settings["life"], self.life_bar_rect, ui_settings["health_color"])
