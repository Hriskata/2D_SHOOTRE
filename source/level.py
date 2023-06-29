import pygame.sprite

from source.settings import *
from source.tile import Tile
from source.player import Player
from source.enemy import Enemy
from source.ui import UI
from source.camera import CameraGroup


class Level:
    def __init__(self, screen):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.screen = screen

        self.create_map()

        self.ui = UI()

    # method that creates a map level using already loaded information from a data directory
    def create_map(self):
        # creating tiles
        for key, photo in tiles.items():
            for row_index, row in enumerate(WORLD_MAP):
                for column_index, col in enumerate(row):
                    x = column_index * game_settings["tilesize"]
                    y = row_index * game_settings["tilesize"]
                    if col == key:
                        Tile((x, y), [self.visible_sprites, self.obstacle_sprites], photo)

        # creating enemies
        for enemy in enemies:
            for row_index, row in enumerate(WORLD_MAP):
                for column_index, col in enumerate(row):
                    x = column_index * game_settings["tilesize"]
                    y = row_index * game_settings["tilesize"]
                    if col == enemy["id"]:
                        Enemy((x, y), self.screen, [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites,
                              enemy["name"], enemy["life"], enemy["dmg"], enemy["speed"], enemy["attack_radius"],
                              enemy["notice_range"], enemy["path"])

        # creating player
        self.player = Player((960, 704), self.screen, [self.visible_sprites], self.obstacle_sprites,
                             player_settings["life"], player_settings["dmg"], player_settings["speed"],
                             player_settings["photo_path"])

    # drawing and updating level
    def update(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        entity_group.update()
        self.ui.display(self.player)
