class Checker:

    def __init__(self, name):

        self._name = name
        self._n_min = 0
        self._n_max = 7
        self._n_delta = 1
        self._king = False
        self.__gamer_one = 'white'
        self.__gamer_two = 'black'
        self.__field = 'field'
        self.__block = 'block'
        self.__fight = 'fight'
        self.__friend = 'friend'


    def __str__(self):

        if self._king == True:
            if self._name == self.__gamer_one:
                result = 'O'
            elif self._name == self.__gamer_two:
                result = 'X'
        else:
            if self._name == self.__gamer_one:
                result = 'o'
            elif self._name == self.__gamer_two:
                result = 'x'

        return result


    def get_cell_number(self):
        return self._cell_number


    def set_cell_number(self, name):
        self._cell_number = name


    cell_number = property(get_cell_number, set_cell_number)


    def get_coords(self):
        return self._x, self._y


    def set_coords(self, coord):
        self._x, self._y = coord


    coordinates = property(get_coords, set_coords)


    def get_do_else(self):

        try:
            output = self._do_else
        except AttributeError:
            output = False

        return output


    def set_do_else(self, name):
        self._do_else = name


    do_else = property(get_do_else, set_do_else)


    def get_status_delete(self):

        try:
            output = self._status_delete
        except AttributeError:
            output = False

        return output


    def set_status_delete(self, name):
        self._status_delete = name


    status_delete = property(get_status_delete, set_status_delete)


    def get_king(self):
        return self._king


    def set_king(self, y):

        if self._king == False:
            if self._name == self.__gamer_two and y == self._n_min:
                self._king = True
            elif self._name == self.__gamer_one and y == self._n_max:
                self._king = True


    king = property(get_king, set_king)


    def get_permitted(self):

        try:
            output = self._permitted
        except AttributeError:
            output = []

        return output


    def set_permitted(self, permitted_list):
        """
        This is a function defenites permitted list of move, fight and soft fight (king fight)
        :param self: self is Checker object
        :param permitted_list: permitted_list is the permitted list from game map disposition
        :type self: object of checkers
        :type permitted_list: list
        """
        inpermitted_list = [(row[0], row[1], row[3]) for row in permitted_list]

        in_x = []
        in_y = []
        in_y_fight = []

        # movement and fighting rules for checker
        if self._x == self._n_max:
            in_x.append(self._x - self._n_delta)
        elif self._x == self._n_min:
            in_x.append(self._x + self._n_delta)
        else:
            in_x.append(self._x - self._n_delta)
            in_x.append(self._x + self._n_delta)

        if self._y == self._n_max:
            in_y_fight.append(self._y - self._n_delta)
            if self._name == self.__gamer_two:
                in_y.append(self._y - self._n_delta)
        elif self._y == self._n_min:
            in_y_fight.append(self._y + self._n_delta)
            if self._name == self.__gamer_one:
                in_y.append(self._y + self._n_delta)
        else:
            in_y_fight.append(self._y + self._n_delta)
            in_y_fight.append(self._y - self._n_delta)
            if self._name == self.__gamer_one:
                in_y.append(self._y + self._n_delta)
            elif self._name == self.__gamer_two:
                in_y.append(self._y - self._n_delta)

        self._permitted = []

        for i in in_x:
            for j in in_y:
                if (i, j, self.__field) in inpermitted_list:
                    self._permitted.append((i, j))

        self._permitted_king = []
        self._permitted_soft = []

        if self._king is True:
            self.__king_rules(1, 1, inpermitted_list, range(self._n_max - self._x))
            self.__king_rules(1, -1, inpermitted_list, range(self._n_max - self._x))
            self.__king_rules(-1, 1, inpermitted_list, range(self._x - self._n_min))
            self.__king_rules(-1, -1, inpermitted_list, range(self._x - self._n_min))

        for row in self._permitted_king:
            if row[0] == self.__field:
                self._permitted.append((row[1], row[2]))

        self._permitted_fight = []

        for i in in_x:
            for j in in_y_fight:
                if (i, j, self.__block) in inpermitted_list:
                    result = self.__proove_fight(i, j, inpermitted_list)
                    if result:
                        self._permitted_fight.append((i, j, *result))


    permitted = property(get_permitted, set_permitted)


    @property
    def name(self):
        return self._name


    @property
    def permitted_soft(self):

        try:
            output = self._permitted_soft
        except AttributeError:
            output = []

        return output

    @property
    def permitted_fight(self):

        try:
            output = self._permitted_fight
        except AttributeError:
            output = []

        return output

    @property
    def permitted_fight_coord(self):

        _list_coord = []

        try:
            output = self._permitted_fight
            for row in output:
                _x, _y, _x_new, _y_new = row
                _list_coord.append((_x, _y))
        except AttributeError:
            print('Error. No coords for fighing after')

        return _list_coord


    def __king_rules(self, i, j, inpermitted_list, _range):

        _x = self._x
        _y = self._y
        _b = 1
        _c = False

        for _ in _range:
            if _b != 3:
                _x += i
                _y += j

                if self._n_min <= _y <= self._n_max and self._n_min <= _x <= self._n_max:
                    if (_x, _y, self.__field) in inpermitted_list:
                        if _b == 2 or _c:
                            _c = True
                            self._permitted_soft.append((_x, _y))

                        self._permitted_king.append((self.__field, _x, _y))
                        _b = 1
                    elif (_x, _y, self.__block) in inpermitted_list and _b == 1:
                        _b = 2
                    elif (_x, _y, self.__block) in inpermitted_list and _b == 1:
                        _b = 3
                    else:
                        _b = 3


    def __proove_fight(self, i, j, inpermitted_list):

        output = ()

        if self._x > i:
            i -= self._n_delta
        else:
            i += self._n_delta

        if self._y > j:
            j -= self._n_delta
        else:
            j += self._n_delta

        if (self._n_min <= i <= self._n_max) and (self._n_min <= j <= self._n_max) and ((i, j, self.__field) in inpermitted_list):
            output = i, j

        return output