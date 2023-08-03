import jieba

"""
这个好像有一点问题

"""
# 通过enable_paddle接口安装paddlepaddle-tiny，并且import相关代码；
jieba.enable_paddle()  # 初次使用可以自动安装并导入代码
seg_list = jieba.cut(str, use_paddle=True)
print('Paddle模式: ' + '/'.join(list(seg_list)))

