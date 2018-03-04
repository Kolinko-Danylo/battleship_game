from game import Game
from player import Player
from field import Field
from generating import generate_field


def winner(str1, str2):
    """Check if anyone won te game."""
    if '@' not in str1 or '@' not in str2:
        return True
    return False


def write(path1, path2, game):
    'Write current results in personal file.'
    f1 = open(path1, 'w+')
    f2 = open(path2, 'w+')
    f_list = [f1, f2]
    f_list[game.current_player].write("Your field:\
    \n" + game.field_with_ships(game.current_player) + "\nEnemy's field:\
     \n" + game.field_without_ships(game.current_player - 1))


def main():
    "Play the game."
    name1 = input('1st player, enter your name: ')
    name2 = input('2nd player, enter your name: ')
    path1, path2 = '{}.txt'.format(name1), '{}.txt'.format(name2)
    player1 = Player(name1)
    player2 = Player(name2)
    ships1 = generate_field()
    field1 = Field(ships1)
    ships2 = generate_field()
    field2 = Field(ships2)
    game = Game(fields=[field1, field2], players=[player1, player2])
    write(path1=path1, path2=path2, game=game)

    print('New game.')
    while not winner(field1.field_with_ships(), field2.field_with_ships()):
        write(path1=path1, path2=path2, game=game)
        # making move.
        move = (game._players[game.current_player]).read_position()
        # if shot in the ship.
        if game.shot_at(move, game.current_player - 1):
            print('Yeah!')
            write(path1=path1, path2=path2, game=game)
        # if didn;t change the player.
        else:
            if game.current_player == 1:
                game.current_player = 0
            else:
                game.current_player = 1

    print('The end!')
    if '@' in field2.field_with_ships():
        print('Winner is {}'.format(player2._name))
    else:
        print('Winner is {}'.format(player1._name))

main()
