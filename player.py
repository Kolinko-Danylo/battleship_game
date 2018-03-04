class Player:
    """Represents player in battleship game by name."""

    def __init__(self, name):
        'Initialize name of the player'
        self._name = name

    def read_position(self):
        "Read the players move and convert in sufficient format."
        try:
            st = input('{}, enter move: '.format(self._name))
            assert st[0].isalpha()
            y = ord(st[0].capitalize()) - 64
            assert y in range(1, 11)
            x = int(st[1:])
            assert x in range(1, 11)
            return (x, y)
        except (ValueError, AssertionError, IndexError):
            print('Wrong input!')
            return self.read_position()
