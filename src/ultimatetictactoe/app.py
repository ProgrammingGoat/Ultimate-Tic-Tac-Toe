"""
Tic Tac Toe within Tic Tac Toe
"""

import toga
from toga.constants import RED, TRANSPARENT
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .game import game


class UltimateTicTacToe(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        # game objects
        active_player = 0
        # main_game = TicTacToe()
        # subgames = []
        # for i in range(3):
        #      subgames.append([])
        #      for j in range(3):
        #           subgames[i].append(TicTacToe())

        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Button Handlers
        def press_button(button: toga.Button, i, j, k, l):
                    # player = game.subgames[i][j].play(k, l, game.active_player)
                    # if player is not None:
                    #     button.text = player
                    #     win = game.subgames[i][j].determine_victory()
                    #     if win is not None:
                    #         game_box.children[i].children[j].clear()
                    #         game_box.children[i].children[j].add(toga.Label(player, style=Pack(width=150, height=150, alignment="center", font_size=100)))
                    #         game.main_game.play(i, j, 0 if player == "X" else 1)
                    #         big_win = game.main_game.determine_victory()
                    #         if big_win is not None:
                    #              self.main_window.info_dialog("Somebody won!", "Somebody won!")
            placed, subgame_win, board_win = game.play(i, j, k, l)
            if placed:
                button.text = placed
                if subgame_win is not None:
                    # replace tictactoe with X or O
                    game_box.children[i].children[j].clear()
                    game_box.children[i].children[j].add(toga.Label(placed, style=Pack(width=150, height=150, alignment="center", font_size=100)))
                    if board_win is not None:
                        self.main_window.info_dialog(f"{board_win} won!", f"{board_win} won!")

        # Game info
        game_info_box = toga.Box()
        game_info_label = toga.Label("It's some player's turn!", style=Pack(font_size=15, padding=10, alignment="center"))
        game_info_box.add(game_info_label)
        main_box.add(game_info_box)

        game_box = toga.Box(style=Pack(direction=COLUMN))
        # Creating the large grid
        for i in range(3):
            row = toga.Box(style=Pack(direction=ROW))
            game_box.add(row)

            for j in range(3):
                column = toga.Box(style=Pack(direction=COLUMN, padding=10))

                # Creating the small grid
                for k in range(3):
                    button_row = toga.Box(style=Pack(direction=ROW))
                    column.add(button_row)
                    for l in range(3):
                        button = toga.Button(
                            on_press=lambda widget, i=i, j=j, k=k, l=l: press_button(widget, i, j, k, l),
                            style=Pack(width=50, height=50))
                        button_row.add(button)
                row.add(column)

        main_box.add(game_box)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(480, 480), resizable=False)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return UltimateTicTacToe()
