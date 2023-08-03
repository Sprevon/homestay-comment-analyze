import jieba
import jieba.analyse

from data import local_data_API

content = local_data_API.get_plain_text_column4()
tags = jieba.analyse.extract_tags(content,topK=20,withWeight=True,allowPOS=("nr"))
print(tags)

