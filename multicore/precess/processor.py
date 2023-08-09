from data.local_data_API import get_single_text_in_column4, get_plain_text_column4
from data.split.accuracy.default import split_by_default


def worker_function(content, start, end, result_queue):
    data_set = []
    for i in range(start, end):
        seg_list = content.get_single_text_in_column4(i)
        spl_list = split_by_default(seg_list)  # 分词 + 去标点
        data_set.append(spl_list)
    result_queue.put(data_set)
