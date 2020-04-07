import gameobjects as game_object
from random import randint, choice
from characters import CHARACTERS, ENEMIES
from gamemap import GameMap


def get_trapped(character):
    """
    This is a function witch trapped effect.
    :param character: Char character
    :type character: object
    """
    print('You get trapped')
    damage = randint(5, 25)
    character.get_damaged(damage)


def get_healed(character):
    """
    This is a function witch healed effect.
    :param character: Char character
    :type character: object
    """
    print('You get healed')
    hp = randint(5, 25)
    character.get_healed(hp)


def fight_with_enemy(character, enemy):
    """
    This is a function witch enemy effect.
    :param character: Char character
    :type character: object
    :param enemy: Enemy character
    :type enemy: object
    :return: return flag of fighting result
    :rtype: boolean
    """
    is_won = True

    while True:

        character.fight(enemy)

        if character.is_dead():
            is_won = False
            break
        elif enemy.is_dead():
            break

    return is_won

print('Welcome to my game!')
name = input('Enter your name: ')

while True:

    race = input('Choose race [Human, Orc, Elf]: ')

    if race in ['Human', 'Orc', 'Elf']:
        break

while True:

    level = input('Difficulty [Hard, Medium, Easy]: ')

    if level in ['Hard', 'Medium', 'Easy', 'Test']:
        break

while True:

    rank = int(input('N*N map. Enter "N". Max 10: '))

    if 10 >= rank > 0:
        break

objects = []
objects.append(game_object.Door())

if level == 'Hard':
    objects += [game_object.Trap() for i in range(4)]
    objects += [choice(ENEMIES)() for i in range(5)]
elif level == 'Medium':
    objects += [game_object.Trap() for i in range(3)]
    objects += [choice(ENEMIES)() for i in range(4)]
elif level == 'Easy':
    objects += [game_object.Trap() for i in range(2)]
    objects += [choice(ENEMIES)() for i in range(3)]

objects.append(game_object.Heal())

char = CHARACTERS[race](name)
char.show_stats()

game_map = GameMap(rank, rank, objects, char)
x, y = game_map.char_coords()
char.set_coords(x, y)

while True:

    char_permitted = game_map.char_permitted()
    print(game_map)
    move = input(f'Move? {str(char_permitted)} ')

    if move in char_permitted:

        game_map.clean_grid(x, y)
        x, y = char.move(move)
        effect = game_map.get_map_effect(x, y)

        if isinstance(effect, game_object.Trap):
            print('TRAP!!!')
            get_trapped(char)

            if char.is_dead():
                break

        elif isinstance(effect, game_object.Heal):
            print('HEAL!!!')
            get_healed(char)

        elif isinstance(effect, game_object.Door):
            print('You WIN!!! Congratulation!')
            break

        elif isinstance(effect, (ENEMIES[0], ENEMIES[1])):
            print('ENEMY!!!')
            enemy = effect
            is_won = fight_with_enemy(char, enemy)

            if not is_won:
                print(f'Sorry, you lost.')
                break

        else:
            print('STEP')

        game_map.put_char(char, *char.get_coords())
    else:
        print('Enter one of permitted moves [u - up, d - down, l - left, r - right]')

game_map.put_char(char, *char.get_coords())
print(game_map)
print(f'Game over')