import jieba
import pandas as pd
import json
import os

class VocabEntry(object):
    def __init__(self, file_path):
        ''' 初始化字典入口类
        @param file_path: 字典路径
        '''
        self.text2id = None
        self.id2text = None
        self.file_path = file_path
        self.pad = '_pad_'
        self.unk = '_unk_'
        self.sos = '_sos_'
        self.eos = '_eos_'
        self.unk_id = 0
        self.pad_id = 0#10000
        self.sos_id = 0#20000
        self.eos_id = 0#30000
        self.load_dict(self.file_path)
    
    def __len__(self):
        ''' 返回Vocab长度
        @return len: 总的词汇长度
        '''
        return len(self.text2id)
    
    def __getitem__(self, word):
        ''' 返回text对应的id，不存在则返回 '_unk_'
        @param word: str, 查询的文本
        @param id: int, 对应的id
        '''
        return self.text2id.get(word, self.unk_id)
    
    def __contains__(self, word):
        ''' word词语是否在词典中
        @param contains(bool): 是否存在
        '''
        return word in self.text2id

    def load_dict(self, dictFile):
        ''' 加载字典
        @param: 字典路径
        @return text2id: dict, 根据文本查找id的字典
        @return id2text: dict, 根据id查找文本的字典
        '''
        if not os.path.exists(dictFile):
            print('[ERROR] load_dict failed! | The params {}'.format(dictFile))
            return None
        with open(dictFile, 'r', encoding='UTF-8') as df:
            dictF = json.load(df)
        self.text2id, self.id2text = dict(), dict()
        count = 0
        for key, value in dictF.items():
            self.text2id[key] = count
            self.id2text[count] = key
            count += 1
        self.text2id[self.unk] = self.unk_id
        self.text2id[self.sos] = self.sos_id
        self.text2id[self.eos] = self.eos_id
        self.text2id[self.pad] = self.pad_id
        self.id2text[self.unk_id] = self.unk
        self.id2text[self.sos_id] = self.sos
        self.id2text[self.eos_id] = self.eos
        self.id2text[self.pad_id] = self.pad
        return self.text2id, self.id2text

    def id2text(self, id):
        return self.id2text[id]
    
    def text2id(self, text):
        return self.text2id[text]
    
    def add(self, word):
        """ Add word to VocabEntry, if it is previously unseen.
        @param word (str): word to add to VocabEntry
        @return index (int): index that the word has been assigned
        """
        if word not in self.word2id.keys():
            wid = self.text2id[word] = len(self)
            self.id2text[wid] = word
            return wid
        else:
            return self.text2id[word]

    def text2words(self, textline):
        ''' 对一句话进行分词
        @param textline: str, 文本
        @param text_list: list, 分词后的token list
        @param text_len: 分词后的list长度
        '''
        textline = jieba.lcut(textline)
        text_list = list()
        text_list = [self.eos] + textline
        text_len = len(text_list)
        return text_list, text_len

    def words2ids(self, words):
        ''' 将分词的list转成id的list
        @param words (List[str]): 分词的list
        @return ids (List[int]): 对应id的list
        '''
        return [self.text2id.get(w, self.unk_id) for w in words]

    def sent2ids(self, sents):
        ''' 将一个句子str转成 List[id]
        @param sents (str): 句子
        @return word_ids ([list[int]): 句子的表征
        @return text_len (int): 句子长度
        '''
        text_list, text_len = self.text2words(sents)
        ids_list = self.words2ids(text_list)
        return (ids_list, text_len)

    def ids2words(self, word_ids):
        ''' 将ids转成分词
        @param word_ids (list[int]): id的列表
        @return sents (List[str]): 分词的列表
        '''
        return [self.id2text.get(w_id, self.unk) for w_id in word_ids]
    
    def ids2sents(self, word_ids):
        ''' 将ids转成句子
        @param word_ids List[int]: id列表
        @return sents (str): 句子
        '''
        return ''.join(self.ids2words(word_ids))

class Vocab(object):
    def __init__(self, src_vocab: VocabEntry, tgt_vocab: VocabEntry):
        """ Init Vocab.
        @param src_vocab (VocabEntry): VocabEntry for source language
        @param tgt_vocab (VocabEntry): VocabEntry for target language
        """
        self.src = src_vocab
        self.tgt = tgt_vocab


# if __name__ == '__main__':
    

