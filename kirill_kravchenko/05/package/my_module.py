# Use your Task 4 to finish Task 5.
#
# Additional features:
# - Module that provide a possibility to:
# -- Extract a text from text.txt file;
# -- Save results to results.txt file;
# - Run your logic only if the main file was executed;
# - Try to handle as much exceptions as possible.
def extract_file(file_name='text.txt'):
    """
    This is function extract a text from text.txt file
    :param file_name: file name
    :type file_name: string
    :return: result string
    :rtype: str
    """
    try:

        with open(file_name, 'r') as file:
            text = file.read()

        return text

    except FileNotFoundError:

        print('No file exist')


def save_result(obj, file_name='results.txt'):
    """
    This is function save results to results.txt file
    :param obj: output data
    :type obj: string
    :param file_name: file name
    :type file_name: string
    """
    with open(file_name, 'w') as file:
        file.write(str(obj))