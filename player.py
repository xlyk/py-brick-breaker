import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    width = 86
    height = 4
    top_margin = 650
    center_screen = (SCREEN_WIDTH / 2) - (width / 2)

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.center_screen, self.top_margin)
        self.dead = False

    def update(self, screen, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
