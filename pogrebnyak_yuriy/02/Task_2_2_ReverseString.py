'''

Reverse a string

Examples:

input: "Hello"
output: "olleH"

'''
print('Enter word for reverse')
print('Solution 1')

while True:

    #clear variables
    word_reversed = []
    word_reversed_string = ''

    print('')
    reversable_word = list(input('input: '))

    word_reversed = [reversable_word[i] for i in range(len(reversable_word) - 1, -1, -1)]

    j = 0

    for i in word_reversed:

        word_reversed_string += word_reversed[j]

        j += 1

    print('output:', word_reversed_string)
    print('')

    if input('Try again - press "y": ') != 'y':
        break

print('')
print('Solution 2')

while True:

    #clear variables
    word_reversed = []
    word_reversed_string = ''

    print('')
    reversable_word = list(input('input: '))

    word_len = len(reversable_word)
    
    word_reversed = [reversable_word[- i] for i in range(1, word_len + 1)]

    for i in range(word_len):
        word_reversed_string += word_reversed[i]

    print('output:', word_reversed_string)
    print('')

    if input('Try again - press "y": ') != 'y':
        break
