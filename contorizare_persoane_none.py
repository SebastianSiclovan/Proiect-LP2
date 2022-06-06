file = open("Date_stocate.txt", 'rt')

def search_none_word(none_word):

    if (none_word == 'none'):
        read_data = file.read()
        word_count = read_data.lower().count(none_word)
        return word_count
