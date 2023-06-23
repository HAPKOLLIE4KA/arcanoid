import pygame
from global_data import *
from game_elements.game_field import GameField
from screens.control_menu import ControlMenu
from screens.main_menu import MainMenu
from screens.game_screen import GameScreen
from screens.constructor import Constructor


class Game:

    def __init__(self):
        pygame.init()
        self.sound = pygame.mixer.Sound('sound/tap_key.ogg')
        self._clock = pygame.time.Clock()
        self._game_screen = GameScreen()
        self._game_field = GameField(self._game_screen.get_screen())
        self._constructor = Constructor(self._game_screen.get_screen(), self._exit_constructor)
        self._main_menu = MainMenu(self._game_screen.get_screen(), self._exit_game, self._start_arcanoid,
                                   self._go_to_control, self._go_constructor)
        self._control_menu = ControlMenu(self._game_screen.get_screen(), self._exit_control)
        self._pause = False
        self._running = True
        self._flag_main_menu = True
        self._flag_arcanoid_game = False
        self._flag_control_game = False
        self._flag_constructor = False

    def game(self):
        self._clock.tick(FPS)
        while self._running:
            if self._flag_main_menu:
                self._menu()
            elif self._flag_arcanoid_game:
                self._arcanoid_game()
            elif self._flag_control_game:
                self._control_game()
            elif self._flag_constructor:
                self._constructor_menu()
        return True

    def _menu(self):
        self._game_screen.clear_screen()
        while self._flag_main_menu:
            self._menu_event()
            self._main_menu.draw()

    def _control_game(self):
        self._game_screen.clear_screen()
        while self._flag_control_game:
            self._control_game_event()
            self._control_menu.draw()

    def _constructor_menu(self):
        self._game_screen.clear_screen()
        while self._flag_constructor:
            self._constructor_event()
            self._constructor.draw()

    def _arcanoid_game(self):
        while self._flag_arcanoid_game:
            self._clock.tick(FPS)
            self._arcanoid_game_event()
            self._game_screen.update(self._game_field, self._pause)

    def _arcanoid_game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._game_field.start_ball()
                    self.sound.play()
                if event.key == pygame.K_r:
                    self._game_field.__init__(self._game_screen.get_screen())
                    self.sound.play()
                if event.key == pygame.K_ESCAPE:
                    self._restart_game()
                    self.sound.play()
                if event.key == pygame.K_p:
                    self._pause = not self._pause
                    self.sound.play()

    def _control_game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return

    def _menu_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return

    def _constructor_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP:
                self._constructor.set_btn(event.button)
            else:
                self._constructor.set_btn(-1)

    def _start_arcanoid(self):
        self._flag_main_menu = False
        self._flag_arcanoid_game = True

    def _exit_control(self):
        self._flag_control_game = False
        self._flag_main_menu = True

    def _go_to_control(self):
        self._flag_control_game = True
        self._flag_main_menu = False

    def _exit_game(self):
        self._running = False
        self._flag_main_menu = False

    def _go_constructor(self):
        self._flag_main_menu = False
        self._flag_constructor = True

    def _exit_constructor(self):
        self._flag_constructor = False
        self._flag_main_menu = True
        self._constructor.__init__(self._game_screen.get_screen(), self._exit_constructor)
        self._game_field.__init__(self._game_screen.get_screen())

    def _restart_game(self):
        self._flag_arcanoid_game = False
        self._flag_main_menu = True
        self._pause = False
        self._game_field.__init__(self._game_screen.get_screen())
        pass
