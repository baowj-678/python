import jieba

seg_list = jieba.cut('我来自华中科技大学')
print("Default Mode: " + "/ ".join(seg_list))
