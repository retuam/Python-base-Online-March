class Trap:

    def __str__(self):
        return '*'

    def obj_type(self):
        return 'trap'

class Heal:

    def __str__(self):
        return '*'

    def obj_type(self):
        return 'heal'


GAME_OBJECTS = [Trap, Heal]
