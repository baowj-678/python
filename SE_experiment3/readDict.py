import pandas as pd

class Dictionary:
    def __init__(self, path='SE_experiment3/ox-edict-utf8.txt'):
        self.Dict = None
        self.path = path
        self.readFile()

    def readFile(self):
        # try:
        #     fp = open(self.path, 'r', encoding='utf-8')
        # except FileNotFoundError:
        #     print('文件不存在！')
        # else:
        #     print('read file......')
        #     self.Dict = fp.readlines()
        #     print('read file successfully')
        #     for i in range(10):
        #         print(self.Dict[i])
        #     print(len(self.Dict))
        #     fp.close()
        fp = pd.read_csv(self.path)
        fp.drop()
        print(type(fp))


if __name__ == '__main__':
    dictt = Dictionary('SE_experiment3/ecdict.mini.csv')
