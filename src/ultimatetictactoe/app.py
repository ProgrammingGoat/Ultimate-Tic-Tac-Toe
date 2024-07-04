"""
Tic Tac Toe within Tic Tac Toe
"""

import toga
from toga.constants import RED, TRANSPARENT
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .tictactoe import tictactoe


class UltimateTicTacToe(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Button Handlers
        def press_button(button: toga.Button, i, j):
                    player = tictactoe.play(i, j)
                    if player is not None:
                        button.text = player
                        win = tictactoe.determine_victory()
                        if win is not None:
                            self.main_window.info_dialog("Victory!", f"Player {win} wins!")
                    print(tictactoe.grid)

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
                            on_press=lambda widget, i=i, j=j: press_button(widget, i, j),
                            style=Pack(width=50, height=50))
                        button_row.add(button)
                row.add(column)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(480, 480), resizable=False)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return UltimateTicTacToe()
