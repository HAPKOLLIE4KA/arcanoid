import pygame
import json
from global_data import *
from screens.button import Button
from screens.constructor_brick import ConstructorBrick


class Constructor:
    def __init__(self, con_exit):
        self._bricks = self._init_bricks()
        self._btn = -1
        self._image = pygame.image.load("assets/gamefield.png")
        self._surf = pygame.Surface((GAMEFIELD_WIDHT, LOWER_LINE))
        self._exit = con_exit
        self._button_save = Button(105, 600, 300, 75, "Сохранить",
                                   normal="#8EEB00", hover='#5C9900', pressed='#5C9900',
                                   onclickFunction=self._save)
        self._button_clear = Button(415, 600, 200, 75, "Clear",
                                    normal="#FF0000", hover='#A60000', pressed='#A60000',
                                    onclickFunction=self._clear)

        self._button_fill = Button(625, 600, 280, 75, "Заполнить",
                                   normal="#FF0000", hover='#A60000', pressed='#A60000',
                                   onclickFunction=self._fill)
        self._button_back = Button(915, 600, 200, 75, "Назад",
                                   normal="#FF7400", hover='#A65F00', pressed='#A65F00',
                                   onclickFunction=self._exit)

    def _clear(self):
        bricks = [[ConstructorBrick(0, 0, 0) for j in range(LEVEL_COUNT_WIDTH)] for i in range(LEVEL_COUNT_HEIGHT)]

        for i in range(LEVEL_COUNT_HEIGHT):
            for j in range(LEVEL_COUNT_WIDTH):
                if i == 0:
                    bricks[i][j] = ConstructorBrick(i, j, 3)
                elif j == 0 or j == LEVEL_COUNT_WIDTH - 1:
                    bricks[i][j] = ConstructorBrick(i, j, 3)
                elif i <= 17:
                    bricks[i][j] = ConstructorBrick(i, j, 0)
                else:
                    bricks[i][j] = None

        self._bricks = bricks

    def _fill(self):
        bricks = [[ConstructorBrick(0, 0, 0) for j in range(LEVEL_COUNT_WIDTH)] for i in range(LEVEL_COUNT_HEIGHT)]

        for i in range(LEVEL_COUNT_HEIGHT):
            for j in range(LEVEL_COUNT_WIDTH):
                if i == 0:
                    bricks[i][j] = ConstructorBrick(i, j, 3)
                elif j == 0 or j == LEVEL_COUNT_WIDTH - 1:
                    bricks[i][j] = ConstructorBrick(i, j, 3)
                elif i <= 17:
                    bricks[i][j] = ConstructorBrick(i, j, 1)
                else:
                    bricks[i][j] = None

        self._bricks = bricks

    def _save(self):
        level = [
            [self._bricks[i][j].get_type() if self._bricks[i][j] is not None else 0 for j in range(LEVEL_COUNT_WIDTH)]
            for i in range(LEVEL_COUNT_HEIGHT)]
        with open("data/level.json", "w") as f:
            json.dump(level, f)

        self._exit()

    def set_btn(self, btn):
        self._btn = btn

    def get_surface(self):
        return self._surf

    def draw(self, screen: pygame.Surface):
        self._surf.blit(self._image, (0, 0))

        for i in range(LEVEL_COUNT_HEIGHT):
            for j in range(LEVEL_COUNT_WIDTH):
                if self._bricks[i][j] is not None:
                    self._bricks[i][j].draw(self._surf, self._btn)

        self._button_save.process(screen)
        self._button_back.process(screen)
        self._button_clear.process(screen)
        self._button_fill.process(screen)

        screen.blit(self._surf, (INDENT_SIDE, INDENT_UP))
        pygame.display.update()

    def _init_bricks(self):

        with open("data/level.json", 'r') as f:
            bricks = json.load(f)

        lv_bricks = [[None for j in range(LEVEL_COUNT_WIDTH)] for i in range(LEVEL_COUNT_HEIGHT)]

        for i in range(LEVEL_COUNT_HEIGHT):
            for j in range(LEVEL_COUNT_WIDTH):
                if j == 0 or j == LEVEL_COUNT_WIDTH - 1 or i <= 17:
                    lv_bricks[i][j] = ConstructorBrick(i, j, bricks[i][j])

        return lv_bricks
