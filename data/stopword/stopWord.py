def load_stop_words():
    with open('stopwords.txt', 'r', encoding='utf-8') as file:
        stop_words = [line.strip() for line in file.readlines()]
    return stop_words

# print(load_stop_words())