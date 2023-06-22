import pygame
from global_data import *
from typing import List
import json
from game_elements.brick import Brick, UnDestructibleBrick, DestructibleBrick
class Level:
    def __init__(self):
        self._all_count_brick = 0
        self._now_count_brick = 0
        self._player_crash_count_brick = 0
        self._bricks = self._init_bricks()
        self._ind = [[i, j] for i in range(LEVEL_COUNT_HEIGHT) for j in range(LEVEL_COUNT_WIDTH)]

    def _init_bricks(self) -> List[List[Brick]]:

        with open("data/level.json", 'r') as f:
            bricks = json.load(f)

        lv_bricks = [[Brick(i, j) for j in range(LEVEL_COUNT_WIDTH)] for i in range(LEVEL_COUNT_HEIGHT)]

        for i in range(LEVEL_COUNT_HEIGHT):
            for j in range(LEVEL_COUNT_WIDTH):
                if bricks[i][j] == 2 or bricks[i][j] == 3:
                    lv_bricks[i][j] = UnDestructibleBrick(i, j)
                elif bricks[i][j] == 1:
                    lv_bricks[i][j] = DestructibleBrick(i, j)
                    self._all_count_brick += 1
                else:
                    lv_bricks[i][j] = None

        self._now_count_brick = self._all_count_brick

        return lv_bricks

    def getInd(self) -> List[List[int]]:
        return self._ind

    def deleteInd(self, i, j):
        self._ind.remove([i, j])

    def draw(self, surf: pygame.Surface):
        for i in range(LEVEL_COUNT_HEIGHT):
            for j in range(LEVEL_COUNT_WIDTH):
                if self._bricks[i][j] is not None:
                    self._bricks[i][j].draw(surf)

    def minus_brick(self):
        self._now_count_brick -= 1
        self._player_crash_count_brick += 1

    def get_count_brick(self):
        return self._all_count_brick, self._now_count_brick, self._player_crash_count_brick

    def get_bricks(self):
        return self._bricks
