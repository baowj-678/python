# -*- coding: utf-8 -*- 
# author: Honay.King

import os
import json
import jieba
import pandas as pd


def load_dict(dictFile):
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
    text2id, id2text = dict(), dict()
    count = 0
    for key, value in dictF.items():
        text2id[key] = count
        id2text[count] = key
        count += 1
    return text2id, id2text


def text2id(textline, target_dict):
    ''' 将一句话分词并转成其id
    @param textline: str，一句话
    @param target_dict: dict,目标语言的字典

    @return text_list: list，id的list
    @return text_len: 分词后的长度
    '''
    textline = jieba.lcut(textline)
    text_list = list()
    for i in range(len(textline)):
        if textline[i] in target_dict.keys():
            text_list.append(target_dict[textline[i]])
        else:
            text_list.append(target_dict['_unk_'])
    text_len = len(text_list)
    return text_list, text_len

def id2text(text_list, target_dict):
    ''' 根据id的list，返回str的文本内容

    @param text_list: list, id的list
    @param target_dict: dict目标的id2text字典
    '''
    textline = []
    for i in range(len(text_list)):
        textline.append(target_dict[text_list[i]])
    return ''.join(textline)

def text_cut(textline):
    ''' 对文本进行分词并添加 _unk_

    @param textline: str, 文本

    @param text_list: list, 分词后的token list
    @param text_len: 分词后的list长度
    '''
    textline = jieba.lcut(textline)
    text_list = list()
    text_list.append('_unk_')
    text_len = len(text_list)
    return text_list, text_len

def raed_data_text(data, source_dict, target_dict):
    ''' 读取数据,返回文本的id编码
    @param data: csv的训练数据
    @param source_dict: dict, text->id字典
    @param target_dict: dict, text->id字典

    @return source_list: List[List[int]], 输入语句的 文本, [sents_num, seq_len]
    @return target_list: List[List[int]], 目标语句的 id, [sents_num, seq_len]
    @return source_lens: List[int], 每句话的长度(未padding), [sents_num]
    '''
    source_list = []
    target_dict = []
    source_lens = []
    target_lens = []
    for ind, row in data.iterrows():
        source, source_len = text_cut(row['title']+row['ask'], source_dict)
        source_list.append(source)
        source_lens.append(source_len)
        target, target_len = text2id(row['answer'], target_dict)
        target_list.append(target)
        target_lens.append(target_len)
    return [source_list, source_lens], [target_list, target_lens]

def read_data_id(data, source_vocab, target_vocab):
    ''' 读取数据,返回文本的id编码
    @param data: csv的训练数据
    @param source_dict: dict, text->id字典
    @param target_dict: dict, text->id字典

    @return source_list: List[List[int]], 输入语句的id, [sents_num, seq_len]
    @return target_list: List[List[int]], 目标语句的id, [sents_num, seq_len]
    @return source_lens: List[int], 每句话的长度(未padding), [sents_num]
    '''
    source_list, source_lens, target_list, target_lens = list(), list(), list(), list()
    for ind, row in data.iterrows():
        # 将title department ask 合起来转成id作为输入
        source, source_len = source_vocab.sent2ids(row['department'] + row['title'] + row['ask'])
        source_list.append(source)
        source_lens.append(source_len)
        target, target_len = target_vocab.sent2ids(row['answer'])
        target_list.append(target)
        target_lens.append(target_len)
    return [source_list, source_lens], [target_list, target_lens]


def pad_sentence_batch(sentence_batch, padding='_pad_'):
    '''
    对batch中的序列进行补全，保证batch中的每行都有相同的sequence_length
    参数：
    - sentence batch
    - padding: <PAD>对应索引号
    '''
    max_sentence = max([len(sentence) for sentence in sentence_batch])
    return [sentence + [padding] * (max_sentence - len(sentence)) for sentence in sentence_batch]


def get_batches(targets, sources, batch_size, src_vocab, tgt_vocab):
    ''' 获取一个batch的数据
    @param targets: 输出的语句
    @param sources: 输入的语句
    @param batch_size: batch大小
    @param source_padding: padding
    @param target_padding: padding

    @return pad_target_batch: List[List[int]], 一个batch的padding好的目标数据, [batch_size, seq_len]
    @return pad_sources_batch: List[List[int]], 一个batch的padding好的输入数据, [batch_size, seq_len]
    @return target_len_batch, source_len_batch: List[int], 句子原始长度不包括_eos_
    '''
    source_list, source_lens = sources
    target_list, target_lens = targets
    for batch_i in range(0, len(source_list)//batch_size):
        start_i = batch_i * batch_size
        source_batch = source_list[start_i: start_i + batch_size]
        source_len_batch = source_lens[start_i: start_i + batch_size]
        target_batch = target_list[start_i: start_i + batch_size]
        target_len_batch = target_lens[start_i: start_i + batch_size]
        # paadding
        pad_sources_batch = pad_sentence_batch(source_batch, src_vocab.pad_id)
        pad_targets_batch = pad_sentence_batch(target_batch, tgt_vocab.pad_id)
        # sort
        source = zip(source_len_batch, pad_sources_batch)
        source = sorted(source, reverse=True)
        source_len_batch, pad_sources_batch = zip(*source)

        target = zip(target_len_batch, pad_targets_batch)
        target = sorted(target, reverse=True)
        target_len_batch, pad_targets_batch = zip(*target)
        yield pad_targets_batch, pad_sources_batch, target_len_batch, source_len_batch

    
if __name__ == "__main__":


    # 测试predict是否OK

    from prediction import Prediction

    model = Prediction()
    model.load_model()

    result = model.predict(department='', title='孕妇经常胃痛会影响到胎儿吗',
                           ask='"我怀上五个多月了,自从怀上以来就经常胃痛(两个胸之间往下一点儿是胃吧?)有时痛十几分钟,有时痛'
                               '半个钟,每次都痛得好厉害,不过痛过这一阵之后就不痛了,我怀上初期饮食不规律,经常吃不下东西,会不'
                               '会是这样引发的呀?我好忧心对胎儿有影响,该怎么办呢?可有食疗的方法可以纾解一下痛呢?"')
    print(result)

    exit(0)
