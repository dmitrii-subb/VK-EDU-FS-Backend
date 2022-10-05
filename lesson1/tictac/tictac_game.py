import random
from sys import exit


PLAY_WITH_OTHER_PLAYER = 2
PLAY_WITH_COMPUTER = 1
OUT_OF_MOVES = 9


class TicTacGame:

    def __init__(self):
        self.board = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
        }
        self.moves = 0
        self.result = ''
        self.end_game = False

    def show_board(self):
        board = self.board
        print(f'|{board[1]}|{board[2]}|{board[3]}|')
        print(f'|{board[4]}|{board[5]}|{board[6]}|')
        print(f'|{board[7]}|{board[8]}|{board[9]}|')

    def validate_input(self, cell: str, range: tuple = (1, 9)) -> int:
        ''' check if input_num is actually an integer number '''
        try:
            cell = int(cell)
        except ValueError:
            raise ValueError(f'"{input_num}" is not an integer number')

        if cell < range[0] or cell > range[1]:
            raise ValueError('number out of range')

        if self.board[cell] in 'ox':
            raise ValueError('cell is busy')
        return cell

    def computer_move(self, mark: str) -> None:
        empty_cells = []
        for key, value in self.board.items():
            if value not in 'ox':
                empty_cells.append(key)

        cell = random.choice(empty_cells)
        self.board[cell] = mark
        self.moves += 1

    def player_move(self, player_mark: str) -> None:
        cell = input()
        cell = self.validate_input(cell, range=(1, 9))
        self.board[cell] = player_mark
        self.moves += 1

    def check_winner(self) -> bool:
        win_cases = [
            (1, 5, 9), (3, 5, 7), (1, 2, 3), (4, 5, 6),
            (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)
        ]
        for win in win_cases:
            if self.board[win[0]] == self.board[win[1]] == self.board[win[2]]:
                self.result = 'x win' if self.board[win[0]] == 'x' else 'o win'
                self.end_game = True
        if self.moves == OUT_OF_MOVES and not self.end_game:
            self.result = 'draw!'
            self.end_game = True

    def select_mode(self) -> int:
        print('--=[modes]=--\n')
        print('[1] one player')
        print('[2] two players\n')

        mode = input('mode number: ')
        try:
            mode = self.validate_input(mode, range=(1, 2))
        except ValueError as err:
            print(err)
            exit(1)

        if mode == PLAY_WITH_COMPUTER:
            print('\n[!] game with computer\n')
        else:
            print('\n[!] game with friend\n')
        return mode

    def start(self, mode: int) -> None:
        self.show_board()

        while not self.end_game:
            try:
                if self.moves % 2 == 0:
                    print('\nplayer 1 move: ', end='')
                    self.player_move('x')
                else:
                    if mode == PLAY_WITH_COMPUTER:
                        print('\ncomputer move:')
                        self.computer_move('o')
                    if mode == PLAY_WITH_OTHER_PLAYER:
                        print('\nplayer 2 move: ', end='')
                        self.player_move('o')
                self.show_board()
                self.check_winner()
            except Exception as err:
                print(err)
                continue

        print('\n--=[game over]=--\n')
        self.show_board()
        print(f'\nresult: {self.result}')


if __name__ == '__main__':
    game = TicTacGame()
    mode = game.select_mode()
    game.start(mode)
