import emoji
import jieba
import string

from data.stopword.stopWord import load_stop_words


def split_by_default(content):
    # 去emoji
    content = emoji.replace_emoji(content, "")
    # 去除标点
    translator = str.maketrans('', '', string.punctuation + "\n 。 ， 、 ； ： ？！ “” ‘’ … "
                               + "的 了 很 也 非常 在 还 来 是 接 小姐姐 到 "
                                 "和 都 有 就 好 进 大 多 会 人 我 看 去 不 老板"
                                 "朋友 我们 比较 一边 体现 用 ~ ⁓ ～ 门口 太 一个 不 过 房间 们 住"
                                 "让 那种 走 赞 带 睡 挺 亲自 下次 房间 真 让 干净 位置 给"
                               # "这 着 第三 咯噔 睁 必住 酒店 吧 老板 床 地方 觉"
                                 "齐全 各 没 条街 日本 蛮 入 错金 毛萌萌 两趟"
                                 "雨天 西塘 图片 可以 阿姨 晚上 时候"
                               # "民宿 给 便 真 空调 说 里 你 里面 性 "
                                 "特别 喜欢 推荐 满意 找 再 哦 票 楼 近 选择"
                                 "早餐 订 高 买 淡淡 啊 但 聊 联系 点"
                                 "说 这 要 感觉 你 能"
                                 "差  吃 着 吧 么 只 着 着 娘 把"
                                 "知道 后 得 又 她 因为"
                                 "超级 里 离 而且 前台"
                               )
    stop_words = load_stop_words()
    for word in stop_words:
        translator[word] = None

    joined_words = ' '.join(content)
    new_content = joined_words.translate(translator)
    # 分词
    seg_list = jieba.cut(new_content, cut_all=False)
    return list(seg_list)


# print(split_by_default("我来,到北京清华大学😍😍😍"))


def just_split(content):
    seg_list = jieba.cut_for_search(content)
    return list(seg_list)
