from chekers import Checker
from gamemap import GameMap
from logicgame import LogicGame


class Bot:

    def __init__(self, game, rank, name, name_enemy):

        self._name = name
        self._name_enemy = name_enemy

        self._army = {'white': [], 'black': []}
        self._army_old = {'white': [(objct.king, *objct.coordinates) for objct in game.get_army('white')],
                          'black': [(objct.king, *objct.coordinates) for objct in game.get_army('black')]}

        for key, armies in self._army_old.items():
            for row in armies:
                _obj = Checker(key)
                _obj._king, _obj._x, _obj._y = row
                self._army[key].append(_obj)

        self._game = LogicGame(self._army['white'], self._army['black'])
        self._game_map = GameMap(rank, self._game.armies)


    def movement(self, coordinates, coord, user_movement_func):

        self._game.army_list(self._game_map, self._name)
        self._list = self._game._army_move_list

        obj = self._game_map.get_object(*coordinates)

        # print('User generator map', self._name, obj.cell_number, '->',self._game_map.get_name_cell(*coord))

        user_movement_func(self._game_map, self._game, obj, coord)

        # print(self._game_map)

        self._game.army_list(self._game_map, self._name)
        self._game.army_list(self._game_map, self._name_enemy)

        _list = [(objct.king, *objct.coordinates) for objct in self._game.army_fight_list]

        return _list
