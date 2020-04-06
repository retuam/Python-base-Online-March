def extract_text():
    """
    :description: Function call extracts a text from external file
    """
    try:
        with open('original_text.txt', 'r') as file:
            if not file.name.endswith('.txt'):
                raise TypeError
            text = file.readlines()
            text = list(text)
            text = ''.join(text)

        return text

    except FileNotFoundError:
        print('File doesn\'t exist')

    except TypeError:
        print('File extension is not ".txt"')


def create_file():
    """
    :description: Function call creates a txt file
    """
    file = open('result.txt', 'a')
    file.close()


def append_file(content):
    """
    :description: Function call appends created txt file
    """
    file = open('result.txt', 'a')
    file.write(content)
    file.close()


