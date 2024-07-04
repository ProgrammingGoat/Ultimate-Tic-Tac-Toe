"""
Tic Tac Toe within Tic Tac Toe
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .grid import tictactoe


class UltimateTicTacToe(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction=COLUMN))

        def press_button(button: toga.Button, i, j):
            player = tictactoe.play(i, j)
            if player is not None:
                button.text = player
                win = tictactoe.determine_victory()
                if win is not None:
                    self.main_window.info_dialog("Victory!", f"Player {win} wins!")
            print(tictactoe.grid)

        for i in range(3):
            row = toga.Box(style=Pack(direction=ROW))
            main_box.add(row)
            for j in range(3):
                button = toga.Button(
                    on_press=lambda widget, i=i, j=j: press_button(widget, i, j),
                    style=Pack(width=50, height=50))
                row.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return UltimateTicTacToe()
