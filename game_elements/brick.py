from global_data import *
import pygame
from random import choice


class Brick:
    def __init__(self, i, j):
        self._x = (j + 1) * INDENT_HORIZONTAL_BRICK + j * BRICK_WIDTH
        self._y = (i + 1) * INDENT_VERTICAL_BRICK + i * BRICK_HEIGHT
        self._rect = pygame.Rect(self._x - 2, self._y - 2, BRICK_WIDTH + 4, BRICK_HEIGHT + 4)
        self._image = None

    def draw(self, surf: pygame.Surface):
        # pygame.draw.rect(surf, "white", self._rect, 1)
        surf.blit(self._image, (self._x, self._y))

    def get_rect(self) -> pygame.Rect:
        return self._rect


class DestructibleBrick(Brick):

    def __init__(self, i, j):
        Brick.__init__(self, i, j)
        self._image = pygame.image.load(choice(BRICK_COLORS))


class UnDestructibleBrick(Brick):

    def __init__(self, i, j):
        Brick.__init__(self, i, j)
        self._image = pygame.image.load("assets/unbrick.png")
