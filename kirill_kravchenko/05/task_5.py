# Implement Text Analyzer program.
# Features:
# - Calculate words quantity;
# - Extract text dictionary - unique words;
# - Find keywords - top 3 most frequent words;
# - Calculate frequency for each word - word quantity / all words quantity * 100.
#
# Do not analyze such words as a, an, to, is, are, was, were, will, would, could, and, or, if, he, she, it, this, my, etc.
#
# Add docstring.
#
# Example:
# input: This is my favourite text. Let's try to analyze it. I love this text. I love Python.
# output:
# - words quantity: 9
# - text dictionary: favourite, text, let's, try, analyze, love, python
# - keywords: text - 2, love - 2, favourite - 1
# - frequency: favourite - 11%, text - 22%, let's - 11%, try - 11%, analyze - 11%, love - 22%, python - 11%
from package import my_module

def output_keywords(list):
    """
    This is formater function
    :param list: dictionary
    :type list: dict
    :return: result string
    :rtype: str
    """
    try:

        output = []

        for key, value in list.items():

            output.append(key + ' - ' + str(value))

        return output

    except AttributeError:

        print('Attribute must be a list')


def text_analizer(mstring):
    """
    This is text analyzer function
    :param string: text
    :type string: str
    :return: array of function result values
    :rtype: list
    """
    try:

        replaced_word = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if',
                         'he',
                         'she', 'it', 'this', 'my', 'the', 'on', 'of', 'in', 'no', 'with', 'but', 'that', 'than']
        replaced_symbols = (',', '!', '.', ':', ';', '?', ' - ', '"', "'s", '(', ')', '”', '“', '&', ' — ', '$')

        output = {'keywords': {}, 'frequency': {}, 'frequency_three': {}}

        mstring = ' ' + mstring.lower()

        for repl in replaced_symbols:
            mstring = mstring.replace(repl, '')

        for repl in replaced_word:
            mstring = mstring.replace(' ' + repl + ' ', ' ')

        words_dict = mstring.split()

        sample = ''

        for i in sorted(words_dict):

            if i.isdigit():
                continue

            if i != sample:
                value = 1
                sample = i
            else:
                value += 1

            output['keywords'][i] = value

        output['words_quantity'] = len(output['keywords'])

        j = 0

        for key, value in sorted(output['keywords'].items(), key=lambda item: item[1], reverse=True):

            percent = str(round(value / output['words_quantity'] * 100, 2)) + '%'

            output['frequency'][key] = percent
            if j < 3:
                output['frequency_three'][key] = percent
                j += 1

        return output

    except AttributeError:

        print('Attribute must be a string')


if __name__ == '__main__':
    # variant 1 for eval(arg) extraction
    # save_result(text_analizer(extract_function()))

    # variant 2 for string extraction
    mstring = my_module.extract_file('text3.txt')

    try:

        input_list = text_analizer(mstring)
        output = []

        output.append(str(input_list['words_quantity']))
        output.append(', '.join(input_list['keywords']))
        output.append(', '.join(output_keywords(input_list['keywords'])))
        output.append(', '.join(output_keywords(input_list['frequency'])))
        output.append(', '.join(output_keywords(input_list['frequency_three'])))

        my_module.save_result('\n'.join(output))

    except TypeError as error:
        print('Arguments to save in file isn\'t a string')
