'''
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Examples:

list: [1, 2, 3, 1, 3, 2, 1]
output: 1

'''

print('enter list without delimiter(example: 1231321) or press Enter with empty input (default list: [1, 2, 3, 1, 3, 2, 1])')
print('Solution 1')

while True:
    
    new_list = list(input('input: '))

    if new_list == []:

        print('empty input goes to default entry')

        new_list = list('1231321')

    print('list:', new_list)

    '''
    check if there are list elements that appear.
    universal method for all types of elements
    '''

    list_len = len(new_list)

    repeatable_odd = []
    repeatable_even = []
    repeatable_ones = []

    for i in range(0, list_len):

        appears_count = 0

        for j in range(0, list_len):

            if new_list[i] == new_list[j]:
                appears_count += 1

        if appears_count == 1 and not new_list[i] in repeatable_ones:
            repeatable_ones.append(new_list[i])

        elif appears_count > 1 and appears_count % 2 == 0 and not new_list[i] in repeatable_even:
            repeatable_even.append(new_list[i])
                
        elif appears_count > 1 and appears_count % 2 != 0 and not new_list[i] in repeatable_odd:
            repeatable_odd.append(new_list[i])

    '''
    check if repeatable element is integer
    '''

    count_repeatable_int = 0

    if not repeatable_odd == []:

        for i in repeatable_odd:

            for j in range(0,10):
                
                if str(i) == str(j):
                    print('output:', i)
                    count_repeatable_int += 1

    if len(repeatable_ones) > 0:
        print('There are list elements that appear ones and it is although odd times')

        for i in repeatable_ones:
            print('output:', i)

    if count_repeatable_int > 1 and len(repeatable_ones) > 0:

            print('There must always be only one integer that appears an odd number of times.')
            print('and FYI there are several list elements that appear odd times.')

    if input('Try again - press "y": ') != 'y':
        break

print('Solution 2')

while True:
    '''
    Clear previous list entry
    '''
    repeatable_odd = []
    repeatable_even = []
    repeatable_ones = []
    appears_count = []
    
    new_list = list(input('input: '))

    if new_list == []:

        print('empty input goes to default entry')

        new_list = list('1231321')

    print('list:', new_list)

    '''
    check if there are list elements that appear.
    universal method for all types of elements
    '''

    list_len = len(new_list)

    for i in range(0, list_len):

        appears_count = len([1 for j in range(0, list_len) if new_list[i] == new_list[j]])

        if appears_count == 1 and not new_list[i] in repeatable_ones:
            repeatable_ones.append(new_list[i])

        elif appears_count > 1 and appears_count % 2 == 0 and not new_list[i] in repeatable_even:
            repeatable_even.append(new_list[i])
                
        elif appears_count > 1 and appears_count % 2 != 0 and not new_list[i] in repeatable_odd:
            repeatable_odd.append(new_list[i])

    '''
    check if repeatable element is integer
    '''

    count_repeatable_int = []

    if not repeatable_odd == []:
        count_repeatable_int = [i for i in repeatable_odd for j in range(0,10) if str(i) == str(j)]

        for i in count_repeatable_int:
            print('output:', i)

    if len(repeatable_ones) > 0:
        print('There are list elements that appear ones and it is although odd times')
        
        for i in repeatable_ones:
            print('output:', i)

    if len(count_repeatable_int) > 1 and len(repeatable_ones) > 0:

            print('There must always be only one integer that appears an odd number of times.')
            print('and FYI there are several list elements that appear odd times.')

    if input('Try again - press "y": ') != 'y':
        break
    
