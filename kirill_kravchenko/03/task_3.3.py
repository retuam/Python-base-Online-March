# Implement custom_filter function, which will behave like the original Python filter() function.
#
# Add docstring.

def if_true_or_false(x):

    output = False

    if x > 2:
        output = True

    return output

filtred_object = filter(if_true_or_false, [1, 2, 3, 4])
print(list(filtred_object))

def my_filter(func, args):
    """
    This is custom filter-function
    :param func: user function
    :type func: function
    :param args: list of arguments
    :type args: list
    :return: array of function result values
    :rtype: list
    """
    output = []

    for i in args:

        flag = func(i)

        if flag:
            output.append(i)

    return output

filtred_object = my_filter(if_true_or_false, [1, 2, 3, 4])
print(list(filtred_object))