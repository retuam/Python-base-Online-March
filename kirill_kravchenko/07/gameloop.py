from random import choice
from chekers import Checker
from gamemap import GameMap
from logicgame import LogicGame
from botai import Bot

rank = 8
limit = 12
radius = 1
# if select start position, set number, zero by default, 1 - start position 1
_case = 0
# test mode test_case = True. In test mode user is not exist
test_case = False
# test mode color should be 'auto' if you select user in test mode sgould be set color to 'white' or 'black'
color = 'auto'

def set_initial_coord(objects, n, m, x, y, rank, delta):
    """
    This is a function initializes default start coordinates of checkers
    :param objects: objects is Checkers object list
    :param rank: rank of deck
    :param radius: rules of raduius step by default
    :param n: step to top or to bottom
    :param m: border of step to top or bottom
    :param x: start y coordinate
    :param y: start y coordinate
    :type objects: list
    :type rank: int
    :type radius: int
    :type n: int
    :type m: int
    :type x: int
    :type y: int
    :return: objects
    :rtype: list
    """
    for obj in objects:

        if n * y < m:
            if x > rank - delta:
                y += n * delta
                if y % 2:
                    x = 0
                else:
                    x = delta

            obj.coordinates = (x, y)
            x += 2

    return objects


def fight_coord(move, move_coord):
    """
    This is a function set and get fight coord after fight
    :param move: star coordinates
    :param move_coord: fight coordinates
    :type move: tuple
    :type move_coord: tuple
    :return: coordinates
    :rtype: tuple
    """
    _x_start, _y_start = move
    _x_enemy, _y_enemy = move_coord

    _x, _y = 2 * _x_enemy - _x_start, 2 * _y_enemy - _y_start

    return (_x_enemy, _y_enemy, _x, _y)


def movement(game_map, game, obj, coord):
    """
    This is a function defenites movement action
    :param game_map: game_map is GameMap object
    :param game: game is Game object
    :param obj: obj is Checker object
    :param coord: coord is x, y coordinates of the movement
    :type game_map: object GameMap
    :type game: object Game
    :type obj: object Checker
    :type coord: tuple (x, y)
    """
    # for log after game
    _name = obj.name
    _from = obj.cell_number
    # delete the object from map
    old_coord = obj.coordinates
    game_map.delete_object(*old_coord)
    # check the king status if condition done
    if obj.king:
        # set do else soft move to king
        obj.do_else = game_map.delete_on_diagonal(old_coord, coord)
    else:
        obj.king = coord[1]
    # set new coordinates of object
    obj.coordinates = coord
    # get cell number from map for new coordinate
    # set the object cell number
    obj.cell_number = game_map.get_name_cell(*coord)
    # put the object to map for new coordinate
    game_map.set_object(obj, *coord)
    # for log after game
    _to = obj.cell_number
    # add move to log
    game.log = (_name, _from, '-', _to)
    # set new permitted for map
    game_map.set_permitted_moves(game.armies)


def to_fight(game_map, game, obj, name, name_enemy, to_coord=()):
    """
    This is a function defenites fight action
    :param game: game is Game object
    :param game_map: game_map is GameMap object
    :param obj: obj is Checker object
    :param name: name is name of gamer
    :param name_enemy: name_enemy is name of enemy
    :param to_coord: to_coord is coordinates to fight for user gamer
    :type game_map: object GameMap
    :type game: object Game
    :type obj: object Checker
    :type name: str
    :type name_enemy: str
    :type to_coord: tuple
    :return: for flag for user
    :rtype: bool if returned
    """
    if not to_coord:
        coord = choice(obj.permitted_fight)
    else:
        coord = to_coord

    # set do else soft move to king
    obj.do_else = obj.king
    # for log after game
    _from = obj.cell_number
    # coordinates for enemy and coordinates for set after fight
    _x_enemy, _y_enemy, _x, _y = coord
    # clean cell on map, delete checker
    game_map.delete_object(*obj.coordinates)
    # select enemy object from map
    enemy = game_map.get_object(_x_enemy, _y_enemy)
    # clean enemy object from map
    game_map.delete_object(_x_enemy, _y_enemy)
    # check the king status if condition done
    obj.king = _y
    # set new coordinates for check after fight
    obj.coordinates = (_x, _y)
    # get cell number from map for new coordinate
    # set the object cell number
    obj.cell_number = game_map.get_name_cell(_x, _y)
    # put the object to map for new coordinate
    game_map.set_object(obj, _x, _y)
    # for log after game
    _to = obj.cell_number
    # add fight to log
    game.log = (name, _from, ':', _to)
    # delete enemy from its army
    game.get_army(name_enemy).remove(enemy)
    # delete enemy from armies (all armies)
    game.armies.remove(enemy)
    # set new permitted moves for armies
    game_map.set_permitted_moves(game.armies)
    # set permitted move for moving cecker
    obj.set_permitted(game_map.get_permitted_moves(name))
    # recursion for auto fight, it is excepted for user gamer
    if obj.permitted_fight and not to_coord:
        coord = choice(obj.permitted_fight)
        to_fight(game_map, game, obj, name, name_enemy, coord)
    # if adding move exist for user it return True
    elif obj.permitted_fight and to_coord:
        return True


def add_king_move(game_map, game, obj, name, name_enemy):
    """
    This is a recursive function defenites additional step for king
    :param game: game is Game object
    :param game_map: game_map is GameMap object
    :param obj: obj is Checker object
    :param name: name is name of gamer
    :param name_enemy: name_enemy is name of enemy
    :type game_map: object GameMap
    :type game: object Game
    :type obj: object Checker
    :type name: str
    :type name_enemy: str
    :return: themselves
    :rtype: function
    """
    print(game_map)

    for item in army[name_enemy]:
        if item.status_delete:
            army[name_enemy].remove(item)
            game.armies.remove(item)

    game.army_list(game_map, name)
    game_map.set_permitted_moves(game.armies)
    obj.set_permitted(game_map.get_permitted_moves(name))

    # Always step (for tst mode)
    do_else_move = choice([True])

    if game.army_fight_list:

        # do fight if fighting exist, speciafic rules
        if obj.permitted_fight:
            to_fight(game_map, game, obj, name, name_enemy)
        else:
            return

    elif obj.permitted_soft and do_else_move:

        coord = choice(obj.permitted_soft)
        movement(game_map, game, obj, coord)

    else:
        return

    add_king_move(game_map, game, obj, name, name_enemy)


def user_stepper(game_map, game, name, name_enemy):

    coordinates_to_fight = [obj.coordinates for obj in game.army_fight_list]
    coordinates_to_soft = []

    while True:

        move = str(input('Move, example to move or to fight "h3g4": '))

        if len(move) < 3:
            continue

        move_coord = ()

        if (move[0] in game_map.get_line_x()) and (move[1] in game_map.get_line_y()):
            move_coord = game_map.get_coordinate(move[0], move[1])

        if not move_coord:
            continue

        obj = game_map.get_object(*move_coord)

        if not isinstance(obj, Checker):
            continue

        coordinates_to_move = obj.permitted

        if obj.king:
            coordinates_to_soft = obj.permitted_soft

        _move_coord = ()

        if (move[2] in game_map.get_line_x()) and (move[3] in game_map.get_line_y()):
            _move_coord = game_map.get_coordinate(move[2], move[3])

        if not _move_coord:
            continue

        obj_move = game_map.get_object(*_move_coord)

        if coordinates_to_fight:

            if obj.king and _move_coord in coordinates_to_soft and not isinstance(obj_move, Checker):

                movement(game_map, game, obj, _move_coord)
                game.army_list(game_map, name_enemy)
                game_map.set_permitted_moves(game.armies)

                print(game_map)

                obj.set_permitted(game_map.get_permitted_moves(name))

                if obj.do_else:

                    while obj.do_else and obj.permitted_soft:

                        move_else = str(input('Move ELSE, example to move "g4" (free cell after fight) or set "n" for end step: '))

                        if move_else != 'n':

                            move_coord_else = ()

                            if (move_else[0] in game_map.get_line_x()) and (move_else[1] in game_map.get_line_y()):
                                move_coord_else = game_map.get_coordinate(move_else[0], move_else[1])

                            if move_coord_else not in obj.permitted_soft:
                                continue

                            movement(game_map, game, obj, move_coord_else)
                            game.army_list(game_map, name_enemy)
                            game_map.set_permitted_moves(game.armies)

                            print(game_map)

                            obj.set_permitted(game_map.get_permitted_moves(name))

                        elif not obj.permitted_fight:
                            break

                break

            elif isinstance(obj_move, Checker) and move_coord in coordinates_to_fight:

                to_move_coord = fight_coord(move_coord, _move_coord)
                flag = to_fight(game_map, game, obj, name, name_enemy, to_move_coord)

                if not flag:
                    break
                else:

                    while obj.permitted_fight and flag:

                        print(game_map)

                        move_else = str(input('Move ELSE, example to move "g4", enemy cell for fight: '))

                        move_coord_else = ()

                        if (move_else[0] in game_map.get_line_x()) and (move_else[1] in game_map.get_line_y()):
                            move_coord_else = game_map.get_coordinate(move_else[0], move_else[1])

                        if move_coord_else not in obj.permitted_fight_coord:
                            continue

                        to_move_coord = fight_coord(obj.coordinates, move_coord_else)
                        flag = to_fight(game_map, game, obj, name, name_enemy, to_move_coord)

                    print(game_map)
                    break

        elif _move_coord in coordinates_to_move:

            movement(game_map, game, obj, _move_coord)

            obj.set_permitted(game_map.get_permitted_moves(name))

            if obj.do_else:

                print(game_map)

                while obj.do_else and obj.permitted_soft:

                    move_else = str(
                        input('Move ELSE, example to move "g4" (free cell after fight) or set "n" for end step: '))

                    if move_else != 'n':

                        move_coord_else = ()

                        if (move_else[0] in game_map.get_line_x()) and (move_else[1] in game_map.get_line_y()):
                            move_coord_else = game_map.get_coordinate(move_else[0], move_else[1])

                        if move_coord_else not in obj.permitted_soft:
                            continue

                        movement(game_map, game, obj, move_coord_else)
                        game.army_list(game_map, name_enemy)
                        game_map.set_permitted_moves(game.armies)

                        print(game_map)

                        obj.set_permitted(game_map.get_permitted_moves(name))

                    elif not obj.permitted_fight:
                        break

            break

    return True


def bot_stepper(game_map, game, name, name_enemy, rank, test_case):
    """
    This is a function defenites bot movement
    :param game_map: game_map is GameMap object
    :param game: game is Game object
    :param name: name is name of gamer
    :param name_enemy: name_enemy is name of enemy
    :type game_map: object GameMap
    :type game: object Game
    :type name: str
    :type name_enemy: str
    :return: rules for no draw map
    :rtype: bool
    """
    if game.army_fight_list:

        obj = choice(game.army_fight_list)
        to_fight(game_map, game, obj, name, name_enemy)

    elif game.army_move_list:

        _check = []

        for obj in game.army_move_list:
            for coord in obj.permitted:
                bot = Bot(game, rank, name, name_enemy)

                _list = bot.movement(obj.coordinates, coord, movement)
                _check.append((obj, obj.coordinates, coord, len(_list)))

        _check = sorted(_check, key=lambda item: item[3])

        if not test_case:
            obj = _check[0][0]
            coord = _check[0][2]
        else:
            obj = choice(game.army_move_list)
            coord = choice(obj.permitted)

        movement(game_map, game, obj, coord)

    # additional for Bot king
    if obj.do_else:
        add_king_move(game_map, game, obj, name, name_enemy)

        return False
    else:
        return True

if _case == 1:

    stepper = [('black', 'white'), ('white', 'black')]
    army = {'white': [], 'black': []}

    #    A B C D E F G H
    #
    # 1 | |X| | | | | |o| 1
    # 2 | | | | | | | | | 2
    # 3 | | | |o| |o| |o| 3
    # 4 | | | | | | | | | 4
    # 5 | | | | | |x| | | 5
    # 6 | | | | | | | | | 6
    # 7 | |x| | | |x| |x| 7
    # 8 | | |x| |x| |x| | 8
    #
    #    A B C D E F G H

    test_white = [
        (False, 7, 0),
        (False, 7, 2),
        (False, 5, 2),
        (False, 3, 2),
    ]

    for row in test_white:
        obj = Checker('white')
        obj._king, obj._x, obj._y = row
        army['white'].append(obj)

    test_black = [
        (True, 1, 0),
        (False, 1, 6),
        (False, 2, 7),
        (False, 4, 7),
        (False, 5, 4),
        (False, 5, 6),
        (False, 7, 6),
    ]

    for row in test_black:
        obj = Checker('black')
        obj._king, obj._x, obj._y = row
        army['black'].append(obj)

else:

    stepper = [('white', 'black'), ('black', 'white')]

    army = {'white': [Checker('white') for i in range(limit)],
            'black': [Checker('black') for i in range(limit)]}

    army['white'] = set_initial_coord(army['white'], 1, (rank - radius), 1, 0, rank, radius)
    army['black'] = set_initial_coord(army['black'], -1, 0, 0, (rank - radius),rank, radius)

game = LogicGame(army['white'], army['black'])
game_map = GameMap(rank, game.armies)

if not test_case:
    while True:
        color = input('Select your color for a game [black - black, white - white, auto - auto]: ')
        if color in ('black', 'white', 'auto', 'long'):
            break

if color == 'auto':
    test_case = True
elif color == 'long':
    test_case = False

print(f'\nStart\n')
print(game_map)

i = 0
_end = True

while _end and i < 100:

    i += 1

    for step in stepper:

        if _end:
            name, name_enemy = step
            game.army_list(game_map, name)

            print(f'\nStep: {i} ({name})\n')

            if game.army_move_list or game.army_move_list:
                if color == name:
                    if_draw = user_stepper(game_map, game, name, name_enemy)
                else:
                    if_draw = bot_stepper(game_map, game, name, name_enemy, rank, test_case)

                if if_draw:
                    print(game_map)

            else:
                _end = False

    if not _end:
        print(f'{name_enemy.capitalize()} winner!\n')

if i == 100:
    win_white = len(game.get_army('white'))
    win_black = len(game.get_army('black'))
    if win_black > win_white:
        print(f'Black winner statistically!\n')
    elif win_black < win_white:
        print(f'White winner statistically!\n')
    else:
        print(f'Drafts in checkers!\n')

print(game)