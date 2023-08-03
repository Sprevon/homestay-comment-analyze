import warnings
import pyLDAvis.gensim

import gensim
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from gensim import corpora

from data.local_data_API import get_plain_text_column4, get_single_text_in_column4, get_num_rows
from model.split.accuracy.default import split_by_default

warnings.filterwarnings('ignore')
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel

content = get_plain_text_column4()
data_set = []
for i in range(get_num_rows()):
    seg_list = get_single_text_in_column4(i)
    spl_list = split_by_default(seg_list)
    data_set.append(spl_list)

dictionary = corpora.Dictionary(data_set)  # 构建词典
corpus = [dictionary.doc2bow(text) for text in data_set]  # 表示为第几个单词出现了几次

lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=30, random_state=1)
topic_list = lda.print_topics()
print(topic_list)

result_list = []
for i in lda.get_document_topics(corpus)[:]:
    listj = []
    for j in i:
        listj.append(j[1])
    bz = listj.index(max(listj))
    result_list.append(i[bz][0])
print(result_list)


pyLDAvis.enable_notebook()
data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(data, 'D:/Program/PyCharm/PycharmProjects/Homestay/model/output')

