class Field:
    "Represents the field in battleship game by containing ships and shots"

    def __init__(self, ships_list):
        "Initialize ships as list and empty shot_list."
        self._ships = ships_list
        self.shot_list = []

    def shot_at(self, coordinates):
        """Return whether any ship contains coordinates, if it's last cell,
        shoot around the ship."""
        self.shot_list.append(coordinates)
        for i in self._ships:
            if i.shot_at(coordinates) == True:
                if len(i._hit) == i._length:
                    self._dead(i)
                return True
        return False

    def _dead(self, ship):
        """Shoot_arount the 'dead' ship."""
        x, y, x2, y2 = ship._quadrangle()
        for k in range(y, y2):
            for j in range(x, x2):
                self.shot_at((j, k))

    def _field_ships(self, flag):
        """It's suporting function for """
        # upper inscription
        field_str = '  12345678910\n'
        let = 'A'
        for i in range(10):
            for j in range(11):
                # side inscription
                if j == 0:
                    field_str += let + ' '
                    let = chr(ord(let) + 1)
                else:
                    # write shot cells
                    if tuple((j, i + 1)) in self.shot_list:
                        field_str += 'X'
                    # write ship cells if fiels_with_ships is calling.
                    elif flag == 1 and any(
                            [ship.exist(tuple((j, i + 1))) for ship in
                             self._ships]):
                        field_str += '@'
                    else:
                        field_str += '-'
            field_str += '\n'
        return field_str

    def field_without_ships(self):
        flag = 0
        return self._field_ships(flag)

    def field_with_ships(self):
        flag = 1
        return self._field_ships(flag)
