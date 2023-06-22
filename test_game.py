import unittest
from game_elements import Paddle
from game import Game


class TestGame(unittest.TestCase):
    # тестирование инициализации игры

    def setUp(self):
        self.paddle = Paddle()
        self.game = Game()

    def test_start_arcanoid(self):
        self.game._start_arcanoid()  # вызываем метод, который должен перевести игру в режим Arkanoid
        self.assertTrue(self.game._flag_arcanoid_game)
        self.assertFalse(self.game._flag_main_menu)
        self.assertFalse(self.game._flag_control_game)

    def test_control_menu(self):
        self.game._go_to_control()  # вызываем метод, который должен показывать экран управления
        self.assertTrue(self.game._flag_control_game)
        self.assertFalse(self.game._flag_main_menu)
        self.assertFalse(self.game._flag_arcanoid_game)

    # тестирование позиции платформы в зависимости от положения курсора
    def test_move(self):
        self.assertEqual(self.paddle.move_to_cursor(-100), 34)
        self.assertEqual(self.paddle.move_to_cursor(1323121332), 894)
        self.assertEqual(self.paddle.move_to_cursor(400), 350)


if __name__ == '__main__':
    unittest.main()
