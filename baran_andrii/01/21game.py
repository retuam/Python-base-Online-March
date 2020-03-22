from random import randint

print('\n\n\t\t21 GAME \n\n\n')
game = 1
while game == 1:
    print('SELECT MODE\n')
    print('1 - Player')
    print('2 - Player and bot')
    print('3 - Player and two bots\n')
    mode = input('MODE: ')
    if mode != '1' and mode != '2' and mode != '3':
        mode = input('PLEASE TYPE VALID MODE TYPE: 1, 2 or 3. MODE: ')

    if mode == '1':
        print('\n\n\t\tMODE "1" SELECTED \n\n')
        move = 1
        while move:
            print('Player move ....\n')
            card_1 = randint(2, 11)
            card_2 = randint(2, 11)
            card_sum = card_1 + card_2
            pick = 0
            print(f'First card - {card_1}')
            print(f'Second card - {card_2}')
            print(f'Points - {card_sum}')

            if card_sum == 21:
                print('\n\n\t\tYou got 21 points. YOU WIN!\n\n')
                move = 0
                try_again = input('Try again? y/n')
                if try_again == 'y':
                    move = 1
                if try_again == 'n' or not try_again:
                    move = 0
                    pick = 0
                    break
            if card_sum > 21:
                print('\n\n\t\tYou got more than 21 points. You loose\n\n')
                card_sum = 0
                move = 0

            if card_sum == 22 and card_1 == 11 and card_2 == 11:
                print('\n\n\t\tYou got double ace! 22 Points. YOU WIN\n\n')
                move = 0

            if card_sum < 21:
                pick = 1

            while pick:
                next_card = input('Next card? y/n ')
                if next_card == 'y':
                    c = randint(2, 11)
                    card_sum += c
                    print(f'Your next card {c}')
                    print(f'Points - {card_sum}')
                if next_card == 'n':
                    pick = 0
                    print(f'Your score is {card_sum}')

                if card_sum == 21:
                    print('\n\n\t\tYou got 21 points.\n\n')
                    pick = 0

                if card_sum > 21:
                    print('\n\n\t\tYou got more than 21 points. You loose\n\n')
                    card_sum = 0
                    pick = 0

                if card_1 == 11 and card_2 == 11:
                    print('\n\n\t\tYou got double ace! 22 Points\n\n')
                    pick = 0

            if pick == 0:
                move = 0
                try_again = input('Try again? y/n ')
                if try_again == 'y':
                    move = 1
                if try_again == 'n' or not try_again:
                    pick = 0
                    break
        if move == 0:
            break
        game = 0
    if mode == '2':
        print('\n\n\t\tMODE "2" SELECTED \n\n')
        
        user_move = 1
        user_points = 0

        player_move = 1
        while player_move:
            print('Player move ....\n')
            card_1 = randint(2, 11)
            card_2 = randint(2, 11)
            card_sum = card_1 + card_2
            pick = 0
            print(f'First card - {card_1}')
            print(f'Second card - {card_2}')
            print(f'Points - {card_sum}')

            if card_sum == 21:
                print('\n\n\t\tYou got 21 points\n\n')
                user_points = card_sum

            if card_sum > 21:
                print('\n\n\t\tYou got more than 21 points. You loose\n\n')
                card_sum = 0
                player_move = 0
                user_points = card_sum

            if card_sum == 22 and card_1 == 11 and card_2 == 11:
                print('\n\n\t\tYou got double ace! 22 Points. YOU WIN\n\n')
                player_move = 0
                user_points = card_sum

            if card_sum < 21:
                pick = 1

            while pick:
                next_card = input('Next card? y/n ')
                if next_card == 'y':
                    c = randint(2, 11)
                    card_sum += c
                    print(f'Your next card {c}')
                    print(f'Points - {card_sum}')
                    user_points = card_sum
                if next_card == 'n':
                    pick = 0
                    player_move = 0
                    user_points = card_sum

                if card_sum == 21:
                    print('\n\n\t\tYou got 21 points.\n\n')
                    pick = 0
                    player_move = 0
                    user_points = card_sum

                if card_sum > 21:
                    print('\n\n\t\tYou got more than 21 points. You loose\n\n')
                    card_sum = 0
                    pick = 0
                    player_move = 0
                    user_points = 0
                if card_1 == 11 and card_2 == 11:
                    print('\n\n\t\tYou got double ace! 22 Points\n\n')
                    pick = 0
                    player_move = 0
                    user_points = card_sum

        if player_move == 0:
            print('Player finished the move\n\n\n')

        bot_move = 1
        bot_points = 0
        while bot_move:
            print('Bot move ....\n')
            bot_card_1 = randint(2, 11)
            bot_card_2 = randint(2, 11)
            bot_card_sum = bot_card_1 + bot_card_2
            pick = 0
            print(f'BOT First card - {bot_card_1}')
            print(f'BOT Second card - {bot_card_2}')
            print(f'BOT Points - {bot_card_sum}')

            if bot_card_sum == 21:
                print('\n\n\t\tYou got 21 points. YOU WIN!\n\n')
                bot_points = bot_card_sum
                bot_move = 0

            if bot_card_sum > 21:
                print('\n\n\t\tBOT got more than 21 points. BOT loose\n\n')
                bot_card_sum = 0
                bot_move = 0
                bot_points = bot_card_sum

            if bot_card_sum == 22 and bot_card_1 == 11 and bot_card_2 == 11:
                print('\n\n\t\tBOT got double ace! 22 Points.\n\n')
                bot_move = 0
                bot_points = bot_card_sum

            if bot_card_sum < 21:
                pick = 1

            while pick:
                c = randint(2, 11)
                bot_card_sum += c
                print(f'BOT next card {c}')
                print(f'BOT Points {bot_card_sum}')
                if bot_card_sum == 21:
                    print('\n\n\t\tBOT got 21 points.\n\n')
                    pick = 0
                    bot_points = bot_card_sum

                if bot_card_sum > 21:
                    print('\n\n\t\tBOT got more than 21 points. BOT loose\n\n')
                    bot_card_sum = 0
                    pick = 0
                    bot_points = bot_card_sum

                if bot_card_1 == 11 and bot_card_2 == 11:
                    print('\n\n\t\tBOT got double ace! 22 Points\n\n')
                    pick = 0
                    bot_points = bot_card_sum
                if bot_card_sum >= 18:
                    bot_points = bot_card_sum
                    pick = 0

            if pick == 0:
                bot_move = 0

        print('\n\n\t\t\t\tTOTAL SCORE\n')
        print(f'\t\tUSER: {user_points}')
        print(f'\t\tBOT: {bot_points}')

        if bot_points > user_points:
            print('\n\n\n\t\tBOT WINS')

        if bot_points < user_points:
            print('\n\n\n\t\tPLAYER WINS')

        if bot_points == user_points:
            print('\n\n\n\t\tEqual')
        game = 0

    if mode == '3':
        print('\n\n\t\tMODE "3" SELECTED \n\n')
        
        user_move = 1
        user_points = 0

        player_move = 1
        while player_move:
            print('Player move ....\n')
            card_1 = randint(2, 11)
            card_2 = randint(2, 11)
            card_sum = card_1 + card_2
            pick = 0
            print(f'First card - {card_1}')
            print(f'Second card - {card_2}')
            print(f'Points - {card_sum}')

            if card_sum == 21:
                print('\n\n\t\tYou got 21 points\n\n')
                user_points = card_sum

            if card_sum > 21:
                print('\n\n\t\tYou got more than 21 points. You loose\n\n')
                card_sum = 0
                player_move = 0
                user_points = card_sum

            if card_sum == 22 and card_1 == 11 and card_2 == 11:
                print('\n\n\t\tYou got double ace! 22 Points. YOU WIN\n\n')
                player_move = 0
                user_points = card_sum

            if card_sum < 21:
                pick = 1

            while pick:
                next_card = input('Next card? y/n ')
                if next_card == 'y':
                    c = randint(2, 11)
                    card_sum += c
                    print(f'Your next card {c}')
                    print(f'Points - {card_sum}')
                    user_points = card_sum
                if next_card == 'n':
                    pick = 0
                    player_move = 0
                    user_points = card_sum

                if card_sum == 21:
                    print('\n\n\t\tYou got 21 points.\n\n')
                    pick = 0
                    player_move = 0
                    user_points = card_sum

                if card_sum > 21:
                    print('\n\n\t\tYou got more than 21 points. You loose\n\n')
                    card_sum = 0
                    pick = 0
                    player_move = 0
                    user_points = 0
                if card_1 == 11 and card_2 == 11:
                    print('\n\n\t\tYou got double ace! 22 Points\n\n')
                    pick = 0
                    player_move = 0
                    user_points = card_sum

        if player_move == 0:
            print('Player finished the move\n\n\n')

        bot1_move = 1
        bot1_points = 0
        while bot1_move:
            print('BOT1 move ....\n')
            bot1_card_1 = randint(2, 11)
            bot1_card_2 = randint(2, 11)
            bot1_card_sum = bot1_card_1 + bot1_card_2
            pick = 0
            print(f'BOT First card - {bot1_card_1}')
            print(f'BOT Second card - {bot1_card_2}')
            print(f'BOT Points - {bot1_card_sum}')

            if bot1_card_sum == 21:
                print('\n\n\t\tBOT1 got 21 points.\n\n')
                bot1_points = bot1_card_sum
                bot1_move = 0

            if bot1_card_sum > 21:
                print('\n\n\t\tBOT1 got more than 21 points. BOT loose\n\n')
                bot1_card_sum = 0
                bot1_move = 0
                bot1_points = bot1_card_sum

            if bot1_card_sum == 22 and bot1_card_1 == 11 and bot1_card_2 == 11:
                print('\n\n\t\tBOT1 got double ace! 22 Points.\n\n')
                bot1_move = 0
                bot1_points = bot1_card_sum

            if bot1_card_sum < 21:
                pick = 1

            while pick:
                c = randint(2, 11)
                bot1_card_sum += c
                print(f'BOT1 next card {c}')
                print(f'BOT1 Points {bot1_card_sum}')
                if bot1_card_sum == 21:
                    print('\n\n\t\tBOT1 got 21 points.\n\n')
                    pick = 0
                    bot1_points = bot1_card_sum

                if bot1_card_sum > 21:
                    print('\n\n\t\tBOT1 got more than 21 points. BOT1 loose\n\n')
                    bot1_card_sum = 0
                    pick = 0
                    bot1_points = bot1_card_sum

                if bot1_card_1 == 11 and bot1_card_2 == 11:
                    print('\n\n\t\tBOT1 got double ace! 22 Points\n\n')
                    pick = 0
                    bot1_points = bot1_card_sum
                if bot1_card_sum >= 18:
                    bot1_points = bot1_card_sum
                    pick = 0

            if pick == 0:
                bot1_move = 0

        bot2_move = 1
        bot2_points = 0
        while bot2_move:
            print('BOT2 move ....\n')
            bot2_card_1 = randint(2, 11)
            bot2_card_2 = randint(2, 11)
            bot2_card_sum = bot2_card_1 + bot2_card_2
            pick = 0
            print(f'BOT2 First card - {bot2_card_1}')
            print(f'BOT2 Second card - {bot2_card_2}')
            print(f'BOT2 Points - {bot2_card_sum}')

            if bot2_card_sum == 21:
                print('\n\n\t\tBOT2 got 21 points.\n\n')
                bot2_points = bot2_card_sum
                bot2_move = 0

            if bot2_card_sum > 21:
                print('\n\n\t\tBOT2 got more than 21 points. BOT2 loose\n\n')
                bot2_card_sum = 0
                bot2_move = 0
                bot2_points = bot2_card_sum

            if bot2_card_sum == 22 and bot2_card_1 == 11 and bot2_card_2 == 11:
                print('\n\n\t\tBOT2 got double ace! 22 Points.\n\n')
                bot2_move = 0
                bot2_points = bot2_card_sum

            if bot2_card_sum < 21:
                pick = 1

            while pick:
                c = randint(2, 11)
                bot2_card_sum += c
                print(f'BOT2 next card {c}')
                print(f'BOT2 Points {bot2_card_sum}')
                if bot2_card_sum == 21:
                    print('\n\n\t\tBOT2 got 21 points.\n\n')
                    pick = 0
                    bot1_points = bot2_card_sum

                if bot2_card_sum > 21:
                    print('\n\n\t\tBOT2 got more than 21 points. BOT2 loose\n\n')
                    bot2_card_sum = 0
                    pick = 0
                    bot2_points = bot2_card_sum

                if bot2_card_1 == 11 and bot2_card_2 == 11:
                    print('\n\n\t\tBOT2 got double ace! 22 Points\n\n')
                    pick = 0
                    bot2_points = bot2_card_sum
                if bot2_card_sum >= 18:
                    bot2_points = bot2_card_sum
                    pick = 0

            if pick == 0:
                bot2_move = 0

        print('\n\n\t\t\t\tTOTAL SCORE\n')
        print(f'\t\tUSER: {user_points}')
        print(f'\t\tBOT1: {bot1_points}')
        print(f'\t\tBOT2: {bot2_points}')

        if bot1_points > user_points and bot1_points > bot2_points:
            print('\n\n\n\t\tBOT1 WINS')

        if bot2_points > user_points and bot2_points > bot1_points:
            print('\n\n\n\t\tBOT2 WINS')

        if user_points > bot1_points and user_points > bot2_points:
            print('\n\n\n\t\tUSER WINS')

        if bot1_points == bot2_points == user_points:
            print('\n\n\n\t\tEQUAL')
        if bot1_points == bot2_points and bot1_points > user_points:
            print('\n\n\n\t\tBOT1 and BOT2 WIN')
        if user_points == bot2_points and bot1_points > bot1_points:
            print('\n\n\n\t\tUSER and BOT2 WIN')
        if bot1_points == user_points and bot1_points > bot2_points:
            print('\n\n\n\t\tBOT1 and USER WIN')
        game = 0

    try_again = input('Try again? y/n ')

    if try_again == 'y':
        game = 1


