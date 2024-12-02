from time import sleep

from nicegui import ui
import random


class TicTacToeGame:
    def __init__(self):
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False

    def reset_game(self):
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False
        self.update_board()

    def player_move(self, index):
        if not self.game_over and self.board[index] == '':
            self.board[index] = self.current_player
            if self.check_winner():
                self.game_over = True
                ui.notify(f'{self.current_player} a gagné !', type='positive')
            elif '' not in self.board:
                self.game_over = True
                ui.notify('Égalité !', type='warning')
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.update_board()

    def check_winner(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]  # Diagonales
        ]
        return any(
            self.board[a] == self.board[b] == self.board[c] and self.board[a] != ''
            for a, b, c in win_patterns
        )

    def update_board(self):
        for i, value in enumerate(self.board):
            buttons[i].text = value


game = TicTacToeGame()

ui.add_head_html('<style>body {background-color: #202a32; }</style>')

with ui.column().classes('grid grid-cols-3 flex item-center gap-5 w-[90%] mx-auto mb-10'):
    with ui.row().style('display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px'):
        buttons = [
            ui.button('', color='#7D4FFE', on_click=lambda _, i=i: game.player_move(i))
            .classes('h-[100px] p-[24%] text-[80px]')
            for i in range(9)
        ]

    ui.button('Recommencer', on_click=game.reset_game).classes('w-full h-12 bg-blue-500 text-white rounded-md')

ui.run()