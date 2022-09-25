import random
from sys import exit


class TicTacGame:

    def __init__(self):
        self.board = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
        }
        self.moves = 0
        self.result = ''

    def show_board(self):
        board = self.board
        print(f'|{board[1]}|{board[2]}|{board[3]}|')
        print(f'|{board[4]}|{board[5]}|{board[6]}|')
        print(f'|{board[7]}|{board[8]}|{board[9]}|')

    def validate_input(self, input_num: int, range: tuple = (1, 9)) -> int:
        ''' check if input_num is actually an integer number '''
        try:
            input_num = int(input_num)
        except ValueError:
            raise ValueError(f'"{input_num}" is not an integer number')

        input_num = int(input_num)
        if input_num < range[0] or input_num > range[1]:
            raise ValueError('number out of range')

        return input_num

    def check_cell(self, cell) -> bool:
        ''' return True if cell is empty, False instead '''
        if self.board[cell] == 'o' or self.board[cell] == 'x':
            raise ValueError('cell is busy')
        return True

    def computer_move(self, mark: str):
        empty_cells = []
        for key, value in self.board.items():
            if value != 'x' and value != 'o':
                empty_cells.append(key)

        cell = random.choice(empty_cells)
        self.board[cell] = mark

    def player_move(self, player_mark: str):
        cell = input()
        cell = self.validate_input(cell, range=(1, 9))
        if self.check_cell(cell):
            self.board[cell] = player_mark

    def check_winner(self):
        win_cases = [
            (1, 5, 9), (3, 5, 7), (1, 2, 3), (4, 5, 6),
            (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)
        ]
        for c in win_cases:
            if self.board[c[0]] == self.board[c[1]] == self.board[c[2]]:
                self.result = 'x win!' if self.board[c[0]] == 'x' else 'o win!'
                return True
        if self.moves == 9:
            self.result = 'draw!'
            return True
        return False

    def select_mode(self) -> int:
        print('--=[modes]=--\n')
        print('[1] one player')
        print('[2] two players\n')

        mode = input('mode number: ')
        try:
            mode = self.validate_input(mode, range=(1, 2))
        except ValueError as e:
            print(e)
            exit(1)

        if mode == 1:
            print('\n[!] game with computer\n')
        else:
            print('\n[!] game with friend\n')
        return mode

    def make_move(self, player, mark):
        player(mark)
        self.show_board()
        self.moves += 1
        if self.check_winner():
            return True

    def start_game(self, mode: int):
        self.show_board()
        while self.moves < 9:
            try:
                print('\nplayer 1 move: ', end='')
                stop = self.make_move(self.player_move, 'x')
                if stop:
                    break

                if mode == 1:
                    print('\ncomputer move: ')
                    stop = self.make_move(self.computer_move, 'o')
                    if stop:
                        break
                else:
                    print('\nplayer 2 move: ', end='')
                    stop = self.make_move(self.player_move, 'o')
                    if stop:
                        break
            except Exception as e:
                print(e)
                continue

        print('\n--=[game over]=--\n')
        self.show_board()
        print(f'\nresult: {self.result}')


if __name__ == '__main__':
    game = TicTacGame()
    mode = game.select_mode()
    game.start_game(mode)
