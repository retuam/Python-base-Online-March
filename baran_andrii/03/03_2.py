# method for single list in arguments


def map_(func, seq):
    """
    :description function executes a specified function for each item in a iterable
    :argument func specified function that executes to each item
    :argument seq a single processing sequence
    :type func callback function
    :type seq list
    :return a list of processed items
    :rtype list
    """
    res = []
    for i in seq:
        res.append(func(i))
    return res


def my_func(a):
    return a + 1


x = map_(my_func, [1, 2, 3])
y = map(my_func, [1, 2, 3])

# Check if custom_map works the same as builtin
print(x)
print(list(y))


# method for multiple lists in arguments


def _map(func, *args):
    """
    :description function executes a specified function for each item in a iterable
    :argument func specified function that executes to each item
    :argument args a single or multiple processing sequences
    :type func callback function
    :type args list
    :return a list of processed items
    :rtype list
    """

    common_res = []

    def multi_seq(n):
        res = []
        for seq in args:
            res.append(seq[n])
        return tuple(res)

    if len(args) > 1:
        # We can't use min() so...
        length = len(args[0])
        for arg in args:
            if len(arg) < length:
                length = len(arg)
            else:
                continue

    else:
        length = len(*args)

    for i in range(length):
        common_res.append(func(*multi_seq(i)))
    return common_res


def my_sum(a, b):
    return a + b


x = _map(my_sum, [1, 2, 3], [1, 2, 3])
y = map(my_sum, [1, 2, 3], [1, 2, 3])

# Check if custom_map works the same as builtin
print(x)
print(list(y))
