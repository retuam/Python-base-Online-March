from input_output import get_text, text_output

# Text Analyzer program.


delated_words = ('a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would',
                 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'etc', 'to', 'the', 'in', 'be',
                 'no', 'for', 'that')
punctuation = [".", ",", ":", ";", "'", '!', '"', '-']


def lower(pretext):
    pretext_2 = pretext.lower().split()
    return pretext_2


def pretext_conversion(pretext_2):
    text_1 = []
    for word in pretext_2:
        if not word in delated_words:
            text_1.append(word)
    return text_1


def delite_punctuation(text_1):
    text = []
    for word in text_1:
        if not word in punctuation:
            text.append(word)
    return text


# Calculate words quantity;

def count_words(text):
    '''
    The function subtracts one list from another and returns the result.
    :param list1: custom user list
    :type list1: list
    :return: the result of lists' subtracts
    '''
    return len(text)


# Extract text dictionary - unique words;

def count_unique_words(text):
    '''
    The function subtracts one list from another and returns the result.
    :param list1: custom user list
    :type list1: list
    :return: the result of lists' subtracts
    '''
    list = []
    for word in text:
        if not word in list:
            list.append(word)
    return list


# Find keywords - top 3 most frequent words;
def count_top_3_words(text):
    '''
    The function subtracts one list from another and returns the result.
    :param list1: custom user list
    :type list1: list
    :return: the result of lists' subtracts
    '''
    text_dictionary = {i: text.count(i) for i in text}
    return text_dictionary


# Calculate frequency for each word - word quantity / all words quantity * 100.

def freq(text):
    str_list = text
    unique_words = set(str_list)
    for words in unique_words:
        print('Frequency of ', words, 'is :', int((str_list.count(words) / len(str_list)) * 100), '%')


if __name__ == '__main__':


    pretext = get_text('text_to_read.txt')

    pretext_2 = lower(pretext)
    text1 = pretext_conversion(pretext_2)
    text = delite_punctuation(text1)

    words_quantity = count_words(text)
    print(words_quantity)
    text_output('text_output.txt', words_quantity)

    count_unique_words = count_unique_words(text)
    print(count_unique_words)
    text_output('text_output.txt', count_unique_words)

    count_top_3_words = count_top_3_words(text)
    j = 0
    for key, value in sorted(count_top_3_words.items(), key=lambda item: item[1], reverse=True):
        print("%s - %s" % (key, value))
        j += 1
        if j >= 3:
            break
    text_output('text_output.txt', count_top_3_words)

    freq = freq(text)
    print(freq)
    text_output('text_output.txt', freq)
