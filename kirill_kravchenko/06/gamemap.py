from random import sample


class GameMap:

    def __init__(self, n, m, objects, char):

        self._n = n
        self._m = m
        self._map = self._generate_map()
        self._put_objects(objects, char)


    def __str__(self):
        return self._show_map()


    def _generate_map(self):

        self._shuffle = []

        i = 0
        for _ in range(self._n):
            for _ in range(self._m):
                self._shuffle.append(i)
                i += 1

        return [[' ' for _ in range(self._n)] for _ in range(self._m)]


    def _put_objects(self, objects, char):
        """
        This is a function for put game objects on map. If map size smaller than length of object list plus 1,
        take Door object and put it after other objects have been putted on map. Type of randomizing is <sample>-func
        :param objects: Game object
        :type objects: object
        :param char: Char object
        :type char: object
        """
        length = len(objects) + 1
        len_shuffle = len(self._shuffle)

        if length > len_shuffle:
            length = len_shuffle
            objects = objects[0:len_shuffle - 1]

        object_sample = sample(self._shuffle, k=length)

        i = 0
        for obj in objects:
            x, y = self.__cell_object(object_sample[i])
            self._map[x][y] = obj
            i += 1

        self.put_char(char, *self.__cell_object(object_sample[i]))


    def __cell_object(self, index):
        return index % self._n, index // self._m


    def _show_map(self):

        game_map = []

        for row in self._map:

            game_map.append('|')

            for i in row:
                game_map.append(f'{str(i)}|')

            game_map.append('\n')

        game_map.pop()

        return ''.join(game_map)


    def clean_grid(self, n, m):
        self._map[m][n] = ' '


    def get_map_effect(self, n, m):
        return self._map[m][n]


    def put_char(self, char, x, y):
        """
        This is a function for put char on map and execute permitted types of movement for futher step
        :param char: Char object
        :type char: object
        :param x: X - coordinate
        :type x: int
        :param y: Y - coordinate
        :type y: int
        """
        self._n_char = x
        self._m_char = y

        self._permitted_array = []

        if self._n_char < self._n - 1:
            self._permitted_array.append('r')

        if self._n_char > 0:
            self._permitted_array.append('l')

        if self._m_char < self._m - 1:
            self._permitted_array.append('d')

        if self._m_char > 0:
            self._permitted_array.append('u')

        self._map[self._m_char][self._n_char] = str(char)


    def char_permitted(self):
        return self._permitted_array


    def char_coords(self):
        return self._n_char, self._m_char