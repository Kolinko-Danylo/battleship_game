class Game:
    """
    Represents game in battleship game by fields and players. Can check if any
    ship contains enemy's coordinates and shows field with and without ships.
    """
    current_player = 1

    def __init__(self, fields, players):
        """Initialize fields and players."""
        self._field = fields
        self._players = players

    def shot_at(self, coordinates, c):
        """Check if any ship contains enemy's coordinates."""
        return self._field[c].shot_at(coordinates)

    def field_with_ships(self, c):
        """Return string with players field."""
        return self._field[c].field_with_ships()

    def field_without_ships(self, c):
        """Return string with players field without ships."""
        return self._field[c].field_without_ships()
