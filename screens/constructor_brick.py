import pygame
from global_data import *


class ConstructorBrick:

    def __init__(self, i, j, type):
        self._type = type
        self._flag = True
        self._types = {
            0: {'standart': "green", "border": 1},
            1: {'standart': "green", "border": 0},
            2: {'standart': "red", "border": 0},
            3: {'standart': "red", "border": 0},
        }

        self._colors = {
            "focus": "white",
            "standart": self._types[type]['standart'],
            "click": "gold",
        }

        self._x = (j + 1) * INDENT_HORIZONTAL_BRICK + j * BRICK_WIDTH
        self._y = (i + 1) * INDENT_VERTICAL_BRICK + i * BRICK_HEIGHT
        self._width = BRICK_WIDTH
        self._height = BRICK_HEIGHT
        self._rect = pygame.Rect(self._x, self._y, BRICK_WIDTH, BRICK_HEIGHT)

        self._border = self._types[type]['border']
        self._color = self._types[type]['standart']

    def _on_click(self, sing):
        # self._type = (self._type + 1 * sing) % 3
        self._type = sing

        self._border = self._types[self._type]['border']
        self._colors['standart'] = self._types[self._type]['standart']
        self._flag = False

    def draw(self, surf: pygame.Surface, btn):

        self._color = self._colors['standart']
        pos = (pygame.mouse.get_pos()[0] - INDENT_SIDE, pygame.mouse.get_pos()[1] - INDENT_UP)
        if self._type != 3 and self._rect.collidepoint(pos):
            self._color = self._colors['focus']
            if self._flag and True in pygame.mouse.get_pressed():

                self._on_click(pygame.mouse.get_pressed().index(True))
                self._color = self._colors['click']

        if btn > 0:
            self._flag = True


        pygame.draw.rect(surf, self._color, self._rect, self._border)

    def get_type(self):
        return self._type
