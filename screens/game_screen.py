from global_data import *
import pygame
from game_elements.game_field import GameField

class GameScreen:
    def __init__(self):
        self._screen = pygame.display.set_mode((GAMESCREEN_WIDTH, GAMESCREEN_HEIGHT))
        self._image = pygame.image.load("assets/screen.png")
        self._screen.blit(self._image, (0, 0))
        pygame.display.set_caption("Arcanoid")
        pygame.display.set_icon(pygame.image.load("assets/gameIcon.png"))

    def update(self, game_field: GameField, pause: bool):
        game_field.update_state_game(pause)
        game_field.draw(pause)
        self._screen.blit(game_field.get_surface(), (INDENT_SIDE, INDENT_UP))
        pygame.display.flip()

    def clear_screen(self):
        self._screen.blit(self._image, (0, 0))
        pygame.display.flip()

    def get_screen(self):
        return self._screen

