# -*- coding: utf-8 -*
import os
# import tensorflow as tf
import torch
from path import DATA_PATH, MODEL_PATH
from modelNet import ChatBotModel
from vocab import Vocab, VocabEntry
from data_helper import load_dict, text2id
from modelNet import get_tensor_name
# from flyai.framework import FlyAI


class Prediction(object):
    def __init__(self):
        ''' init
        '''
        self.BATCH = 1
        self.embedding_size = 64
        self.hidden_size = 1024
        self.device = torch.device('cpu')
        if torch.cuda.is_available():
            self.device = torch.device('cuda:0')
        self.load_model()

    def load_model(self):
        '''
        模型初始化，必须在构造方法中加载模型
        '''
        # 加载词典
        src_vocab = VocabEntry(os.path.join(DATA_PATH, 'MedicalQA/test/src.dict'))
        tgt_vocab = VocabEntry(os.path.join(DATA_PATH, 'MedicalQA/test/tgt.dict'))
        self.vocab = Vocab(src_vocab, tgt_vocab)
        # 加载模型
        self.model = ChatBotModel(self.BATCH, self.embedding_size, self.hidden_size, vocab=self.vocab, droprate=0.2)
        self.load_model_file(self.model)
        self.model.to(self.device)
        self.model.eval()

    def predict(self, department, title, ask):
        '''
        模型预测返回结果
        :param input: 评估传入样例 {"department": "心血管科", "title": "心率为72bpm是正常的吗",
                                    "ask": "最近不知道怎么回事总是感觉心脏不舒服..."}
        :return: 模型预测成功中户 {"answer": "心脏不舒服一般是..."}
        '''
        src = department + title + ask
        src_x, src_len = self.vocab.src.sent2ids(title + ask)
        src_len = [src_len]
        predict = self.model.predict(src_x, src_len)
        predict = predict.squeeze_().tolist()
        result_list = list()
        for item in predict:
            if item != self.vocab.tgt.unk_id:
                result_list.append(self.vocab.tgt.id2text.get(item, self.vocab.tgt.unk))
        result = ''.join(result_list)

        return {'answer': result}
    
    def save_model(self, model):
        torch.save(model.state_dict(), 'data/output/model/model.pkl')
    
    def load_model_file(self, model):
        model.load_state_dict(torch.load('data/output/model/model.pkl'))


if __name__ == "__main__":
    Pre = Prediction()
    department = "心血管科"
    title = "心率为72bpm是正常的吗"
    ask = "最近不知道怎么回事总是感觉心脏不舒服..."
    print(Pre.predict(department, title, ask))