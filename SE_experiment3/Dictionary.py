import pandas as pd


class Dictionary:
    def __init__(self, path='SE_experiment3/edict.mini.csv'):
        self.data = None
        self.path = path
        self.readFile(self.path)

    def readFile(self, path: str):
        try:
            print('reading data........')
            self.data = pd.read_csv(self.path, low_memory=False)
            self.nums = self.data.shape[0]
            print('success........')
        except(Exception):
            print('read data fail......')
        finally:
            return self.data

    def search(self, word: str, isGetIndex=False):
        if(self.data is None):
            self.readFile(self.path)
        point, word_ = 0, self.data['word'][0]
        left, right = 0, self.nums - 1
        while(word_ != word and left < right):
            if(word > word_):
                left = point
            else:
                right = point
            point = (left + right) // 2
            word_ = self.data['word'][point]
        if(word_ == word):
            if(isGetIndex):
                return point
            else:
                return self.data.loc[point]
        else:
            print('There is no this word......')
            return None

    def getTranslation(self, word: str) -> list:
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        return wordInfo['translation'].split('\\n')

    def getDefinition(self, word: str) -> list:
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        return wordInfo['definition'].split('\\n')

    def getPhonetic(self, word: str):
        wordInfo = self.search(word)
        return wordInfo['phonetic']

    def getQuerry(self, word: str, querry: list):
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        ans = []
        for i, v in wordInfo.items():
            ans.append(v)
        return ans

    def getSentences(self, word: str) -> list:
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        return wordInfo['sentences'].split('\\n')

    def setSentence(self, word: str, a: str):
        index = self.search(word, isGetIndex=True)
        self.data.loc[index, 'sentences'] = a

    def saveTo(self, newPath=''):
        if(newPath == ''):
            self.data.to_csv(self.path, index=False)
        else:
            self.data.to_csv(newPath, index=False)


if __name__ == '__main__':
    print('hello\n')
    dictt = Dictionary('SE_experiment3/ecdict.mini.csv')
