
file = open("Date_stocate.txt", 'rt')

def search_light_word(light_word):

    if (light_word == 'light'):
        read_data = file.read()
        word_count = read_data.lower().count(light_word)
        return word_count
