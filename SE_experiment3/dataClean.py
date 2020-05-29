import pandas as pd


def getWords(path='SE_experiment3/ox-edict-utf8.txt'):
    fp = open(path, 'r', encoding='utf-8')
    data = fp.readlines()
    fp.close()
    fp = open('SE_experiment3/words.txt', 'w+', encoding='utf-8')
    for i in range(len(data)):
        if(len(data[i]) < 20):
            fp.write(data[i])
    fp.close()


# 删除单词长度大于20或者开头不是字母的词条
def cleanDataFirst():
    path = 'SE_experiment3/ecdict.csv'
    delIndex = []
    data = pd.read_csv(path, low_memory=False)
    for i, word in enumerate(data.word):
        if(isinstance(word, str) and
           (len(word) > 20 or word[0].isalpha() is False)):
            delIndex.append(i)
    data = data.drop(delIndex, axis=0)
    data.to_csv('SE_experiment3/temp.csv', index=False)


# 删除没有音标的词条
def cleanDataSecond():
    path = 'SE_experiment3/temp.csv'
    data = pd.read_csv(path, low_memory=False)
    data.dropna(subset=['phonetic'], inplace=True)
    data.to_csv('SE_experiment3/temp.csv', index=False)


# 删除没用的信息
def cleanDataThird():
    path = 'SE_experiment3/temp.csv'
    data = pd.read_csv(path, low_memory=False)
    data.drop(['collins', 'oxford', 'tag', 'bnc', 'frq', 'audio'],
              axis=1, inplace=True)
    data.to_csv('SE_experiment3/temp.csv', index=False)


if __name__ == '__main__':
    cleanDataThird()
