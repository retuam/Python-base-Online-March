def filter_(func, seq):
    """
    :description: function returns an iterator were the items are filtered through a function
     to test if the item is accepted or not
    :argument func: specified function that executes for each item
    :argument seq: processed sequence
    :type func function
    :type seq list
    :return: filtered list
    :rtype list
    """

    res = []

    for i in seq:

        if func(i):
            res.append(i)

        else:
            continue

    return res


def is_odd(number):
    if number % 2:

        return False

    else:
        return True


x = filter_(is_odd, [1, 2, 3, 4, 5])
y = filter(is_odd, [1, 2, 3, 4, 5])

# Check if custom filter returns same value as builtin
print(x)
print(list(y))
