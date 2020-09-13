from random import randint

import pygame
from pygame.sprite import Group

colors = [
    (230, 138, 0),
    (3, 252, 252),
    (237, 12, 72),
    (170, 17, 217),
    (37, 245, 10),
    (242, 235, 15),
]

brick_height = 35


def setup_bricks():
    group = Group()
    margin = 10
    y = 15

    for t in range(1, 4):
        if t == 1:
            y += 80
        brick_x = 65
        for i in range(1, 10):
            _b = Brick(f"brick_{i}", brick_x, y)
            group.add(_b)
            brick_x += _b.width + margin
        y += brick_height + margin

    return group


class Brick(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()

        self.name = name
        self.width = 66
        self.height = brick_height
        self.dead = False

        # surface
        self.surf = pygame.Surface((self.width, self.height))

        color_i = randint(0, len(colors) - 1)
        self.surf.fill(colors[color_i])

        # rectangle
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    # def update(self, screen, ball):
    #     if self.dead:
    #         return
    #
    #     hit = self.rect.colliderect(ball)
    #     if hit:
    #         self.dead = True
    #         print(f"hit detected: {self.name}")
