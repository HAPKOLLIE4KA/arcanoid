import pygame
from global_data import *
from screens.button import Button
class ControlMenu:

    def __init__(self, exit_control):
        self._f1 = pygame.font.Font("font/Fibre.otf", 44)

        self._space = self._f1.render("SPACE - начать движение мяча в начале игры", False, "#D50065")
        self._p = self._f1.render("P - поставить игру на паузу / возобновить игру", False, "#D50065")
        self._esc = self._f1.render("escape - вернуться в главное меню", False, "#D50065")
        self._r = self._f1.render("R - перезапустить игру", False, "#D50065")
        self._mouse = self._f1.render("Управление платформой осуществляется мышью", False, "#D50065")
        self._button_back = Button(GAMESCREEN_WIDTH // 2 - 400 // 2, 580, 400, 75, "Назад",
                                   normal="#8EEB00", hover='#5C9900', pressed='#5C9900',
                                   onclickFunction=exit_control)

    def draw(self, screen: pygame.Surface):
        screen.blit(self._space, (GAMESCREEN_WIDTH // 2 - self._space.get_width() // 2, 125))
        screen.blit(self._r, (GAMESCREEN_WIDTH // 2 - self._r.get_width() // 2, 200))
        screen.blit(self._p, (GAMESCREEN_WIDTH // 2 - self._p.get_width() // 2, 275))
        screen.blit(self._esc, (GAMESCREEN_WIDTH // 2 - self._esc.get_width() // 2, 350))
        screen.blit(self._mouse, (GAMESCREEN_WIDTH // 2 - self._mouse.get_width() // 2, 425))
        self._button_back.process(screen)
        pygame.display.flip()
