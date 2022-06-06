file = open("Date_stocate.txt", 'rt')

def search_extreme_word(extreme_word):

    if (extreme_word == 'extreme'):
        read_data = file.read()
        word_count = read_data.lower().count(extreme_word)
        return word_count