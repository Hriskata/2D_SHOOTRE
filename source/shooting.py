import pygame
import math
from source.settings import *


class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacle_sprite, angle, scale, speed, range, path):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        # drawing rect
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.obstacle_sprites = obstacle_sprite
        self.speed = speed
        self.shoot_spawn = pygame.time.get_ticks()
        self.shoot_range = range

        self.x = x
        self.y = y
        self.angle = angle

        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed

        self.hitbox = self.rect.inflate(50, 50)

    def shoot_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.hitbox.x = self.rect.x
        self.rect.y = int(self.y)
        self.hitbox.y = self.rect.y
        self.collusion()

        if pygame.time.get_ticks() - self.shoot_spawn > self.shoot_range:
            self.kill()

    # not working
    def collusion(self):
        for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(self.rect):
                entity_group.remove(self.rect)

    def update(self):
        self.shoot_movement()
