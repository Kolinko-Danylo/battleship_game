from ship import Ship
import random as r


def generate_field():
    """Return valid field 10x10 with 10 ships."""
    lst = []
    # generate 1: 4-cells ship, 2: 3-cells, 3: 2, 4: 1.
    for i in range(1, 5):
        length = 5 - i
        for j in range(i):
            while True:

                horizontal = r.choice((False, True))
                bow = tuple((r.randint(1, 10), r.randint(1, 10)))

                # check if ship in the field.
                if bow[not int(horizontal)] + length - 1 <= 10:
                    if len(lst) == 0:
                        break
                    if not_overlap(lst, horizontal, bow, length):
                        break

            lst.append(Ship(bow=bow, length=length, horizontal=horizontal))

    return lst


def not_overlap(lst, horizontal, bow, length):
    """Check if current ship doesn't overlap with anyone else."""
    s = Ship(bow=bow, length=length, horizontal=horizontal)
    x, y, x2, y2 = s._quadrangle()
    for i in lst:
        if any([i.exist((j, k)) for k in range(y, y2) for j in range(x, x2)]):
            return False
    return True
