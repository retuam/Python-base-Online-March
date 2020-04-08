def get_text(text_to_read):

    try:
        with open(text_to_read, 'r') as file:
            pretext = file.read()
        return pretext

    except FileNotFoundError as error:
        print('Wrong name of  txt file')

def text_output(text_out, text_output):
    try:
        with open(text_out, 'a') as new_file:
            new_file.write(str(text_output))

    except TypeError as error:
        print('only string can be used')