from source.shooting import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, screen, groups, obstacle_sprites, life, dmg, speed):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites
        self.screen = screen
        self.life = life
        self.dmg = dmg
        self.speed = speed
        self.direction = pygame.math.Vector2()

    # return entity life points
    def get_life(self):
        return self.life

    # change player life points + bonus
    def set_life(self, bonus):
        self.life += bonus

    # return entity dmg
    def get_dmg(self):
        return self.dmg

    # change player dmg + bonus
    def set_dmg(self, bonus):
        self.dmg += bonus

    # return entity speed
    def get_speed(self):
        return self.speed

    # change player speed + bonus
    def set_speed(self, bonus):
        self.speed += bonus

    # method to kill the entity
    def check_life(self):
        if self.life <= 0:
            self.kill()

    # move method
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collusion("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collusion("vertical")
        self.rect.center = self.hitbox.center

    # collusion with walls for now
    def collusion(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # moving right
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    # moving left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # moving down
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    # moving up
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
