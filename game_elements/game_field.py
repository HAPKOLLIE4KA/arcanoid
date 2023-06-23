import pygame
from game_elements.paddle import Paddle
from game_elements.ball import Ball
from game_elements.level import Level
from game_elements.bonus import Bonus
from screens.screen import Screen
from global_data import *


class GameField(Screen):
    def __init__(self, screen):
        Screen.__init__(self, screen)
        self._bonus = []
        self._paddle = Paddle()
        self._balls = [Ball()]
        self._level = Level()
        self._image = pygame.image.load("assets/gamefield.png")
        self._state_image = pygame.image.load("assets/stata.png")
        self._surf = pygame.Surface((GAMEFIELD_WIDHT, GAMEFIELD_HEIGHT))
        self._loos = False
        self._win = False
        self._crash = True

    def get_surface(self) -> pygame.Surface:
        return self._surf

    def update_state_game(self, pause: bool):
        self._check_loose()
        self._check_win()
        if not self._loos and not pause and not self._win:
            for ball in self._balls: ball.check_crash_paddle(self._paddle.get_rect())
            for ball in self._balls: ball.check_crash_bricks(self._level.get_bricks(), self._level, self._set_crash,
                                                             self._add_bonus)
            self._paddle.move_to_cursor()

            for ball in self._balls: ball.move()
            for ball in self._balls: ball.binding_to_paddle(self._paddle.get_rect())
            for bonus in self._bonus: bonus.update(self._delete_bonus, self._paddle.get_rect(), self._add_ball)

    def start_ball(self):
        for ball in self._balls: ball.start_ball()

    def draw(self, pause: bool):
        if self._loos:
            self._draw_loos()
        elif self._win:
            self._draw_win()
        elif pause:
            self._draw_pause()
        else:
            self._draw_game()

    def _draw_game_statistics(self):
        if not self._crash: return

        acb, ncb, pccb = self._level.get_count_brick()
        font = pygame.font.Font("font/Fibre.otf", 30)
        acb_t = font.render(f"Всего кирпечей: {acb}", False, "#F0FC00")
        ncb_t = font.render(f"Осталось крипечей: {ncb}", False, "#F0FC00")
        pccb_t = font.render(f"Разрушено кирпичей: {pccb}", False, "#F0FC00")

        surf = pygame.Surface((GAMEFIELD_WIDHT, GAMEFIELD_HEIGHT - 520))
        surf.blit(self._state_image, (0, 0))
        surf.blit(acb_t, (0, 0))
        surf.blit(ncb_t, (0, 30))
        surf.blit(pccb_t, (0, 60))

        self._surf.blit(surf, (0, 520))

        self._crash = False

    def _draw_game(self):
        self._surf.blit(self._image, (0, 0))
        for bonus in self._bonus: bonus.draw(self._surf)
        self._draw_game_statistics()
        self._paddle.draw(self._surf)
        for ball in self._balls:  ball.draw(self._surf)
        self._level.draw(self._surf)

    def _draw_loos(self):
        f1 = pygame.font.Font("font/Fibre.otf", 125)
        f2 = pygame.font.Font("font/Fibre.otf", 45)
        loose_text = f1.render("поражение", False, "red")
        help_text = f2.render("Нажмите R, чтобы начать заново", False, "purple")
        self._surf.blit(loose_text, (GAMEFIELD_WIDHT // 2 - loose_text.get_width() // 2, 250))
        self._surf.blit(help_text, (GAMEFIELD_WIDHT // 2 - help_text.get_width() // 2, 370))
        pygame.display.update()

    def _draw_win(self):
        loose_text = pygame.font.Font("font/Fibre.otf", 125).render("Победа", False, "green")
        help_text = pygame.font.Font("font/Fibre.otf", 45).render("Нажмите R, чтобы начать заново",
                                                                  False, "purple")
        self._surf.blit(loose_text, (GAMEFIELD_WIDHT // 2 - loose_text.get_width() // 2, 250))
        self._surf.blit(help_text, (GAMEFIELD_WIDHT // 2 - help_text.get_width() // 2, 370))
        pygame.display.update()

    def _draw_pause(self):
        font = pygame.font.Font("font/Fibre.otf", 45)
        pause_text = font.render("Игра на паузе. Нажмите P, чтобы продолжить",
                                 False, "purple")
        self._surf.blit(pause_text, (GAMEFIELD_WIDHT // 2 - pause_text.get_width() // 2, 370))

    def _check_win(self):
        if not self._level.get_count_brick()[1]:
            self._win = True

    def _check_delete_ball(self):
        for ball in self._balls:
            if ball.get_rect().bottom >= LOWER_LINE + 10:
                self._balls.remove(ball)

    def _check_loose(self):
        self._check_delete_ball()
        if len(self._balls) == 0: self._loos = True

    def _set_crash(self):
        self._crash = True

    def _add_ball(self):
        ball = Ball()
        ball.start_bonus_ball(self._paddle.get_rect())
        self._balls.append(ball)

    def _add_bonus(self, x, y):
        self._bonus += [Bonus(x, y)]

    def _delete_bonus(self, bonus):
        self._bonus.remove(bonus)
