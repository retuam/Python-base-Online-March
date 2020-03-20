from random import randint

player_choice = 0
level_choice = 0

cards_first_player = 0
cards_second_player = 0
cards_third_player = 0

card_a = randint(2, 11)
card_b = randint(2, 11)

hand_first_player = card_a + card_b
hand_second_player = card_a + card_b
hand_third_player = card_a + card_b

print("Let's play")
print('Please, choose level of the Game! 1/2/3')

level_choice = int(input())
'''
    if level_choice != '1' and level_choice != '2' and level_choice != '3':
        print('You have make a typo! Please, choose level of the Game! 1/2/3')
'''


if level_choice == 1:
    while True:
        cards_first_player = input('pull a cards')
        if hand_first_player > 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You lose! Your hand is more then 21', hand_first_player)
            break
        elif hand_first_player == 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You win! You got 21')
            break
        elif 18 < hand_first_player < 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('Your hand is', hand_first_player)
            break
        else:
            while hand_first_player <= 18:
                print('the first card is', card_a, 'the second card is', card_b)
                print('Try one more card! The sum of your cards as of now is', hand_first_player, 'So, what is your choice? Yes or No')
                player_choice = input()
                if player_choice == 'yes':
                    hand_first_player += randint(2, 11)
                    if hand_first_player > 21:
                        print('You lose! Your hand is more then 21', hand_first_player)
                        break
                    elif hand_first_player == 21:
                        print('You win!You got 21')
                        break
                    elif 18 < hand_first_player < 21:
                        print('Your hand is', hand_first_player)
                        break
                else:
                    print('You folded!')
                    break
            break
    print('The game is over!')


elif level_choice == 2:
    cards_first_player = input('pull a cards, Player 1')
    while True:
        if hand_first_player > 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You lose! Your hand is more then 21', hand_first_player)
            break
        elif hand_first_player == 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You got 21')
            break
        elif 18 < hand_first_player < 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('Your hand is', hand_first_player)
            break
        else:
            while hand_first_player <= 18:
                print('the first card is', card_a, 'the second card is', card_b)
                print('Try one more card! The sum of your cards as of now is', hand_first_player, 'So, what is your choice? Yes or No')
                player_choice = input()
                if player_choice == 'yes':
                    hand_first_player += randint(2, 11)
                    if hand_first_player > 21:
                        print('You lose! Your hand is more then 21', hand_first_player)
                        break
                    elif hand_first_player == 21:
                        print('You got 21')
                        break
                    elif 18 < hand_first_player < 21:
                        print('Your hand is', hand_first_player)
                        break
                else:
                    print('You folded!')
                    break
            break
    cards_second_player = input('pull a cards, Player 2')
    while True:
        if hand_second_player > 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You lose! Your hand is more then 21', hand_second_player)
            break
        elif hand_second_player == 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You got 21')
            break
        elif 18 < hand_second_player < 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('Your hand is', hand_second_player)
            break
        else:
            while hand_second_player <= 18:
                print('the first card is', card_a, 'the second card is', card_b)
                print('Try one more card! The sum of your cards as of now is', hand_second_player, 'So, what is your choice? Yes or No')
                player_choice = input()
                if player_choice == 'yes':
                    hand_second_player += randint(2, 11)
                    if hand_second_player > 21:
                        print('You lose! Your hand is more then 21', hand_second_player)
                        break
                    elif hand_second_player == 21:
                        print('You got 21')
                        break
                    elif 18 < hand_second_player < 21:
                        print('Your hand is', hand_second_player)
                        break
                else:
                    print('You folded!')
                    break
            break
    if hand_second_player < hand_first_player <= 21:
        print('First player is a winner!')
    elif hand_first_player < hand_second_player <= 21:
        print('Second player is a winner!')
    elif hand_first_player == hand_second_player:
        print('Draw!')
    print('The game is over!')


elif level_choice == 3:
    cards_first_player = input('pull a cards, Player 1')
    while True:
        if hand_first_player > 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You lose! Your hand is more then 21', hand_first_player)
            break
        elif hand_first_player == 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You got 21')
            break
        elif 18 < hand_first_player < 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('Your hand is', hand_first_player)
            break
        else:
            while hand_first_player <= 18:
                print('the first card is', card_a, 'the second card is', card_b)
                print('Try one more card! The sum of your cards as of now is', hand_first_player, 'So, what is your choice? Yes or No')
                player_choice = input()
                if player_choice == 'yes':
                    hand_first_player += randint(2, 11)
                    if hand_first_player > 21:
                        print('You lose! Your hand is more then 21', hand_first_player)
                        break
                    elif hand_first_player == 21:
                        print('You got 21')
                        break
                    elif 18 < hand_first_player < 21:
                        print('Your hand is', hand_first_player)
                        break
                else:
                    print('You folded!')
                    break
            break
    cards_second_player = input('pull a cards, Player 2')
    while True:
        if hand_second_player > 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You lose! Your hand is more then 21', hand_second_player)
            break
        elif hand_second_player == 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You got 21')
            break
        elif 18 < hand_second_player < 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('Your hand is', hand_second_player)
            break
        else:
            while hand_second_player <= 18:
                print('the first card is', card_a, 'the second card is', card_b)
                print('Try one more card! The sum of your cards as of now is', hand_second_player, 'So, what is your choice? Yes or No')
                player_choice = input()
                if player_choice == 'yes':
                    hand_second_player += randint(2, 11)
                    if hand_second_player > 21:
                        print('You lose! Your hand is more then 21', hand_second_player)
                        break
                    elif hand_second_player == 21:
                        print('You got 21')
                        break
                    elif 18 < hand_second_player < 21:
                        print('Your hand is', hand_second_player)
                        break
                else:
                    print('You folded!')
                    break
            break
    cards_second_player = input('pull a cards, Player 3')
    while True:
        if hand_third_player > 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You lose! Your hand is more then 21', hand_third_player)
            break
        elif hand_third_player == 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('You got 21')
            break
        elif 18 < hand_third_player < 21:
            print('the first card is', card_a, 'the second card is', card_b)
            print('Your hand is', hand_third_player)
            break
        else:
            while hand_third_player <= 18:
                print('the first card is', card_a, 'the second card is', card_b)
                print('Try one more card! The sum of your cards as of now is', hand_third_player,
                      'So, what is your choice? Yes or No')
                player_choice = input()
                if player_choice == 'yes':
                    hand_third_player += randint(2, 11)
                    if hand_third_player > 21:
                        print('You lose! Your hand is more then 21', hand_third_player)
                        break
                    elif hand_third_player == 21:
                        print('You got 21')
                        break
                    elif 18 < hand_third_player < 21:
                        print('Your hand is', hand_third_player)
                        break
                else:
                    print('You folded!')
                    break
            break
    if hand_second_player < hand_first_player > hand_third_player and hand_first_player <= 21:
        print('First player is a winner!')
    elif hand_first_player < hand_second_player > hand_third_player and hand_second_player <= 21:
        print('Second player is a winner!')
    elif hand_first_player < hand_third_player > hand_second_player and hand_third_player <= 21:
        print('Second player is a winner!')
    elif hand_first_player == hand_second_player == hand_third_player:
        print('Draw!')
    print('The game is over!')
