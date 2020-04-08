'''
Task description:
    Implement Text Analyzer program.
    Features:
    - Calculate words quantity;
    - Extract text dictionary - unique words;
    - Find keywords - top 3 most frequent words;
    - Calculate frequency for each word - word quantity / all words quantity * 100.

    Do not analyze such words as a, an, to, is, are, was, were, will, would, could, and, or, if, he, she, it, this, my, etc.

    Add docstring.

    Example:
    input: This is my favourite text. Let's try to analyze it. I love this text. I love Python.
    output:
    - words quantity: 9
    - text dictionary: favourite, text, let's, try, analyze, love, python
    - keywords: text - 2, love - 2, favourite - 1
    - frequency: favourite - 11%, text - 22%, let's - 11%, try - 11%, analyze - 11%, love - 22%, python - 11%
'''

#functions---------------------------------------------------------------
def prettify_text(text):
    #normalize and exclude some symbols
    """
    Function, which remove all symbols setted in string "pretty_list"(with delimiter "space") from inserted text.
    :param arg1: text for prettyfy
    :type arg1: type - string
    :return: return inserted text without delimiters setted in string "pretty_list" 
    :rtype: return type - string
    """
    
    pretty_text = text.lower()
    pretty_list = '/ . , ) ( * ? : ; # @'
    pretty_list = pretty_list.split()

    for element in pretty_list:
        pretty_text = pretty_text.replace(element, ' ')
    
    return pretty_text


def words_quantity(text):
    #- Calculate words quantity;
    """
    Function, which calculate all words(returned as dictionary from function "unique_words") from inserted text.
    :param arg1: text for word calculation
    :type arg1: type - string
    :return: return sum of elements of dictionary(converted from text using function "unique_words") 
    :rtype: return type - int
    """
    
    text_dictionary = unique_words(text)
    
    sum_elements = 0
    for element in text_dictionary.values():
        sum_elements += element
                
    return sum_elements


def unique_words(text):
    """
    Function, which convert to dictionary and calculate each word repeat from inserted text without words which setted in string "dont_analyze" and without words with len() = 1.
    :param arg1: text for analyze
    :type arg1: type - string
    :return: return dictionary converted from text and calculation of repeat of each word 
    :rtype: return type - dictionary
    """
    
    dont_analyze = 'a, an, to, is, are, was, were, will, would, could, and, or, if, he, she, it, this, my, etc, etc, etc'
    dont_analyze = dont_analyze.replace(',', ' ')
    dont_analyze = dont_analyze.split()
    dont_analyze = set(dont_analyze)
    
    #- Extract text dictionary - unique words;
    text_list = text.split()
    text_list_set = set(text_list)
    text_diff = text_list_set - dont_analyze
    
    exclude_short = [element for element in text_diff if len(element) < 2]
    exclude_short = set(exclude_short)
    text_diff = text_diff - exclude_short
        
    text_dictionary = {}
    
    for element in text_list:
        count_element = text_list.count(element)
        for el in text_diff:
            if element == el:
                text_dictionary[element] = count_element
    
    return text_dictionary


def top_keywords(text, top_quantity):
    """
    Function, which calculate most repeated words(returned as dictionary from function "unique_words") from inserted text.
    :param arg1: text for analyze
    :type arg1: type - string
    :param arg2: top_quantity - ammount of most repeated words for return form function
    :type arg2: type - int
    :return: return text with needed top rated words) 
    :rtype: return type - string
    """
    
    #- Find keywords - top 3 most frequent words;
    text_dictionary = unique_words(text)
        
    top_words = [f'{key} - {value}' for key, value in sorted(text_dictionary.items(), key = lambda item: item[1], reverse = True)]
    
    top_words = ', '.join([top_words[i] for i in range(top_quantity)])
    
    return top_words


def word_frequency(text):
    """
    Function, which calculate weight(quantity of repeats / total_words, total_words - result of function words_quantity())
    of repeat for each words(returned as dictionary from function "unique_words") from inserted text.
    :param arg1: text for calculation
    :type arg1: type - string
    :return: return calculated frequency for each element of dictionary(converted from text using function "unique_words") 
    :rtype: return type - string
    """
    #- Calculate frequency for each word - word quantity / all words quantity * 100.
    text_dictionary = unique_words(text)
    total_words = words_quantity(text)

    word_frequency_dict = []
    for key, value in text_dictionary.items():
        word_frequency_dict.append(f'{key} - {int(text_dictionary[key] / total_words * 100)}%')
    
    word_frequency_dict = ', '.join(word_frequency_dict)

    return word_frequency_dict


#programm body---------------------------------------------------------
text = input('input text or press Enter for default:')

if text == '':
    text = '''This is my favourite text. Let's try to analyze it. I love this text. I love Python.'''

print('input:', text)
print('output:')

text_modified = prettify_text(text)

words_count = words_quantity(text_modified)
print('- words quantity:', words_count)

text_dictionary = ', '.join(list(unique_words(text_modified)))
print('- text dictionary:', text_dictionary)

text_keywords = top_keywords(text_modified, 3)
print('- keywords:', text_keywords)

text_word_frequency = word_frequency(text_modified)
print('- frequency:', text_word_frequency)
