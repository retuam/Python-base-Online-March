class GameMap:

    def __init__(self, rank, objects):

        self.__n = rank
        self.__x_names = 'abcdefgh'
        self.__y_names = '12345678'
        self.__gamer_one = 'white'
        self.__gamer_two = 'black'
        self.__field = 'field'
        self.__block = 'block'
        self.__friend = 'friend'
        # generate 2d map
        self._generate_map()
        # resolve permitted moves by default
        self.set_permitted_moves(objects)
        # put the objects on map
        self._put_objects(objects)


    def __str__(self):
        return self._show_map()


    def get_object(self, n, m):
        return self._map[m][n]


    def set_object(self, obj, x, y):
        self._map[y][x] = obj


    def get_line_y(self):
        return self.__y_names


    def get_line_x(self):
        return self.__x_names


    def get_coordinate(self, x_names, y_names):

        list_x = list(self.__x_names)
        list_y = list(self.__y_names)

        if (x_names in list_x) and (y_names in list_y):
            return list_x.index(x_names), list_y.index(y_names)


    def get_name_cell(self, x, y):

        cell_name = str(self.__x_names[x]) + str(self.__y_names[y])

        return cell_name


    def delete_object(self, n, m):
        self._map[m][n] = ' '


    def get_permitted_moves(self, type):
        return self._permitted[type]


    def set_permitted_moves(self, objects):
        """
        This is a function to resolve permitted moves for game map
        :param self: self is GameMap object
        :param objects: list of checkers
        :type self: object
        :type objects: list
        """
        self._permitted = {self.__gamer_one: [row for row in self.__default_permitted],
                           self.__gamer_two: [row for row in self.__default_permitted]}

        for obj in objects:

            try:
                y, x = obj.get_coords()
                cell_number = str(self.__x_names[y]) + str(self.__y_names[x])
            except AttributeError:
                print('Object od checker hasn\'t get_coords attributes.')

            try:
                self._permitted[self.__gamer_one].remove((y, x, cell_number, self.__field))
                self._permitted[self.__gamer_two].remove((y, x, cell_number, self.__field))
            except ValueError:
                print('Coordinates for checkers is false!')
            except UnboundLocalError:
                print('Local variables x, y referenced before assignment')

            try:
                if obj.name == self.__gamer_one:
                    self._permitted[self.__gamer_two].append((y, x, cell_number, self.__block))
                    self._permitted[self.__gamer_one].append((y, x, cell_number, self.__friend))
                elif obj.name == self.__gamer_two:
                    self._permitted[self.__gamer_one].append((y, x, cell_number, self.__block))
                    self._permitted[self.__gamer_two].append((y, x, cell_number, self.__friend))
            except UnboundLocalError:
                print('Local variables name, x, y referenced before assignment')


    def delete_on_diagonal(self, old_coord, new_coord):
        """
        This is a function delete enemy checrs after king move
        :param old_coord: start coordinates (x, y) of king
        :param new_coord: end coordinates (x, y) of king
        :type old_coord: list
        :type new_coord: list
        """
        i = 1
        status_fight = False

        _range = range(old_coord[0] - new_coord[0])

        if old_coord[0] > new_coord[0]:
            i = -1
        else:
            _range = range(new_coord[0] - old_coord[0])

        j = 1
        if old_coord[1] > new_coord[1]:
            j = -1

        _x = old_coord[0]
        _y = old_coord[1]

        for _ in _range:
            _x += i
            _y += j

            if (0 <= _y <= (self.__n - 1)) and (0 <= _x <= (self.__n - 1)):
                obj = self.get_object(_x, _y)
                if obj != ' ':
                    try:
                        obj.status_delete = True
                        self.delete_object(_x, _y)
                    except AttributeError:
                        print('Object od checker hasn\'t set_status_delete attributes.')

                    status_fight = True

        return status_fight


    def _generate_map(self):

        self._map = []
        self.__default_permitted = []

        for i in range(self.__n):

            row = []

            for j in range(self.__n):

                if (i + j) % 2:
                    cell_number = str(self.__x_names[i]) + str(self.__y_names[j])
                    self.__default_permitted.append((i, j, cell_number, self.__field))

                row.append(' ')

            self._map.append(row)


    def _put_objects(self, objects):
        """
        This is a function to put object on map
        :param self: self is GameMap object
        :param objects: list of checkers
        :type self: object GameMap
        :type objects: list
        """
        for obj in objects:

            try:
                y, x = obj.get_coords()
                cell_number = str(self.__x_names[y]) + str(self.__y_names[x])
                self._map[x][y] = obj
                obj.set_cell_number(cell_number)

            except AttributeError:
                print('Object od checker hasn\'t get_coords attributes.')


    def _show_map(self):

        game_map = []

        game_map += self._show_x_names()
        game_map.append('\n\n')

        j = 0

        for row in self._map:

            j += 1
            game_map.append(str(j))
            game_map.append(' |')

            for i in row:
                game_map.append(f'{str(i)}|')

            game_map.append(' ')
            game_map.append(str(j))
            game_map.append('\n')

        game_map.pop()

        game_map.append('\n\n')
        game_map += self._show_x_names()

        return ''.join(game_map)


    def _show_x_names(self):

        line_x = []
        line_x .append('   ')
        line_x += [(i.upper() + ' ') for i in list(self.__x_names)]

        return line_x