# Implement custom_map function, which will behave like the original Python map() function.
#
# Add docstring.

def myfunc(a, b):
    """
    This is a function for concatenating strings (function 1 for test)
    :param a: first string
    :type a: str
    :param b: second string
    :type b: str
    :return: concatenated string
    :rtype: str
    """
    return a + b

def power_two(number):
    """
    This is a function for squaring (function 2 for test)
    :param number: number
    :type number: float
    :return: squared number
    :rtype: float
    """
    result = number ** 2

    return result

print('Map function')

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

x = map(power_two, [1.1, 2, 3])
print(list(x))

x = map(power_two, [7])
print(list(x))

def my_map(func, *args):
    """
    This is custom map-function
    :param func: user function
    :type func: function
    :param `*args`: the variable arguments are used for function
    :type `*args`: variable-length argument list
    :return: array of function result values
    :rtype: list
    """
    output = []

    for i in range(len(args[0])):

        vars = []

        for arg in args:
            vars.append(arg[i])

        x, *y = vars

        output.append(func(x, *y))

    return output

print('Custom map function')

x = my_map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

x = my_map(power_two, [7])
print(list(x))

x = my_map(power_two, [1.1, 2, 3])
print(list(x))
