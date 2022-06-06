file = open("Date_stocate.txt", 'rt')

def search_moderate_word(moderate_word):

    if (moderate_word == 'moderate'):
        read_data = file.read()
        word_count = read_data.lower().count(moderate_word)
        return word_count