from source.entity import *


class Enemy(Entity):
    def __init__(self, pos, screen, groups, obstacle_sprites, name, life, dmg, speed, att_radius, notice_range, photo_path):
        super().__init__(screen, groups, obstacle_sprites, life, dmg, speed)
        self.sprite_type = 'enemy'
        self.image = pygame.image.load(photo_path).convert_alpha()
        self.hitbox_rect = self.image.get_rect(topleft=pos)
        self.rect = self.hitbox_rect.copy()
        self.hitbox = self.rect.inflate(0, 0)

        # stats
        self.name = name
        self.attack_radius = att_radius
        self.notice_range = notice_range
        self.status = 'move'

    # method for distance and direction between enemy and player
    # return distance, direction
    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()  # converting to distance from vec
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()

        return distance, direction

    # method to set status to attack/move
    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]
        direction = self.get_player_distance_direction(player)[1]

        if distance <= self.attack_radius:
            self.status = 'attack'
        else:
            self.status = 'move'

    # not done
    # method to attack or move
    def action(self, player):
        if self.status == 'attack':
            print('attack')
        else:
            self.direction = self.get_player_distance_direction(player)[1]
            print(self.direction)

    # updating move method
    def update(self):
        self.move(self.speed)

    # updating enemy status - move/attack
    def enemy_update(self, player):
        self.get_status(player)
        # self.action(player)
