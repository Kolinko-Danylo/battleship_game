import numpy
import copy


def read_file(path):
    """
    str -> numpy.array
    Read from path-file field and convert it into array.
    """
    arr = numpy.array([[0 for j in range(10)] for i in range(10)])
    string = open(path).readlines()
    for i in range(10):
        for j in range(10):
            if string[i][j] == '@':
                arr[i, j] = 1
            elif string[i][j] == 'X':
                arr[i, j] = -1
    return arr


def has_ship(arr, coordinates):
    """
    numpy.array, str -> bool
    Check if this coordinate contains ship.
    """
    try:
        assert coordinates[0].isalpha()
        y = ord(coordinates[0].capitalize()) - 65
        assert y in range(10)
        x = int(coordinates[1:]) - 1
        assert x in range(10)
        if arr[y, x] == 1:
            return True
        return False
    except (ValueError, AssertionError, IndexError):
        print('Wrong input!')
        return False


def is_valid(valid_arr):
    """
    numpy.array -> bool
    Check if field is valid.
    """
    # we will change our field, so I've decided to make a copy.
    arr = copy.copy(valid_arr)
    try:

        list_ships = []
        assert set(numpy.unique(arr)).issubset({-1, 0, 1})
        assert arr.shape == (10, 10)

        for i in range(10):
            for j in range(10):

                if abs(arr[i, j]) == 1:
                    starti, startj, new = i, j, []
                    # taking as many cells as we can

                    if (j + 1 <= 9) and abs(arr[i, j + 1]) == 1:
                        while startj < 10 and abs(arr[starti, startj]) == 1:
                            # check if the ship is separated from other
                            if starti < 9:
                                assert arr[starti + 1, startj] == 0
                            # append all coordinates
                            new.append((starti, startj))
                            arr[starti, startj] = 0
                            startj += 1
                        list_ships.append(new)

                    elif (i + 1 <= 9) and abs(arr[i + 1, j]) == 1:
                        while starti < 10 and abs(arr[starti, startj]) == 1:
                            # check if the ship is separated from other
                            if startj < 9:
                                assert (arr[starti, startj + 1] == 0)
                            new.append((starti, startj))
                            arr[starti, startj] = 0
                            starti += 1
                        list_ships.append(new)

                    else:
                        list_ships.append([tuple((i, j))])

        list_ships.sort(key=lambda x: len(x), reverse=True)

        counter = 0
        for i in range(1, 5):
            for j in range(i):
                if len(list_ships[counter]) != 5 - i:
                    return False
                counter += 1
        print(valid_arr)
        return True

    except AssertionError:
        return False


def field_to_str(arr):
    """
    Return the field from arr.
    :param arr: numpy.array
    :return: string with field
    """
    new_line = ''
    for j in range(10):
        for i in range(10):
            if arr[j, i] == 1:
                new_line += '@'
            elif arr[j, i] == -1:
                new_line += 'X'
            elif arr[j, i] == 0:
                new_line += '-'
            else:
                print('Wrong array')
                return
        new_line += '\n'
    return new_line


