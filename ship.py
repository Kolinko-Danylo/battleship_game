class Ship:
    """
    Represents the ship in battleship game as bow-coordinates, length and
    horizontal-vertical orientation. Also, You can 'shoot' at some cells, those
    cells will be in hit attribute.
    """

    def __init__(self, bow, length, horizontal):
        "Initial. bow as coordinate, length, horizontal as bool and empty hit."
        self.bow = bow
        self._length = length
        self.horizontal = horizontal
        self._hit = []

    def exist(self, coordinates):
        "Check if ship contains these coordinates"
        # dynamic generating of ship cells and entry check.
        if self.horizontal:
            if coordinates in [tuple((self.bow[0] + i, self.bow[1])) for i in
                               range(self._length)]:
                return True
        else:
            if coordinates in [tuple((self.bow[0], self.bow[1] + i)) for i in
                               range(self._length)]:
                return True
        return False

    def _quadrangle(self):
        "Return quadrangle around the ship bigger by one cell in all sides"
        x, y = self.bow[0] - 1, self.bow[1] - 1

        if self.horizontal:
            x2, y2 = x + self._length + 2, y + 3
        else:
            x2, y2 = x + 3, y + self._length + 2
        return x, y, x2, y2

    def shot_at(self, coord):
        "Return if ship contain coordinate and add to the hit if True."
        self._hit.append(coord)
        if self.exist(coord) == True and self._hit.count(coord) == 1:
            return True
        self._hit.pop()
        return False
