# 导入需要的库
import torch
import gensim

# 假设你有一个文档的数据集，每个文档是一个字符串列表，保存在变量docs中
docs = [
    ["我", "喜欢", "吃", "苹果"],
    ["你", "喜欢", "吃", "香蕉"],
    ["他", "喜欢", "吃", "橘子"],
    ["我们", "喜欢", "吃", "水果"]
]

# 用gensim创建一个词典，将每个词映射到一个整数id
dictionary = gensim.corpora.Dictionary(docs)

# 用gensim创建一个语料库，将每个文档转换为词频向量
corpus = [dictionary.doc2bow(doc) for doc in docs]

# 定义LDA模型的参数，比如主题数、迭代次数、学习率等
num_topics = 2 # 主题数
num_words = len(dictionary) # 词汇数
num_docs = len(corpus) # 文档数
max_iter = 100 # 迭代次数
alpha = 1.0 / num_topics # 文档-主题分布的先验参数
beta = 1.0 / num_topics # 主题-词分布的先验参数
lr = 0.01 # 学习率

# 用pytorch创建LDA模型，包括两个矩阵：theta（文档-主题分布）和phi（主题-词分布）
theta = torch.randn(num_docs, num_topics, requires_grad=True) # 随机初始化theta
phi = torch.randn(num_topics, num_words, requires_grad=True) # 随机初始化phi

# 定义LDA模型的损失函数，使用对数似然函数
def log_likelihood(theta, phi, corpus):
    ll = 0 # 对数似然值
    for d in range(num_docs): # 遍历每个文档
        doc = corpus[d] # 获取文档的词频向量
        for w, c in doc: # 遍历每个词及其出现次数
            ll += c * torch.log(torch.sum(theta[d] * phi[:, w])) # 累加对数似然值
    return ll

# 定义LDA模型的优化器，使用随机梯度下降法
optimizer = torch.optim.SGD([theta, phi], lr=lr)

# 训练LDA模型，迭代更新theta和phi
for i in range(max_iter): # 遍历每次迭代
    optimizer.zero_grad() # 清空梯度
    ll = log_likelihood(theta, phi, corpus) # 计算对数似然值
    loss = -ll # 计算损失值（负对数似然值）
    loss.backward() # 计算梯度
    optimizer.step() # 更新参数
    print(f"Iteration {i+1}, loss = {loss.item()}") # 打印损失值

# 输出LDA模型的结果，包括每个文档的主题分布和每个主题的词分布
print("Document-topic distribution:")
for d in range(num_docs): # 遍历每个文档
    print(f"Document {d}: {torch.softmax(theta[d], dim=0)}") # 输出文档的主题分布（归一化

print("Topic-word distribution:")
for t in range(num_topics): # 遍历每个主题
    print(f"Topic {t}:", end=" ") # 输出主题编号
    topic_words = torch.argsort(phi[t], descending=True) # 按照词的权重降序排序
    for w in topic_words[:10]: # 遍历前10个最相关的词
        print(dictionary[w.item()], end=" ") # 输出词
    print() # 换行
