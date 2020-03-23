from random import randint

print ('')
print ('                  21 GAME')
print ('')
print ('           Powered by Pogrebnyak')
print ('')

game = 1

while game:

    print ('')
    print ('       level - 1 "Monkey"       ')
    print ('       level - 2 "Opponent"     ')
    print ('       level - 3 "Nightmare!"   ')
    print ('')

    level = input('Chose game level OR press any other key to continue (default level: 1 ): ')

    if not level or int(level) < 1 or int(level) > 3:
        level = 1

    else:
        level = int(level)

    print ('')
    print ('                         Your level is:', level, '. Good luck!')
    print ('')

    while level:

        play_game = 1
        while play_game:

            sum_player1 = 0
            sum_player2 = 0
            sum_player3 = 0

            i = 0

            while i < level:

                i += 1

                print ('')
                print('Player',i,'is playing....')
                print ('')

                print ('    Here is your two cards:')
                print ('')
                
                a  = randint(2, 11)

                b  = randint(2, 11)

                if i == 3 and a > b:

                    a = randint(b, a)

                    b = randint(b, a)

                elif i == 3 and a < b:

                    a = randint(a, b)

                    b = randint(a, b)

                print ('    You`ve got', a, 'and', b,'.')
                print ('')

                sum_player = a + b

                if sum_player == 22:

                    print ('    Combo jackpot. Double Ace! You win!')
                    print ('')

                    if i == 1:
                        sum_player1 = 21
                        sum_player2 = 0
                        sum_player3 = 0

                    elif i == 2:
                        sum_player1 = 0
                        sum_player2 = 21
                        sum_player3 = 0

                    elif i == 3:
                        sum_player1 = 0
                        sum_player2 = 0
                        sum_player3 = 21

                    break
                
                while sum_player < 21:
                          
                    print ('    Player`s', i,' points is:', sum_player)
                    print ('')
                    print ('    You`ll win if you get 21.')
                    print ('')

                    if i == 1:

                        check_addcard = input('Press 1 for get additional card OR any key for PASS: ')
                        print ('')

                    else:

                        check_rest = 21 - sum_player

                        if check_rest > 10:

                            check_addcard = 1

                        elif check_rest > 5:

                            print ('    I am thinking........')

                            check_addcard = 1

                        elif check_rest <= 3:

                            check_addcard = 0

                            print ('    I am full.')
                    
                    if not check_addcard or int(check_addcard) != 1:

                        break

                    else:

                        c = 0

                        c = randint(2, 11)

                        sum_player += c

                        print ('')
                        print ('        Next card is', c)
                        print ('')

                if i == 1:

                    sum_player1 = sum_player
                    print ('Player', i, '`ve got', sum_player1)

                elif i == 2:

                    sum_player2 = sum_player
                    print ('Player', i, '`ve got', sum_player2)

                elif i == 3:

                    sum_player3 = sum_player
                    print ('Player', i, '`ve got', sum_player3)

                else:
                    break
            
            print ('And winner is:')
            print ('')

            if sum_player1 > 21: sum_player1 = 0

            if sum_player2 > 21: sum_player2 = 0

            if sum_player3 > 21: sum_player3 = 0

            if level > 0 and sum_player1 > 0:

                print ('Player1', sum_player1)

            if level > 1 and sum_player2 > 0:

                print ('Player2', sum_player2)

            if level > 2 and sum_player3 > 0:

                print ('Player3', sum_player3)

            if sum_player1 > sum_player2 and sum_player1 > sum_player3:

                print ('You win!')

            elif sum_player2 > sum_player1 and sum_player2 > sum_player3:

                print ('You lose! Player2 win!')

            elif sum_player3 > sum_player1 and sum_player3 > sum_player2:

                print ('You lose! Player3 win!')

            elif sum_player1 == sum_player2 or sum_player2 == sum_player3 or sum_player1 == sum_player3:

                print ('There is couple winners. Try again to kill `em all.')

            else:
                print ('Nobody.')


            print ('')
            play_game = input('Press 1 for try again, Press 2 for change level OR any other key for QUIT: ')

            if not play_game:

                game = 0
                level = 0
                play_game = 0

            elif int(play_game) == 2:

                play_game = 0
                level = 0

            elif int(play_game) != 1:

                game = 0
                level = 0
                play_game = 0
        
print ('       Game over!')            
print ('       I`ll be back!')


