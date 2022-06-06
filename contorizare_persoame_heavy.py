file = open("Date_stocate.txt", 'rt')

def search_heavy_word(heavy_word):

    if (heavy_word == 'heavy'):
        read_data = file.read()
        word_count = read_data.lower().count(heavy_word)
        return word_count