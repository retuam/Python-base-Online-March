# Method 1


def array_diff(seq1, seq2):
    """ array_dif returns list of unique values that do not appear in seq1 or seq2
        :argument seq1 comparable sequence 1
        :argument seq2 comparable sequence 2
        :return list
        :type seq1 list
        :type seq2 list
        :rtype list
    """

    res = []

    for i in seq1:
        if i not in seq2:
            res.append(i)
        else:
            continue

    for i in seq2:
        if i not in seq1:
            res.append(i)
        else:
            continue
    return res


print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2, 2, 3], [2]))
print(help(array_diff))


# Method 2


def array_diff1(seq1, seq2):
    """ array_dif returns list of unique values that do not appear in seq1 or seq2
        :argument seq1 comparable sequence 1
        :argument seq2 comparable sequence 2
        :return list
        :type seq1 list
        :type seq2 list
        :rtype list
    """

    res_ls = [i for i in seq1 + seq2 if i not in seq1 or i not in seq2]

    return res_ls


print(array_diff1([1, 2], [1]))
print(array_diff1([1, 2, 2, 2, 3], [2]))
print(help(array_diff1))

