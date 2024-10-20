from typing import NamedTuple, List

from cell import Cell

class Ship:
    CELL = Cell.SHIP

    SHIPS: set = set()

    def _can_add_ship(self, position: List[NamedTuple]) -> bool:
        """
        Can a ship be added to the board

        Args:
            position (List[NamedTuple]): Ship positions to add

        Returns:
            bool: Can add ship
        """
        if len([pos for pos in position if pos in self.SHIPS]) == 0:
            return True
        return False

    def add_ship(self, position: List[NamedTuple]) -> None:
        """
        Add a ship to the boad

        Args:
            position (List[NamedTuple]): Ship position to add
        """
        if self._can_add_ship(position=position):
            for pos in position:
                self.SHIPS.add(pos)
