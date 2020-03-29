# Implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values (all of its occurrences) from list a, which are present in list b.
#
# Add docstring.
#
# Examples:
#
# call: array_diff([1, 2], [1])
# return: [2]
#
# call: array_diff([1, 2, 2, 2, 3], [2])
# return: [1,3]

# Variant 1, with flag

print("Variant 1")

def array_diff(list_1, list_2):
    """
    This is a function that looks for the difference of arrays by unique values
    :param list_1: 1-st array
    :type list_1: list
    :param list_2: 2-nd array
    :type list_2: list
    :return: new array
    :rtype: list
    """
    list_output = []

    for i in list_1:

        flag = True

        for j in list_2:

            if i == j:
                flag = False

        if flag:
            list_output.append(i)

    return list_output

output = array_diff([1, 2], [1])
print(f'Answer 1.1. is {output}')
output = array_diff([1, 2, 2, 2, 3], [2])
print(f'Answer 1.2. is {output}')
# print(array_diff.__doc__)

# Variant 2, without flag

print("Variant 2")

def array_without_element(element, array):
    """
    This is a function that removes an element from an array.
    :param element: removing element
    :type element: int
    :param array: array for searching
    :type array: list
    :return: array without element
    :rtype: list
    """
    list_output = []

    for j in array:

        if element != j:
            list_output.append(j)

    return list_output


def array_diff_in(list_1, list_2):
    """
    This is a function that looks for the difference of arrays by unique values
    :param list_1: 1-st array
    :type list_1: list
    :param list_2: 2-nd array
    :type list_2: list
    :return: different array
    :rtype: list
    """
    for i in list_2:

        list_1 = array_without_element(i, list_1)

    return list_1


output = array_diff_in([1, 2], [1])
print(f'Answer 2.1. is {output}')
output = array_diff_in([1, 2, 2, 2, 3], [2])
print(f'Answer 2.2. is {output}')
# print(array_without_element.__doc__)
# print(array_diff_in.__doc__)

# Variant 3, comprehensive type

print("Variant 3")

def array_without_element_cmpr(element, array):
    """
    This is a function that removes an element from an array.
    :param element: removing element
    :type element: int
    :param array: array for searching
    :type array: list
    :return: array without element
    :rtype: list
    """
    return [j for j in array if element != j]

def array_diff_in_cmpr(list_1, list_2):
    """
    This is a function that looks for the difference of arrays by unique values
    :param list_1: 1-st array
    :type list_1: list
    :param list_2: 2-nd array
    :type list_2: list
    :return: different array
    :rtype: list
    """
    for i in list_2:

        list_1 = array_without_element_cmpr(i, list_1)

    return list_1


output = array_diff_in_cmpr([1, 2], [1])
print(f'Answer 3.1. is {output}')
output = array_diff_in_cmpr([1, 2, 2, 2, 3], [2])
print(f'Answer 3.2. is {output}')
