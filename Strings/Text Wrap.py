def wrap(string, max_width):
    new_string = ''
    for i in range(0, len(string), max_width):
        new_string += string[i : i + max_width] + '\n'

    return new_string.strip()