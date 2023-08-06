import gensim
from gensim import corpora
from gensim.models import LdaModel
import jieba

# 指定的主题及其词汇列表
topics = {
    "Topic1": ["民宿", "环境", "干净"],
    "Topic2": ["服务", "态度", "亲切"],
    "Topic3": ["房间", "设施", "满意"],
    "Topic4": ["早餐", "美味", "推荐"],
    "Topic5": ["喜欢", "感觉", "下次"]
}

# 示例文本数据
documents = [
    "这个民宿的环境非常好，很干净。",
    "服务态度很好，小姐姐很亲切。",
    "房间设施很齐全，非常满意。",
    "早餐很美味，推荐大家来尝试。",
    "下次还会再来住，真的很喜欢这里的感觉。"
]


# 中文分词
def preprocess(text):
    words = jieba.cut(text)
    return list(words)


# 预处理文本数据
processed_documents = [preprocess(doc) for doc in documents]

# 构建词典，并将主题词汇添加进去
dictionary = corpora.Dictionary(processed_documents)
for topic_words in topics.values():
    dictionary.add_documents([topic_words])

# 构建文档-词频矩阵
corpus = [dictionary.doc2bow(doc) for doc in processed_documents]

# 训练 LDA 模型
num_topics = len(topics)
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

# 打印每个主题的关键词
for idx, topic_words in topics.items():
    topic_terms = [term for term, _ in lda_model.get_topic_terms(dictionary.doc2bow(topic_words))]
    print(f"{idx}: {topic_terms}")
