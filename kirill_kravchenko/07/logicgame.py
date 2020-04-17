from random import choice


class LogicGame:

    def __init__(self, army, army_enemy):

        self._army = {'white': army, 'black': army_enemy}
        self._armies = army + army_enemy
        self._log = []


    def get_armies(self):
        return self._armies


    def set_armies(self, armies):
        self._armies = armies


    armies = property(get_armies, set_armies)


    @property
    def army_move_list(self):

        try:
            output = self._army_move_list
        except AttributeError:
            output = []

        return output


    @property
    def army_fight_list(self):

        try:
            output = self._army_fight_list
        except AttributeError:
            output = []

        return output


    def get_army(self, name):
        return self._army[name]


    def army_list(self, game_map, name):
        """
        This is a function to resolve list of checkers
        :param self: self is LogicGame object
        :param game_map: self is GameMap object
        :param name: list of checkers
        :type self: object
        :type game_map: object
        :type name: str
        """
        self._army_move_list = []
        self._army_fight_list = []

        for obj in self._army[name]:

            obj.set_permitted(game_map.get_permitted_moves(name))

            if obj.status_delete:
                self._army[name].remove(obj)
                self._armies.remove(obj)
            else:
                if obj.permitted:
                    self._army_move_list.append(obj)

                if obj.permitted_fight:
                    self._army_fight_list.append(obj)


    def __str__(self):

        j = 0
        k = 0
        flag = ''
        result = ''

        for row in self._log:

            if row[0] == 'white':
                if row[0] != flag:
                    j += 1
                result += f'{j} - {row[0]}: {row[1]}{row[2]}{row[3]}\n'
            elif row[0] == 'black':
                if row[0] != flag:
                    k += 1
                result += f'{k} - {row[0]}: {row[1]}{row[2]}{row[3]}\n'

            flag = row[0]

        return result


    @property
    def log(self):
        return self._log


    @log.setter
    def log(self, log):
        self._log.append(log)