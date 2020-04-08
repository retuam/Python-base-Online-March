class Trap:

    def __init__(self):
        self._name = 'Trap'

    def __str__(self):
        return '*'

    def get_coords(self, x, y):

        self._x = x
        self._y = y

    def respond(self):
        resp = [(self._x, self._y), self._name]
        return resp

    def give_coords(self):

        return self._x, self._y

class Heal:

    def __init__(self):
        self._name = 'Heal'

    def __str__(self):
        return '*'


    def get_coords(self, x, y):

        self._x = x
        self._y = y


    def give_coords(self):

        return self._x, self._y

    def respond(self):
        resp = [(self._x, self._y), self._name]
        return resp

class Exit_door:

    def __init__(self):
        self._name = 'Exit_door'

    def __str__(self):
        return '*'

    def get_coords(self, x, y):

        self._x = x
        self._y = y


    def give_coords(self):

        return self._x, self._y


    def respond(self):
        resp = [(self._x, self._y), self._name]
        return resp

GAME_OBJECTS = [Trap, Heal]
EXIT_DOOR = [Exit_door]