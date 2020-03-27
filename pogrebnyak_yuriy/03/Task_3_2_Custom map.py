'''
Implement custom_map function, which will behave like the original Python map() function.

Add docstring.
'''

def custom_map(func, *args):

    """
    Custom_map function, which will behave like the original Python map() function.
    :param arg1: func, function name to which custom_map passes each element of given iterable
    :param arg2: *args, A sequence, collection or an iterator object
    :type arg1: type - string
    :type arg2: type - list
    :return: Returns a list of the results after applying the given function  
             to each item of a given iterable
    :rtype: return type - list

    Small comment: the differance between map() and custom_map(), output example:
    
        >>> map(print, [1, 2, 3])
        <map object at 0x034D7B20> 

        >>> list(map(print, [1, 2, 3]))
        1
        2
        3
        [None, None, None]

        >>> custom_map(print, [1, 2, 3])
        1
        2
        3
        [None, None, None]

    Custom_map() don`t return object (link to memory value) but return list of the results.
    And I don`t know how to make it exactly the same function as map().
    Possibly It`s needed to use python mathods.
    """

    def inner_func(in_args):
        """
        Function for solve: custom_map(lambda x,y: x*y, [1,2],[3,4])
        """
        print('in_args: ', in_args)
        print(len(in_args))
        
        x = func(tuple(in_args))
        return x

    if len(args) == 1:
        return [func(i) for arg in args for i in arg]
    else:
        return inner_func(args)

     
l = [['sat', 'bat', 'cat', 'mat'], ['sat', 'bat', 'cat', 'mat']]
test = list(map(list, l))
print('Original map() result:', test)

test = list(custom_map(list, l))
print('Custom function custom_map() result:', test)
