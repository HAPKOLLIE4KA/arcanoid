import pygame
from global_data import *

class Paddle:
    def __init__(self):
        self._x = GAMEFIELD_WIDHT // 2 - PADDLE_WIDTH // 2
        self._y = LOWER_LINE - PADDLE_HEIGHT
        self._rect = pygame.Rect((self._x, self._y, PADDLE_WIDTH, PADDLE_HEIGHT))
        self._image = pygame.image.load("assets/paddle.png")

    def draw(self, surf: pygame.Surface):
        pygame.draw.rect(surf, "gray", self._rect, 1)
        surf.blit(self._image, (self._x, self._y))

    def move_to_cursor(self):
        mouse_x = pygame.mouse.get_pos()[0] - INDENT_SIDE

        if mouse_x < BRICK_WIDTH + PADDLE_WIDTH // 2 + INDENT_HORIZONTAL_BRICK:
            self._x = BRICK_WIDTH + INDENT_HORIZONTAL_BRICK
        elif mouse_x > GAMEFIELD_WIDHT - BRICK_WIDTH - PADDLE_WIDTH // 2:
            self._x = GAMEFIELD_WIDHT - BRICK_WIDTH - PADDLE_WIDTH
        else:
            self._x = mouse_x - PADDLE_WIDTH // 2
        self._new_rect()

    def _new_rect(self):
        self._rect = pygame.Rect((self._x, self._y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def get_rect(self):
        return self._rect

