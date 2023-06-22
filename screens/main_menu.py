import pygame
from global_data import *
from screens.button import Button
class MainMenu:

    def __init__(self, exit_game, start_arcanoid, go_to_control, go_constructor):
        self._f1 = pygame.font.Font("font/Fibre.otf", 125)

        self._name_game = self._f1.render("Arcanoid", False, "#D50065")
        self._button_start = Button(GAMESCREEN_WIDTH // 2 - 400 // 2, 200, 400, 75, "Начать игру",
                                    normal="#8EEB00", hover='#5C9900', pressed='#5C9900',
                                    onclickFunction=start_arcanoid)

        self._button_control = Button(GAMESCREEN_WIDTH // 2 - 400 // 2, 300, 400, 75, "Управление",
                                      normal="#FF7400", hover='#A65F00', pressed='#A65F00',
                                      onclickFunction=go_to_control)
        self._button_constructor = Button(GAMESCREEN_WIDTH // 2 - 400 // 2, 400, 400, 75, "Конструктор",
                                   normal="#2A17B1", hover='#150873', pressed='#150873',
                                   onclickFunction=go_constructor)
        self._button_exit = Button(GAMESCREEN_WIDTH // 2 - 400 // 2, 500, 400, 75, "Выйти",
                                   normal="#FF0000", hover='#A60000', pressed='#A60000',
                                   onclickFunction=exit_game)

    def draw(self, screen: pygame.Surface):
        screen.blit(self._name_game, (GAMESCREEN_WIDTH // 2 - self._name_game.get_width() // 2, 50))
        self._button_start.process(screen)
        self._button_control.process(screen)
        self._button_constructor.process(screen)
        self._button_exit.process(screen)
        pygame.display.flip()