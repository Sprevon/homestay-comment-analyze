import multiprocessing
import time
import warnings
from multiprocessing import Pool

from gensim import corpora

from data.local_data_API import get_plain_text_column4, get_single_text_in_column4, get_num_rows
from data.local_data_API_new import LoadData
from data.split.accuracy.default import split_by_default
from multicore.precess.processor import worker_function

warnings.filterwarnings('ignore')
from gensim.models.ldamodel import LdaModel

"""
知乎教程：https://www.zhihu.com/search?type=content&q=LDA%E4%B8%BB%E9%A2%98%E6%A8%A1%E5%9E%8B
NLTK库：https://www.nltk.org/index.html
隐含主题学习教程：https://blog.csdn.net/baidu_18607797/article/details/40511755?ops_request_misc=&request_id=&biz_id=102&utm_term=LDA%E5%BD%92%E7%BA%B3%E9%9A%90%E5%BD%A2%E4%B8%BB%E9%A2%98&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-40511755.142^v92^insert_down1&spm=1018.2226.3001.4187
"""


def compute_mul(start, end):
    start_time = time.time()
    # 创建数据集
    load_data = LoadData()
    data_set = []
    # 参数初始化
    num_processes = 3
    step = (end - start) // num_processes
    processes = []
    result_queue = multiprocessing.Queue()

    for i in range(num_processes):
        process_start = start + i * step
        process_end = process_start + step if i < num_processes - 1 else end
        process = multiprocessing.Process(target=worker_function,
                                          args=(load_data, process_start, process_end, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    result_data = []
    while not result_queue.empty():
        result_data.extend(result_queue.get())
    print("All processed completed.")

    data_set = result_data
    # print(data_set)

    dictionary = corpora.Dictionary(data_set)  # 构建词典
    corpus = [dictionary.doc2bow(text) for text in data_set]  # 表示为第几个单词出现了几次

    # 构建模型
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=20, random_state=1)
    topic_list = lda.print_topics()
    print(topic_list[0])
    print(topic_list[1])
    print(topic_list[2])
    print(topic_list[3])
    print(topic_list[4])

    # 输出主题概率分布
    result_list = []
    for i in lda.get_document_topics(corpus)[:]:
        listj = []
        for j in i:
            listj.append(j[1])
        bz = listj.index(max(listj))
        result_list.append(i[bz][0])

    end_time = time.time()
    elapse_time = end_time - start_time
    print("time-mult:", elapse_time)
