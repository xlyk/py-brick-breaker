import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_RETURN
)

import settings

from ball import Ball
from brick import setup_bricks
from player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def base():
    ball = Ball()
    player = Player()
    bricks = setup_bricks()

    pygame.event.pump()

    while settings.RUNNING:
        pygame.time.Clock().tick(200)

        # handle quitting
        restart = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    settings.RUNNING = False
                elif event.key == K_RETURN:
                    restart = True
            elif event.type == QUIT:
                settings.RUNNING = False

        if settings.DEAD:
            if restart:
                print("restart plz")
                bricks = setup_bricks()
                player = Player()
                ball = Ball()
                settings.DEAD = False
            continue

        # player
        player.update(screen, pygame.key.get_pressed())
        ball.update(screen, player, bricks)

        # draw background
        screen.fill((0, 0, 0))

        # draw sprites on screen
        for b in bricks:
            screen.blit(b.surf, b.rect)
        screen.blit(ball.surf, ball.rect)
        screen.blit(player.surf, player.rect)

        # update display
        pygame.display.flip()


if __name__ == '__main__':
    base()
