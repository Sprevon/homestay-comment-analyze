import pkuseg
import string
import torch


# 自定义停用词列表
def load_stop_words():
    # 加载你的停用词列表
    return ["的", "了", "很", "也", "非常", "在", "还", "和", "都", "有", "就", "好", "进", "大", "多", "会", "人",
            "我", "看", "去", "不", "老板", "朋友"]


def split_by_default(content, seg_model):
    # 去除标点和停用词
    translator = str.maketrans('', '', string.punctuation + "\n 。. ， 、 ； ： ？！ “” ‘’ … ")

    stop_words = load_stop_words()
    for word in stop_words:
        translator[word] = None

    joined_words = ' '.join(content)
    new_content = joined_words.translate(translator)

    # 使用 pkuseg 分词
    seg_list = seg_model.cut(new_content)
    return seg_list


# 创建 pkuseg 分词器并设置为 GPU 模式
seg_model = pkuseg.pkuseg(model_name="web", postag=False, user_dict=None, use_gpu=True)

# 要进行分词的文本
content = ["我喜欢自然语言处理。", "今天天气很好。"]

# 使用 pkuseg 进行分词
seg_results = split_by_default(content, seg_model)

print(seg_results)
