import pandas as pd


class Dictionary:
    def __init__(self, path='SE_experiment3/temp.csv'):
        self.data = None
        self.path = path
        self.readFile(self.path)

    def readFile(self, path: str):
        try:
            print('reading data........')
            self.data = pd.read_csv(path, low_memory=False)
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
        while(left <= right):
            point = (left + right) // 2
            word_ = self.data['word'][point]
            if(word == word_):
                break
            elif(word > word_):
                left = point + 1
            else:
                right = point - 1
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
        elif(pd.isnull(wordInfo['translation'])):
            return None
        else:
            return wordInfo['translation'].split('\\n')

    def getDefinition(self, word: str) -> list:
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        elif(pd.isnull(wordInfo['definition'])):
            return None
        else:
            return wordInfo['definition'].split('\\n')

    def getPhonetic(self, word: str):
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        elif(pd.isnull(wordInfo['phonetic'])):
            return None
        return wordInfo['phonetic'].split('\\n')

    def getQuerry(self, word: str, querry: list):
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        ans = []
        for i, v in wordInfo[querry].items():
            if(i in ('definition', 'translation', 'sentences')):
                if(pd.isnull(v)):
                    ans.append(None)
                else:
                    ans.append(v.split('\\n'))
            elif(i == 'exchange'):
                if(pd.isnull(v)):
                    ans.append(None)
                else:
                    ans.append(v.split('/'))
            else:
                if(pd.isnull(v)):
                    ans.append(None)
                else:
                    ans.append(v)
        return ans

    def getSentences(self, word: str) -> list:
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        elif(pd.isnull(wordInfo['sentences'])):
            return None
        return wordInfo['sentences'].split('\\n')

    def getExchange(self, word: str):
        wordInfo = self.search(word)
        if(wordInfo is None):
            return None
        elif(pd.isnull(wordInfo['exchange'])):
            return None
        return wordInfo['exchange'].split('/')

    def saveTo(self, newPath=''):
        if(newPath == ''):
            self.data.to_csv(self.path, index=False)
        else:
            self.data.to_csv(newPath, index=False)
    
    
    def setSentence(self, word: str, a: str):
        index = self.search(word, isGetIndex=True)
        if(index is None):
            return None
        self.data.loc[index, 'sentences'] = a


Dict = Dictionary()
Dict.getExchange('exchange')
# if __name__ == '__main__':
#     print('hello\n')
#     dictt = Dictionary('SE_experiment3/ecdict.mini.csv')