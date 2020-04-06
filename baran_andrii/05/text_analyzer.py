import file_reader as fr

CLOSED_CLASS_WORDS = (
    'nothing', 'wherefrom', 'in', 'long', 'the', 'wasn’t', 'there', 'for', 'my', 'wheresoever',
    'theirself', 'hadn’t', 'whomsoever', 'do', 'yon', 'outside', 'anybody', 'have', 'such',
    'many', 'third', 'must', 'ought', 'against', 'neither', 'despite', 'following', 'than',
    'whereto', 'whether', 'much', 'nought', 'whence', 'plus', 'both', 'him', 'thee', 'whatnot',
    'across', 'it', 'beneath', 'another', 'every', 'did', 'someone', 'below', 'we', 'each',
    'after', 'us', 'excepting', 'anti', 'like', 'weren’t', 'i', 'everyone', 'theirs', 'except',
    'he', 'is', 'ours', 'about', 'last', 'himself', 'itself', 'mine', 'considering', 'during',
    'yet', 'until', 'didn’t', 'over', 'hasn’t', 'does', 'was', 'save', 'lot', 'beside', 'onto',
    'his', 'their', 'next', 'or', 'whosoever', 'within', 'between', 'versus', 'everybody',
    'your', 'now', 'that', 'into', 'up', 'whosesoever', 'will', 'whereon', 'has', 'suchlike',
    'on', 'themselves', 'none', 'shall', 'were', 'by', 'themself', 'when', 'either', 'under',
    'enough', 'thyself', 'a', 'per', 'along', 'whereof', 'been', 'inside', 'upon', 'thine',
    'yonder', 'few', 'nobody', 'what', 'be', 'time', 'whenever', 'whereinto', 'an', 'thy', 'and',
    'aught', 'them', 'some', 'wherewithal', 'myself', 'doesn’t', 'down', 'near', 'opposite',
    'but', 'off', 'she', 'whomever', 'am', 'idem', 'minus', 'haven’t', 'aren’t', 'any',
    'whatever', 'could', 'which', 'its', 'nor', 'had', 'anyone', 'round', 'others', 'wherein',
    'you', 'are', 'somewhat', 'wherewith', 'isn’t', 'with', 'anything', 'once', 'past', 'where',
    'herself', 'those', 'underneath', 'all', 'unlike', 'before', 'via', 'whichever', 'can',
    'concerning', 'yourself', 'might', 'so', 'somebody', 'among', 'ourself', 'whomso',
    'everything', 'naught', 'our', 'whose', 'yours', 'towards', 'first', 'till', 'little',
    'being', 'around', 'without', 'these', 'one', 'whereby', 'whoever', 'whoso', 'through',
    'whichsoever', 'should', 'shouldn’t', 'as', 'from', 'ourselves', 'most', 'beyond', 'whom',
    'wherever', 'whosever', 'her', 'behind', 'several', 'plenty', 'whatsoever', 'toward',
    'yourselves', 'whereunto', 'above', 'soon', 'other', 'something', 'thou', 'no', 'who',
    'excluding', 'hers', 'of', 'would', 'aboard', 'at', 'theirselves', 'me', 'second', 'while',
    'to', 'they', 'may', 'regarding', 'besides', 'this', 'since', 'acros', 'amid', 'ye', 'is', 'an', 'of',
    'in', 'by', 'and')

PUNCTUATION = (
    ',', '.', '/', ';', '\\', '[', ']', '(', ')', '{', '}', '^', ':', '"', '"', '|', '$', '#', '@', '!',
    '~', '`', '_', '-', '*', '+', '=', '*')


def is_service_word(item):
    """
    :description: Function checks if item is in CLOSED_CLASS_WORDS const
    :param item: list str element
    :return: Bool
    """
    if item in CLOSED_CLASS_WORDS:
        return True

    else:
        return False


def is_punctuation(item):
    """
    :description: Function checks if item is in PUNCTUATION const
    :param item: string item
    :return: Bool
    """
    if item in PUNCTUATION:
        return True

    else:
        return False


def prepare_text(txt):
    """
    :description: Function removes punctuation, convert input string to lower case and cast list
    :param txt: processed string
    :return: casted list
    """
    for symb in txt:
        if is_punctuation(symb):
            txt = txt.replace(symb, ' ')
        else:
            continue
    txt = txt.lower().strip().split()
    return txt


def words_counter(ls):
    """
    :description: Function returns the amount of item in list
    :param ls: processed list
    :return: int
    """
    return len(ls)


def get_unique_words(ls):
    """
    :description: Function returns list of unique items from input
    :param ls: processed list
    :return: list
    """

    return list(set(ls))


def find_keywords(ls):
    """
    :description Function finds 3 top frequent items in input list and returns a list of pairs (word, quantity)
    :param ls: processed list
    :return: list
    """
    filtered_ls = []
    for itm in ls:

        if is_service_word(itm):
            continue
        else:
            filtered_ls.append(itm)

    temp = sorted(list(set(filtered_ls)), key=lambda n: filtered_ls.count(n), reverse=True)
    res = []
    for j in temp[:3]:
        tmp_ls = [j, ls.count(j)]
        res.append(tuple(tmp_ls))
    return res


def find_freq(ls):
    """
    :description Function finds calculates frequency in % fro each item in a list. Returns dict with k,w {word = freq%)
    :param ls: processed list
    :return: dict
    """
    res = {}
    for m in ls:
        res[f'{m}'] = int((ls.count(m) / len(ls) * 100) * 100) / 100
    return res


if __name__ == '__main__':

    fr.create_file()
    text = fr.extract_text()
    text = prepare_text(text)

    words_quantity = words_counter(text)

    text_dictionary = get_unique_words(text)
    text_dictionary = ', '.join(str(i) for i in text_dictionary)

    keywords = find_keywords(text)
    keywords = ', '.join([f'{i[0]} - {i[1]}' for i in keywords])

    word_frequency = find_freq(text)
    word_frequency = ', '.join([f'{k} - {v}%' for k, v in word_frequency.items()])

    content = f'words quantity: {words_quantity} \n' \
              f'text dictionary: {text_dictionary} \n' \
              f'keywords: {keywords} \n' \
              f'frequency: {word_frequency} '

    fr.append_file(content)
