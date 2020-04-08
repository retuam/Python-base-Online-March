class Character:

    _initial_hp = 100

    def __init__(self, name):

        self._name = name
        self._assign_stats()
        self._is_dead = False


    def __str__(self):
        return 'X'


    def _assign_stats(self):

        self._hp = 100
        self._damage = 10
        self._race = None


    def get_coords(self):
        return self._x, self._y

    def move(self, type):
        """
        This is a function for change Char coordinates after move.
        :param type: Direction of movement
        :type type: str
        :return: return new coordinates x, y of Char
        :rtype: tuple
        """
        if type == 'u':
            self._y -= 1
        elif type == 'd':
            self._y += 1
        elif type == 'r':
            self._x += 1
        elif type == 'l':
            self._x -= 1

        return self._x, self._y

    def set_coords(self, x, y):
        """
        This is a function for set Char coordinates.
        :param x: X - coordinate
        :type x: int
        :param y: Y - coordinate
        :type y: int
        """
        self._x = x
        self._y = y


    def show_stats(self):

        print('Character stats: ')
        print(f'Name: {self._name}')
        print(f'HP: {self._hp}')
        print(f'Damage: {self._damage}')
        print(f'Race: {self._race}')


    def get_damaged(self, damage):

        print(f'  {self._name} get damaged by {damage}')
        self._hp -= damage

        if self._hp <= 0:
            print(f'  {self._name} is dead')
            self._is_dead = True

        else:
            print(f'  {self._hp} left')


    def get_healed(self, hp):

        print(f'  {self._name} get healed by {hp}')

        approximate_hp = self._hp + hp

        if approximate_hp >= self._initial_hp:
            self._hp = self._initial_hp
        else:
            self._hp = approximate_hp

        print(f'  {self._hp} left')


    def damage(self):
        return self._damage


    def fight(self, other):

        self.get_damaged(other.damage())

        if not self._is_dead:
            other.get_damaged(self.damage())


    def is_dead(self):
        return self._is_dead


class Human(Character):

    _initial_hp = 100

    def _assign_stats(self):
        self._hp = self._initial_hp
        self._damage = 10
        self._race = 'Human'


class Orc(Character):

    _initial_hp = 120

    def _assign_stats(self):
        self._hp = self._initial_hp
        self._damage = 15
        self._race = 'Orc'


class Elf(Character):

    _initial_hp = 90

    def _assign_stats(self):
        self._hp = self._initial_hp
        self._damage = 20
        self._race = 'Elf'


class Enemy(Character):

    _initial_hp = 30

    def __init__(self):
        self._assign_stats()
        self._is_dead = False


    def __str__(self):
        return '*'


    def _assign_stats(self):
        self._hp = 100
        self._damage = 10
        self._name = None


    def show_stats(self):
        print('Enemy stats: ')
        print(f'HP: {self._hp}')
        print(f'Damage: {self._damage}')
        print(f'Type: {self._name}')


class Undead(Enemy):

    _initial_hp = 30

    def _assign_stats(self):
        self._hp = self._initial_hp
        self._damage = 10
        self._name = 'Undead'


class Murloc(Enemy):

    _initial_hp = 15

    def _assign_stats(self):
        self._hp = self._initial_hp
        self._damage = 5
        self._name = 'Murloc'


CHARACTERS = {'Human': Human, 'Orc': Orc, 'Elf': Elf}
ENEMIES = [Undead, Murloc]