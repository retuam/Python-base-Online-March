'''

Hello world

Check to see if a string has the same amount of 'x's and 'o's.
The string can contain any char.

Examples:

input: "ooxx"
output: True

input: "xooxx"
output: False

input: "ooxXm"
output: True

True when no 'x' and 'o' is present
input: "zpzpzpp"
output: True

'''

print('')
print('Solution 1:')
print('')
print('Check to see if a string has the same amount of "x"s and "o"s.')
print('input your word or "Quit" for quit')

while True:

    print('')
    
    checkable_word = input('input:')
    
    if checkable_word == 'Quit' or checkable_word == 'quit':
        break
    
    checkable_word_list = list(checkable_word)

    count_x = 0
    count_o = 0

    j = 0
    
    for i in checkable_word_list:

        if checkable_word_list[j] == 'x' or checkable_word_list[j] == 'X':
            count_x += 1

        elif checkable_word_list[j] == 'o' or checkable_word_list[j] == 'O':
            count_o += 1

        j += 1

    if not count_x == count_o:
        print('output:', False)

    else:
        print('output:', True)

print('')
print('Solution 2:')
print('input your word or press Enter with empty input for quit')

while True:

    print('')

    checkable_word_list = list(input('input:'))

    checkable_word_len = len(checkable_word_list)

    if checkable_word_len > 0:

        count_x = [1 for i in range(checkable_word_len)
                   if checkable_word_list[i] == 'x'
                   or checkable_word_list[i] == 'X']

        count_o = [1 for i in range(checkable_word_len)
                   if checkable_word_list[i] == 'o'
                   or checkable_word_list[i] == 'O']

        if not count_x == count_o:
            print('output:', False)

        else:
            print('output:', True)
    else:
        break
