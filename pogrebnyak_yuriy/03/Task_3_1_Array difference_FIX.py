'''
Implement a difference function, which subtracts one list from another and returns the result.

It should remove all values (all of its occurrences) from list a, which are present in list b.

Add docstring.

Examples:

call: array_diff([1, 2], [1])
return: [2]

call: array_diff([1, 2, 2, 2, 3], [2])
return: [1,3]
'''

print('It should remove all values (all of its occurrences) from list a, which are present in list b.')

def array_diff(list_a, list_b):
    """
    Function, which subtracts one list from another and returns the result.
    It should remove all values (all of its occurrences) from list a, which are present in list b.
    :param arg1: list A argument
    :param arg2: list B argument
    :type arg1: type - list
    :type arg2: type - list
    :return: return list A values without values removed from list A, which are present in list b 
    :rtype: return type - list
    """
    
    diff_result = []

    for i in list_a:
        same_elements = []
        same_elements = [1 for j in list_b if i == j]
        if same_elements == []:
            diff_result.append(i)
             
    return diff_result


list_a = list(input('input list A without delimiters(example: 12223 will be converted to [1, 2, 2, 2, 3]):'))
print('you list A is:', list_a)

list_b = list(input('input list B without delimiters(example: 12223 will be converted to [1, 2, 2, 2, 3]):'))
print('you list B is:', list_b)

print(f'call: array_diff({list_a}, {list_b})')
print('return:', array_diff(list_a, list_b))
