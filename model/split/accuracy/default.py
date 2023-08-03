import jieba
import string


def split_by_default(content):

    # 去除标点
    translator = str.maketrans('', '', string.punctuation + "\n 。 ， 、 ； ： ？！ “” ‘’ … ")
    joined_words = ' '.join(content)
    new_content = joined_words.translate(translator)
    # 分词
    seg_list = jieba.cut(new_content, cut_all=False)
    return list(seg_list)


# print(split_by_default("我来,到北京清华大学"))
