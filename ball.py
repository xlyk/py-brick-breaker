import pygame
from pygame.sprite import spritecollideany

import settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Direction:
    def __init__(self):
        self.x = 'up'
        self.y = 'left'


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 12
        self.height = 12
        self.top_margin = SCREEN_HEIGHT / 2
        self.center_screen = (SCREEN_WIDTH / 2) - (self.width / 2)

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.center_screen, self.top_margin)

        self.direction = Direction()
        self.speed = 2
        self.tilt_left = 0
        self.tilt_right = 0
        self.tilt_middle = 0

    def detect_side_hit(self, rect_1, rect_2):
        return abs(rect_1.right - rect_2.left) <= self.speed or abs(rect_1.left - rect_2.right) <= self.speed

    def detect_flip(self, player, bricks):
        if not player.dead:
            if self.rect.colliderect(player):
                # if self.detect_side_hit(self.rect, player.rect):
                #     player.dead = True
                #     return False, True

                # which part of player was hit?
                half = (player.rect.right - player.rect.left) / 2
                quarter = half / 2
                left_end = player.rect.left + quarter
                middle_end = left_end + half

                # player_middle = half + player.rect.left
                # ball_middle = ((self.rect.right - self.rect.left) / 2) + self.rect.left

                if self.rect.right < left_end:
                    self.tilt_middle = 0
                    if self.direction.y == "left":
                        self.tilt_left = 2
                elif self.rect.left > middle_end:
                    self.tilt_middle = 0
                    if self.direction.y == "right":
                        self.tilt_right = 2
                else:
                    pass
                    # TODO: detect middle of middle
                    # self.tilt_middle = 1

                return True, False

        # detect any collisions with bricks
        if b := spritecollideany(self, bricks):
            bricks.remove(b)
            self.tilt_left = self.tilt_right = 0
            if self.detect_side_hit(self.rect, b.rect):
                return False, True
            return True, False

        # no collisions
        return False, False

    def detect_wall(self, player):
        if self.rect.left < 0:
            self.tilt_left = self.tilt_right = 0
            self.rect.left = 0
            self.direction.y = 'right'
        if self.rect.right > SCREEN_WIDTH:
            self.tilt_left = self.tilt_right = 0
            self.rect.right = SCREEN_WIDTH
            self.direction.y = 'left'
        if self.rect.top <= 0:
            self.tilt_left = self.tilt_right = 0
            self.rect.top = 0
            self.direction.x = 'down'
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.direction.x = 'up'
            player.dead = False
            settings.DEAD = True

    def flip_direction(self, x_flip, y_flip):
        if x_flip:
            if self.direction.x == 'up':
                self.direction.x = 'down'
            elif self.direction.x == 'down':
                self.direction.x = 'up'
        if y_flip:
            if self.direction.y == 'left':
                self.direction.y = 'right'
            elif self.direction.y == 'right':
                self.direction.y = 'left'

    def update_location(self):
        if self.tilt_middle:
            tilt = self.tilt_middle
        else:
            tilt = 0

        y = 0
        if self.direction.x == 'up':
            y = -1 * (self.speed + tilt)
        elif self.direction.x == 'down':
            y = 1 * (self.speed + tilt)

        tilt = 0
        if self.direction.y == 'left':
            px = -1
            if self.tilt_left:
                tilt = px * self.tilt_left
        else:
            px = 1
            if self.tilt_right:
                tilt = px * self.tilt_right

        x = ((px * self.speed) + tilt)

        self.rect.move_ip(x, y)

    def update(self, screen, player, bricks):
        x_flip, y_flip = self.detect_flip(player, bricks)
        if x_flip or y_flip:
            self.flip_direction(x_flip, y_flip)
        else:
            self.detect_wall(player)
        self.update_location()




