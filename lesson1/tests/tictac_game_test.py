from unittest import TestCase, main
from tictac.tictac_game import TicTacGame


class TicTacGameTest(TestCase):

    def test_input_validation(self):
        game = TicTacGame()

        self.assertEqual(game.validate_input('1', (1, 2)), 1)
        self.assertEqual(game.validate_input('2', (1, 2)), 2)

        self.assertEqual(game.validate_input('0', (0, 10)), 0)
        self.assertEqual(game.validate_input('2', (0, 10)), 2)

    def test_input_validation_errors(self):
        game = TicTacGame()

        with self.assertRaises(ValueError) as e:
            game.validate_input('2.1', (0, 10))
        self.assertEqual('"2.1" is not an integer number', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            game.validate_input('num', (1, 2))
        self.assertEqual('"num" is not an integer number', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            game.validate_input('3', (1, 2))
        self.assertEqual('number out of range', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            game.validate_input('-15', (-10, 0))
        self.assertEqual('number out of range', e.exception.args[0])

    def test_check_cell(self):
        game = TicTacGame()
        game.board = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: 'x', 6: '6',
            7: '7', 8: '8', 9: '9'
        }
        with self.assertRaises(ValueError) as e:
            game.check_cell(5)
        self.assertEqual('cell is busy', e.exception.args[0])

        self.assertEqual(game.check_cell(4), True)


if __name__ == '__main__':
    main()
