# Import function randint from module random
from random import randint

# Level 1 - one player.
# Level 2 - one player + one bot.
# Level 3 - one player + two bots.

# Rules
deck = 10
victory_rule = 21 # max score. After max score gamer is lose
card_min = 2
card_max = 11

# Bots strength
bot_rule_1 = 19 # exemple for fixed score bot in pick
bot_rule_2 = 50 # exemple for dynamic score bot in percents, where 50 is never taking card, if probability of success less or equil equal to 50%, not 0!

level = int(input("Game with 1 Bot input 1, game with 2 Bots input 2, game myself input 0 or other symbol "))

decision_0 = 1 # user decision, 1 - if user are continue gaming
decision_1 = 0
decision_2 = 0

bot_pick_0 = 0 # user pick
bot_pick_1 = 0
bot_pick_2 = 0

if level !=1 and level != 2:
    level = 0
elif level == 1:
    decision_1 = 1
elif level == 2:
    decision_1 = 1
    decision_2 = 1

while (decision_0 or decision_1 or decision_2) and deck:

    # user
    # user step
    if decision_0:
        print("Your pick is", bot_pick_0, "and remaining deck is", deck)
        decision_0 = int(input('Input "1" to take more or input "0" to pass '))
        if decision_0:
            deck -= 1
            bot_pick_0 += randint(card_min, card_max)

    # user check
    if bot_pick_0 > victory_rule:
        bot_pick_0 = -1
        decision_0 = 0   

    # bot 1
    # bot 1 step
    if level > 0 and deck and decision_1:
        if bot_pick_1 >= bot_rule_1:
            decision_1 = 0
        if decision_1:
            deck -= 1
            bot_pick_1 += randint(card_min, card_max)

        # bot 1 check
        if bot_pick_1 > victory_rule:
            bot_pick_1 = -1
            decision_1 = 0 

    # bot 2
    # bot 2 step
    if level > 1 and deck and decision_2:
        if card_min > (victory_rule - bot_pick_2):
            decision_2 = 0
        elif card_max > (victory_rule - bot_pick_2) and (card_max + card_min) > (100 / bot_rule_2) * (victory_rule - bot_pick_2):
            decision_2 = 0
                
        if decision_2:
            deck -= 1
            bot_pick_2 += randint(card_min, card_max)

        # bot 2 check
        if bot_pick_2 > victory_rule:
            bot_pick_2 = -1
            decision_2 = 0

max_pick = bot_pick_0

if level > 0 and max_pick < bot_pick_1:
    max_pick = bot_pick_1      

if level > 1 and max_pick < bot_pick_2:
    max_pick = bot_pick_2

print("remaining deck", deck)

if max_pick < 0:
    print("all gamers and user are loser")
else:    
    if bot_pick_0 == max_pick:
        print("user is winner with score", max_pick)
    elif bot_pick_0 > 0:
        print("user is loser with score", bot_pick_0)
    else:
        print("user is loser with over score points")

    if level > 0:
        if bot_pick_1 == max_pick:
            print("bot 1 is winner with score", max_pick)
        elif bot_pick_1 > 0:
            print("bot 1 is loser with score", bot_pick_1)
        else:
            print("bot 1 is loser with over score points")
            
    if level > 1:
        if bot_pick_2 == max_pick:
            print("bot 2 is winner with score", max_pick)
        elif bot_pick_2 > 0:
            print("bot 2 is loser with score", bot_pick_2)
        else:
            print("bot 2 is loser with over score points")



    
