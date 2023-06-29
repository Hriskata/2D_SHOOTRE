from source.settings import *


# camera that keeps the player in the center of the screen
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = PLAYER_START_SCREEN_X
        self.half_height = PLAYER_START_SCREEN_Y
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load(game_settings["background_path"]).convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    # positioning the camera
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        # displaying all sprites in camera
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    # method to update enemy moving
    # not working yet
    def enemy_update(self, player):
        enemy_sprite = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprite:
            enemy.enemy_update(player)
