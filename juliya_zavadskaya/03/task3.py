def cust_filter(func, lists):

    """
    The function imitate original map python function.
    :param x: custom user list
    :param y: custom user list
    :return: the result of lists' split
    """

    list1 = []
    for i in range(len(lists)):
        if func(lists[i]) == True:
            list1.append(lists[i])
    return list1

print(cust_filter(lambda x: x % 2 ,[ 1,2,3,4,5,6,7,8,9]))