import jieba


def split_by_default(content):
    seg_list = jieba.cut(content, cut_all=False)
    return seg_list


print("精准模式: " + "/ ".join(split_by_default("我来到北京清华大学")))
