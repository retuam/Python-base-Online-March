from random import randint, choice
from characters import CHARACTERS ,ENEMIES
from game_objects import GAME_OBJECTS, EXIT_DOOR
from game_map import GameMap


def get_trapped(character):
    print('You got trapped')
    damage = randint(5 ,25)
    character.get_damaged(damage)


def get_healed(character):
    print('You got healed')
    hp = randint(5 ,25)
    character.get_healed(hp)


def fight_with_enemy(character ,enemy):
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
race = input('Choose race [Human, Orc, Elf]: ')
level = input('Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard':
    objects = [ choice(GAME_OBJECTS)() for i in range(4) ]
    enemies = [ choice(ENEMIES)() for i in range(3) ]
    objects += [choice(EXIT_DOOR)() for i in range(1)]
elif level == 'Medium':
    objects = [choice(GAME_OBJECTS)() for i in range(3)]
    enemies = [choice(ENEMIES)() for i in range(2)]
    objects += [choice(EXIT_DOOR)() for i in range(1)]
elif level == 'Easy':
    objects = [choice(GAME_OBJECTS)() for i in range(3)]
    enemies = [choice(ENEMIES)() for i in range(1)]
    objects += [choice(EXIT_DOOR)() for i in range(2)]


x, y = randint(0, 4), randint(0, 4)
char = CHARACTERS[race](name, x, y)
char.show_stats()

game_map = GameMap(5, 5, objects)
game_map.put_char(char, *char.give_coords())


while True:

    print(game_map)


    move_diraction = input("Choose the way you go (L,R,D,U or stop): ")

    if move_diraction == "u":
         move = (-1, 0)
    elif move_diraction == "d":
        move = (1, 0)
    elif move_diraction == "l":
        move = (0, -1)
    elif move_diraction == "r":
        move = (0, 1)
    elif move_diraction == "stop":
        break

    cur_pos = char.give_coords()
    next_pos = tuple(map(lambda a, b: a + b, cur_pos, move))


    for element in objects:
        if element.respond()[0] == next_pos:
            situation = element.respond()[1]
        else: situation = ''

        if situation == 'Heal':
            get_healed(char)

        elif situation == 'Trap':
            get_trapped(char)
            if char.is_dead():
                print('Sorry, you lost.')
                print('Game Over')
                break
        elif situation == 'Undead' or situation == 'Murloc':
            print (' \nENEMY ! ! !')
            is_won = fight_with_enemy(char, element)
            if not is_won:
                print('\nSorry, you lost.')
                print('\nGame Over')
                break
        elif situation == 'Exit_door':
            print("\nYou won! " )
            break

    char.is_moving(move)
    new_pos = char.give_coords()
    game_map.is_moving(char, *cur_pos, *new_pos)




