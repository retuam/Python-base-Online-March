def get_dif_function(list1, list2):
    """
    The function subtracts one list from another and returns the result.
    It should remove all values (all of its occurrences) from one list, which are present in the another list.
    :param list1: custom user list
    :param list2: custom user list
    :type list1: list
    :type list2: list
    :return: the result of lists' subtracts
    """
    list_result = []
    for i in range(len(list1)):
            if not(list1[i] in list2):
                list_result.append(list1[i])

    return list_result


print(get_dif_function([2, 3, 4, 5], [3]))