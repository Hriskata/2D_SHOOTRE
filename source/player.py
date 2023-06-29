import pygame.sprite

from source.entity import *


class Player(Entity):
    def __init__(self, pos, screen, groups, obstacle_sprites, life, dmg, speed, photo_path):
        super().__init__(screen, groups, obstacle_sprites, life, dmg, speed)
        self.original_image = pygame.image.load(photo_path).convert_alpha()
        self.image = self.original_image
        self.hitbox_rect = self.image.get_rect(topleft=pos)
        self.rect = self.hitbox_rect.copy()
        self.hitbox = self.rect.inflate(0, 0)

        self.groups = groups

        # shoot stats
        self.shoot_offset = pygame.math.Vector2(shooting_info["offset_x"], shooting_info["offset_y"])
        self.shoot = False
        self.shooting_cooldown = 0

    # user input to move
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # checking for shooting
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

    # player rotation method
    def player_rotation(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_map_x = self.rect.centerx - PLAYER_START_SCREEN_X + mouse_pos[0]
        mouse_map_y = self.rect.centery - PLAYER_START_SCREEN_Y + mouse_pos[1]
        self.angle = math.degrees(math.atan2(mouse_map_y - self.rect.centery, mouse_map_x - self.rect.centerx))
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    # creating bullet to shoot
    def is_shooting(self):
        if self.shooting_cooldown == 0:
            self.shooting_cooldown = shooting_info["cooldown"]
            shoot_spawn = pygame.math.Vector2(PLAYER_START_SCREEN_X, PLAYER_START_SCREEN_Y)
            shoot_spawn += self.shoot_offset.rotate(self.angle)
            self.shoot = Shoot(shoot_spawn[0], shoot_spawn[1], self.obstacle_sprites, self.angle, shooting_info["scale"],
                               shooting_info["speed"], shooting_info["range"], shooting_info["photo_path"])

            entity_group.add(self.shoot)

    # updating player
    def update(self):
        self.input()
        self.player_rotation()
        self.move(self.speed)
        entity_group.draw(self.screen)
        entity_group.update()

        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= 1
