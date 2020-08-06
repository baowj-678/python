# 1 导入相关库
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread
import warnings
warnings.filterwarnings("ignore")


# 2 读取文本文件，并使用lcut()方法进行分词
with open("LittleDemo/GetBiliBiliBarrage/lbxx-barrage.txt",
          mode='r',
          encoding="utf-8") as f:
    txt = f.read()
txt = txt.split()
data_cut = [jieba.lcut(x) for x in txt]


# 5 词频统计
all_words = []
for i in data_cut:
    for j in i:
        if(len(j) > 1):
            all_words.append(j)
word_count = pd.Series(all_words).value_counts()

# 6 词云图的绘制
# 1）读取背景图片
back_picture = imread("LittleDemo/GetBiliBiliBarrage/mask.png")

# 2）设置词云参数
wc = WordCloud('simhei.ttf',
               background_color='white',
               width=5000,
               height=5000,
               max_words=200,
               mask=back_picture,
               mode='RGBA',
               max_font_size=1000,
               random_state=42
               )
wc2 = wc.fit_words(word_count)

# 3）绘制词云图
plt.figure(figsize=(16, 8))
plt.imshow(wc2)
plt.axis("off")
plt.show()
wc.to_file("LittleDemo/GetBiliBiliBarrage/lbxx.png")