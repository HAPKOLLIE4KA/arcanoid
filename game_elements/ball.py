from global_data import *
import pygame
from random import choice, randint
from typing import List
from game_elements.brick import DestructibleBrick, UnDestructibleBrick, Brick
from game_elements.level import Level


class Ball:
    def __init__(self):
        self.sound = pygame.mixer.Sound('sound/ball_crash.ogg')
        self._x = 0
        self._y = 0
        self._dx = 0
        self._dy = 0
        self._rect = pygame.Rect(self._x, self._y, BALL_RADIUS, BALL_RADIUS)
        self._ball_is_start = False

    def check_crash_bricks(self, bricks: List[List[Brick]], level: Level, set_crash: (), add_bonus: ()):
        ball = self._test_move()
        ind = level.getInd()
        crash_rect = None
        for i, j in ind:
            if bricks[i][j] is not None:  # если в этом месте сущ-ет кирпич
                rect = bricks[i][j].get_rect()
                if ball.colliderect(rect):  # если мяч столкнулся с кирпичом
                    crash_rect = rect
                    if isinstance(bricks[i][j], DestructibleBrick):
                        bricks[i][j] = None  # удаление кирпича
                        level.minus_brick()
                        level.deleteInd(i, j)
                        set_crash()
                        if self._choice_true(): add_bonus(self._x, self._y)
            else:
                level.deleteInd(i, j)

        if crash_rect is not None: self._check(ball, crash_rect, False)  # проверяется сторона удара

    def move(self):
        self._x += self._dx
        self._y += self._dy
        self._rect = pygame.Rect(self._x, self._y, BALL_RADIUS, BALL_RADIUS)

    def draw(self, surf: pygame.Surface):
        y = GAMEFIELD_HEIGHT - self._y
        if y <= 255 and self._dy > 0:
            color = (255, 0, 0)
        elif 255 < y <= 510 or y <= 255 and self._dy < 0:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        pygame.draw.circle(surf, color, (self._x, self._y), BALL_RADIUS)

    def _check(self, ball: pygame.Rect, rect: pygame.Rect, is_paddle: bool):
        self.sound.play()
        if ball.left < rect.left and self._dx > 0:  # Столкновение слева
            self._dx *= -1
        elif ball.right > rect.right and self._dx < 0:  # Столкновение справа
            self._dx *= -1
        elif ball.top < rect.top and self._dy > 0:  # Столкновение сверху
            self._dy *= -1
        elif not is_paddle:  # Столкновение снизу
            self._dy *= -1

    def _test_move(self) -> pygame.Rect:
        return pygame.Rect(self._x + self._dx, self._y + self._dy, BALL_RADIUS, BALL_RADIUS)

    def check_crash_paddle(self, paddle: pygame.Rect):
        ball = self._test_move()
        if ball.colliderect(paddle):
            self._check(ball, paddle, True)
            self.sound.play()

    def start_ball(self):
        if not self._ball_is_start:
            self._dx = randint(2, 4) * choice([-1, 1])
            self._dy = -randint(2, 4)
            self._ball_is_start = True

    def binding_to_paddle(self, paddle: pygame.Rect):
        if not self._ball_is_start:
            self._x = paddle.centerx
            self._y = paddle.top - BALL_RADIUS

    def get_rect(self):
        return self._rect

    def start_bonus_ball(self, paddle: pygame.Rect):
        self._x = paddle.centerx
        self._y = paddle.top - BALL_RADIUS
        self.start_ball()

    def _choice_true(self):
        if randint(0, 20) == 15: return True

