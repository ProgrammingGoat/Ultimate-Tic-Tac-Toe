"""
Tic Tac Toe within Tic Tac Toe
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .game import game

import logging

logger = logging.getLogger(__name__)


class UltimateTicTacToe(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        # logging setup
        logging.basicConfig(filename=self.paths.logs / "tictactoe.log", level=logging.INFO)

        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Button Handlers
        def press_button(button: toga.Button, i, j, k, l):
            # get legal move(s)
            x, y = game.next_move

            # catch illegal move
            if x is not None and (i != x or j != y):
                print("illegal from app.py")
                return

            # disable previous highlight
            if x is not None:
                for row in game_box.children[x].children[y].children:
                    for style_button in row.children:
                        style_button.style.update(background_color="transparent")
                        style_button.refresh()
            placed, subgame_win, board_win = game.play(i, j, k, l)
            if placed:
                button.text = placed
                logger.info(f"Player {placed} played in {i}/{j} {k}/{l}")
                logger.info(f"Grid: {game.subgames[i][j].grid}")
                if subgame_win is not None:
                    logger.info(f"Player {placed} wins grid {i}/{j}!")
                    # replace tictactoe with X or O
                    for row in game_box.children[i].children[j].children:
                        for button in row.children:
                            button.enabled = False
                    if board_win is not None:
                        logger.info(f"Player {placed} wins the main grid!")
                        self.main_window.info_dialog(f"{board_win} won!", f"{board_win} won!")

                # highlight next legal move, unless every move is legal
                x, y = game.next_move
                if x is not None:
                    for row in game_box.children[x].children[y].children:
                        for style_button in row.children:
                            style_button.style.update(background_color="lightgreen")
                            style_button.refresh()

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
                            style=Pack(width=50, 
                                       height=50, 
                                       font_size=20, 
                                       font_weight="bold",
                                       font_family="cursive",
                                       text_align="center",))
                        button_row.add(button)
                row.add(column)

        main_box.add(game_box)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(480, 480), resizable=False)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return UltimateTicTacToe()
