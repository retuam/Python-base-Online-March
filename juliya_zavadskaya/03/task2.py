#v1
def mapper(func, lists):

    """
    The function imitate original map python function.
    :param func: custom func operated with user list
    :param lists: custom user list
    :return: the result of lists' split
    """

    list1 = []
    for i in range(len(lists[0])):
        list1.append(func(lists[0][i], lists[1][i], lists[2][i]))
    return list1


def func(a, b, c):
    return a + b + c


lists= [['3', '4', '5'], ['13', '44', '65'], ['2', '3', '3']]

x = mapper(func, lists)

print(x)

'''
#v2
def get_my_map(list1, list2):
    """
    The function imitate original map python function.
    :param func: custom func operated with user list
    :param lists: custom user list
    :return: the result of lists' split
    """
    result_1 = [x + y for x, y in zip(list1, list2)]
    return result_1


list1 = input('Enter the first list:')
list2 = input('Enter the second list:')
result_1 = get_my_map(list1, list2)
print(result_1)
'''
'''
#v3
def mapper(func, sequences):

    """
    The function imitate original map python function.
    :param func: custom func operated with user list
    :param lists: custom user list
    :return: the result of lists' split
    """

    list1 = []
    for i in sequences:
        list1.append(func(i))
    return list1


def func(n):
    ls = n + 1
    return ls


ls = [1, 2, 3]
x = mapper(func, ls)

print(x)
'''