import jieba

jieba.set_dictionary("./jieba/dict.txt")
jieba.initialize()

import jieba.posseg as pseg

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

words = pseg.cut("我爱北京天安门") #jieba默认模式
print(list(words))
