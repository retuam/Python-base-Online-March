'''
Task 5 requrements:

Use your Task 4 to finish Task 5.

Additional features:
- Module that provide a possibility to:
-- Extract a text from text.txt file;
-- Save results to results.txt file;
- Run your logic only if the main file was executed;
- Try to handle as much exceptions as possible.


Task_4.py - text functions

Task description:
    Implement Text Analyzer program.
    Features:
    - Calculate words quantity;
    - Extract text dictionary - unique words;
    - Find keywords - top 3 most frequent words;
    - Calculate frequency for each word - word quantity / all words quantity * 100.

    Do not analyze such words as a, an, to, is, are, was, were, will, would, could, and, or, if, he, she, it, this, my, etc.

Task content:
    task_4(text) - main function, makes all task_4 routines
        prettify_text(text)
        words_quantity(text)
        unique_words(text)
        top_keywords(text, top_quantity)
        word_frequency(text)
'''


from Task_4_5 import task_4


def serialize_obj(obj, file_name):
    with open(file_name, 'w') as results:
        results.write(str(obj))


file_path = 'text.txt'
results_path = 'results.txt'

try:
    #check if file exist
    with open(file_path, 'r') as file:
        text_readlines = file.readlines()

    text = ' '.join(text_readlines)

    #small notification for customer
    if len(text) != 0:
        text_nonalpha = []
        text_nonalpha = [1 for i in range(len(text)) if not text[i:i+1].isalpha()]
        freq_nonalpha = int(len(text_nonalpha) / len(text) * 100)

        if freq_nonalpha > 50:
            print(f'Notification! There are {freq_nonalpha}% not alpha symbols. Please check text in file {file_path}')
    
        try:
            #there is exeption in task_4 top_keywords function
            #it`s hardcoded to 3 keywords minimum in dictionary
            result_text = task_4(text)
            serialize_obj(result_text, results_path)
            print('all done!')
        except (IndexError, NameError) as error:
            print('Attention! text too short for analyze.', '\n', 'Error message:', error)
    else:
        try:
            raise ZeroDivisionError
        except ZeroDivisionError:
            print('Warnning! File is empty.')
except FileNotFoundError:
    print('File not found')
