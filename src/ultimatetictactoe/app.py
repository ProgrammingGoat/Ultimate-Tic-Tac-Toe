"""
Tic Tac Toe within Tic Tac Toe
"""

import toga
from toga.constants import RED, TRANSPARENT
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .tictactoe import TicTacToe


class UltimateTicTacToe(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        # game objects
        main_game = TicTacToe()
        subgames = []
        for i in range(3):
             subgames.append([])
             for j in range(3):
                  subgames[i].append(TicTacToe())

        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Button Handlers
        def press_button(button: toga.Button, i, j, k, l):
                    player = subgames[i][j].play(k, l)
                    print(subgames[i][j])
                    print(subgames[i][j].grid)
                    if player is not None:
                        button.text = player
                        win = subgames[i][j].determine_victory()
                        if win is not None:
                            main_game.play(i, j, 0 if player == "X" else 1)
                            big_win = main_game.determine_victory()
                            print(main_game.grid)
                            if big_win is not None:
                                 self.main_window.info_dialog("Somebody won!", "Somebody won!")

        # Game info
        game_info_box = toga.Box()
        game_info_label = toga.Label("It's some player's turn!", style=Pack(font_size=15, padding=10, alignment="center"))
        game_info_box.add(game_info_label)
        main_box.add(game_info_box)


        # Creating the large grid
        for i in range(3):
            row = toga.Box(style=Pack(direction=ROW))
            main_box.add(row)

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

        self.main_window = toga.MainWindow(title=self.formal_name, size=(480, 480), resizable=False)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return UltimateTicTacToe()
