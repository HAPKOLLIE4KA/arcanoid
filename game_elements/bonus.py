import pygame
from global_data import LOWER_LINE


class Bonus:

    def __init__(self, x, y):
        self._width = 15
        self._height = 15
        self._speed = 3
        self._x = x
        self._y = y
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
        self._image = pygame.image.load("assets/bonus.png")

    def _move(self):
        self._y += self._speed
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)

    def draw(self, surf: pygame.Surface):
        surf.blit(self._image, (self._x, self._y))

    def update(self, delete, paddle: pygame.Rect, add_ball):
        if self._rect.bottom >= LOWER_LINE:
            delete(self)
        elif paddle.colliderect(self._rect):
            add_ball()
            delete(self)
        else:
            self._move()

