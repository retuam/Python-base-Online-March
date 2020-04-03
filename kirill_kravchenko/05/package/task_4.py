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

mstring = '''The owners of the Zaandam, Holland America, said that more than 130 people on board had reported 
            suffering "flu-like symptoms" and respiratory issues.
            Nobody has left the ship since it docked in Chile two weeks ago.
            Holland America said it planned to transfer passengers to a sister ship.
            The Zaandam and the Rotterdam are both off the western, Pacific coast of Panama.
            The Zaandam is trying to sail to Florida. But the Panamanian authorities have said no vessel with 
            confirmed coronavirus cases on board can pass through the Panama Canal.'''

replaced_word = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'the', 'on', 'of', 'in', 'no', 'with', 'but', 'that', 'than']

def text_analizer(mstring):
    """
    This is text analyzer function
    :param string: text
    :type string: str
    :return: array of function result values
    :rtype: list
    """
    output = {'keywords': {}, 'frequency': {}, 'frequency_three': {}}

    mstring = ' ' + mstring.lower()

    for repl in replaced_word:

        mstring = mstring.replace(' ' + repl + ' ', ' ')

    words_dict = mstring.split()

    sample = ''

    for i in sorted(words_dict):

        # skip all numbers in text
        if i.isdigit():
            continue

        # for 2nd, 1st, otherwise i.isalpha()
        while not i.isalnum():
            if not i[-1].isalnum():
                i = i[0:-1]
            elif not i[0].isalnum():
                i = i[1:len(i)]
            else:
                break
            break

        if i != sample:
            value = 1
            sample = i
        else:
            value += 1

        output['keywords'][i] = value

    output['words_quantity'] = len(output['keywords'])

    j = 0

    for key, value in sorted(output['keywords'].items(), key=lambda item: item, reverse=True):

        percent = str(int(value / output['words_quantity'] * 100)) + '%'

        output['frequency'][key] = percent
        if j < 3:
            output['frequency_three'][key] = percent
            j += 1

    return output

# formating output, not text_analizer function
def output_keywords(list):
    """
    This is formater function
    :param list: dictionary
    :type list: dict
    :return: result string
    :rtype: str
    """
    output = []

    for key, value in list.items():

        output.append(key + ' - ' + str(value))

    return output

words_quantity = text_analizer(mstring)['words_quantity']
text_dictionary = ', '.join(text_analizer(mstring)['keywords'])

print(f'words quantity: {words_quantity}')
print(f'text_dictionary: {text_dictionary}')

keywords = ', '.join(output_keywords(text_analizer(mstring)['keywords']))
frequency = ', '.join(output_keywords(text_analizer(mstring)['frequency']))
frequency_three = ', '.join(output_keywords(text_analizer(mstring)['frequency_three']))

print(f'keywords: {keywords}')
print(f'frequency: {frequency}')
print(f'frequency_three: {frequency_three}')

# Variant 2, with symbole replacement
print('Variant 2, with symbole replacement list')

replaced_symbols = [',', '!', '.', ':', ';', '?', ' - ', '"', "'s", '(', ')']

def text_analizer2(mstring):
    """
    This is text analyzer function
    :param string: text
    :type string: str
    :return: array of function result values
    :rtype: list
    """
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

    for key, value in sorted(output['keywords'].items(), key=lambda item: item, reverse=True):

        percent = str(int(value / output['words_quantity'] * 100)) + '%'

        output['frequency'][key] = percent
        if j < 3:
            output['frequency_three'][key] = percent
            j += 1


    return output

words_quantity = text_analizer(mstring)['words_quantity']
text_dictionary = ', '.join(text_analizer(mstring)['keywords'])

print(f'words quantity: {words_quantity}')
print(f'text_dictionary: {text_dictionary}')

keywords = ', '.join(output_keywords(text_analizer(mstring)['keywords']))
frequency = ', '.join(output_keywords(text_analizer(mstring)['frequency']))
frequency_three = ', '.join(output_keywords(text_analizer(mstring)['frequency_three']))

print(f'keywords: {keywords}')
print(f'frequency: {frequency}')
print(f'frequency_three: {frequency_three}')