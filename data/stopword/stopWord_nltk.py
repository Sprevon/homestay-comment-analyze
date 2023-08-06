import nltk

nltk.download('stopwords')


class StopWord:
    def __int__(self):
        self.stop_words = set(nltk.corpus.stopwords.words('chinese'))

    def del_stop_word(self, content):
        before = content
        after = [w for w in before if w not in self.stop_words]
        return after


print(StopWord().del_stop_word('我要去广州旅游了'))
