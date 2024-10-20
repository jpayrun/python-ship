from typing import List
from cell import Cell


class Board:

    def __init__(self, rows: int = 7, cols: int = 7) -> None:
        """
        Constructor to build game board

        Args:
            rows (int, optional): Board rows. Defaults to 7.
            cols (int, optional): Board columns. Defaults to 7.
        """
        self.rows: int = rows
        self.cols: int = cols
        self._board: List[List[str]] = None

    def _build_board(self) -> None:
        """
        Build the game board
        """
        self._board = [[Cell.EMPTY for row in self.rows] for col in self.cols]

    @property
    def get_board(self) -> List[List[str]]:
        """
        Get the game board

        Returns:
            List[List[str]]: Game board
        """
        if self._board is None:
            self._build_board()
        return self._board

    def __str__(self):
        return ''.join([row for row in self.get_board])
