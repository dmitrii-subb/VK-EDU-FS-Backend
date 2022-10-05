from unittest import TestCase, main
from tictac.tictac_game import TicTacGame


class TicTacGameTest(TestCase):

    def setUp(self):
        self.game = TicTacGame()
        self.game.board = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
        }

    def test_input_validation(self):

        self.assertEqual(self.game.validate_input('1', (1, 2)), 1)
        self.assertEqual(self.game.validate_input('2', (1, 2)), 2)

        self.assertEqual(self.game.validate_input('0', (0, 10)), 0)
        self.assertEqual(self.game.validate_input('2', (0, 10)), 2)

    def test_input_validation_errors(self):
        with self.assertRaises(ValueError) as e:
            self.game.validate_input('2.1', (0, 10))
        self.assertEqual('"2.1" is not an integer number', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            self.game.validate_input('num', (1, 2))
        self.assertEqual('"num" is not an integer number', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            self.game.validate_input('3', (1, 2))
        self.assertEqual('number out of range', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            self.game.validate_input('-15', (-10, 0))
        self.assertEqual('number out of range', e.exception.args[0])

    def test_cell_validation(self):
        self.game.board = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: 'x', 6: '6',
            7: '7', 8: '8', 9: '9'
        }
        with self.assertRaises(ValueError) as e:
            self.game.validate_input(5)
        self.assertEqual('cell is busy', e.exception.args[0])

        self.assertEqual(self.game.validate_input(4), 4)

    def test_x_win_cross(self):
        self.game.board = {
            1: 'x', 2: '2', 3: '3',
            4: '4', 5: 'x', 6: '6',
            7: '7', 8: '8', 9: 'x'
        }
        self.game.check_winner()
        self.assertEqual('x win', self.game.result)
        self.assertEqual(True, self.game.end_game)

    def test_x_win_strait(self):
        self.game.board = {
            1: '1', 2: '2', 3: '3',
            4: 'x', 5: 'x', 6: 'x',
            7: '7', 8: '8', 9: '9'
        }
        self.game.check_winner()
        self.assertEqual('x win', self.game.result)
        self.assertEqual(True, self.game.end_game)

    def test_o_win_cross(self):
        self.game.board = {
            1: 'o', 2: '2', 3: '3',
            4: '4', 5: 'o', 6: '6',
            7: '7', 8: '8', 9: 'o'
        }
        self.game.check_winner()
        self.assertEqual('o win', self.game.result)
        self.assertEqual(True, self.game.end_game)

    def test_o_win_strait(self):
        self.game.board = {
            1: '1', 2: '2', 3: '3',
            4: 'o', 5: 'o', 6: 'o',
            7: '7', 8: '8', 9: '9'
        }
        self.game.check_winner()
        self.assertEqual('o win', self.game.result)
        self.assertEqual(True, self.game.end_game)

    def test_draw(self):
        self.game.board = {
            1: 'x', 2: 'o', 3: 'x',
            4: 'x', 5: 'o', 6: 'o',
            7: 'o', 8: 'x', 9: 'x'
        }
        self.game.moves = 9
        self.game.check_winner()
        self.assertEqual('draw!', self.game.result)
        self.assertEqual(True, self.game.end_game)


if __name__ == '__main__':
    main()
