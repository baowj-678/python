# -*- coding: utf-8 -*-

import os
import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_packed_sequence, pack_padded_sequence
import torch.nn.functional as F
# from elmoformanylangs import Embedder

# e = Embedder('zhs.model')

# sents = [['今', '天', '天气', '真', '好', '阿'],
# ['潮水', '退', '了', '就', '知道', '谁', '沒', '穿', '裤子']]
# # the list of lists which store the sentences 
# # after segment if necessary.

# print(e.sents2elmo(sents).shape)

class Encoder(nn.Module):
    def __init__(self, batch_size, embed_size, hidden_size, droprate=0.2, predict=False):
        ''' EncoderModel

        @param batch_size (int): batch size
        @param embed_size (int): Embedding size (dimensionality)
        @param hidden_size (int): Hidden Size, the size of hidden states (dimensionality)
        @param droprate (float): Dropout probability
        '''
        super(Encoder, self).__init__()

        self.batch_size = batch_size
        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.droprate = droprate

        # 双向LSTM层
        self.LSTM = nn.LSTM(self.embed_size,
                            self.hidden_size,
                            num_layers=2,
                            batch_first=True,
                            dropout=self.droprate,
                            bidirectional=True)
        # 全连接层，2*hidden_size -> hidden_size
        self.embedding = nn.Embedding(num_embeddings=self.embed_size, embedding_dim=self.embed_size)
        self.h_projection = nn.Linear(2*hidden_size, hidden_size, bias=False)
        self.c_projection = nn.Linear(2*hidden_size, hidden_size, bias=False)


    def forward(self, source_padded, source_len_batch):
        ''' 前向传播
        @param source_padded (List): 训练数据，已经排序, tensor(batch_size, seq_len, embed_size)
        @param source_len_batch (List[int]): 句子长度
        @return (h_n, c_n): (h_n, c_n): tensor(batch, hidden_size*2)
        '''
        # 压紧数据
        source_padded = self.embedding(source_padded)  #tensor(batch_size, seq_len, embed_size)
        print(source_padded.shape)
        source_padded = source_padded.permute(1, 0, -1) #tensor(seq_len, batch_size, embed_size)
        inputt = pack_padded_sequence(source_padded, source_len_batch) #(seq_len, batch, embed_size)
        

        # LSTM
        output, (h_n, c_n) = self.LSTM(inputt) 
        # output:tensor(seq_len, batch, hidden_size * num_directions)
        # h_n(num_layers * num_directions, batch, hidden_size)
        # c_n(num_layers * num_directions, batch, hidden_size)

        # 获取LSTM最后一层双向的c_n，h_n
        h_n = torch.cat((h_n[-1], h_n[-2]), dim=1) # h_n:tensor(batch, hidden_size*2)
        c_n = torch.cat((c_n[-1], c_n[-2]), dim=1) # c_n:tensor(batch, hidden_size*2)

        # 经过全连接层
        h_n = self.h_projection(h_n) # h_n:tensor(batch, hidden_size)
        c_n = self.c_projection(c_n) # c_n:tensor(batch, hidden_size)
        return (h_n, c_n)


class Decoder(nn.Module):
    def __init__(self, batch_size, embed_size, hidden_size, droprate, tgt_vocab, device):
        ''' DecoderModel
        @param batch_size (int): batch size
        @param embed_size (int): Embedding size (dimensionality)
        @param hidden_size (int): Hidden Size, the size of hidden states (dimensionality)
        @param droprate (float): Dropout probability
        '''
        super(Decoder, self).__init__()
        # 最大句子长度
        self.max_length = 50
        self.batch_size = batch_size
        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.droprate = droprate
        self.tgt_vocab = tgt_vocab
        self.device = device
        self.start = None

        # init model
        self.LSTMCell = nn.LSTMCell(self.hidden_size,# + self.hidden_size,
                            self.hidden_size)
        # self.LSTM = nn.LSTM(self.embed_size,
        #                     self.hidden_size,
        #                     num_layers=2,
        #                     batch_first=True,
        #                     dropout=self.droprate,
        #                     bidirectional=True)
        self.embedding = nn.Embedding(num_embeddings=len(tgt_vocab), embedding_dim=embed_size)
        self.dropout = nn.Dropout(self.droprate)
        self.embedding_to_hidden = nn.Linear(self.embed_size, self.hidden_size, bias=False)
        self.out = nn.Linear(self.hidden_size, len(tgt_vocab))
        self.combined_output_projection = nn.Linear(hidden_size, hidden_size, bias=False)
        
    # def step(self, input, dec_state):
    #     ''' 计算decoder一个步骤的计算

    #     @param input (tensor): tensor(batch, embed_size + hidden_size),输入数据
    #     @param dec_state (tuple): (hidden_last, cell_last),上一步骤的输出 
    #     '''
    #     dec_state = self.LSTMCell(input, dec_state) # (hidden_last, cell_last)
    #     return dec_state


    def forward(self, hidden, target_padded, target_len_batch):
        ''' 句子不带_sos_带_eos_
        @param hidden (h_n, c_n): (h_n, c_n): tensor(batch, hidden_size)
        @param target_padded List[List[]]: (batch_size, seq_len)
        @return
        '''
        # 训练
        output = []
        # 对target进行embedding
        # hidden_last, cell_last = inputt #(h_n, c_n): tensor(batch, hidden_size)
        embedded = self.embedding(target_padded).permute(1, 0, -1)  # (batch_size, seq_len, embed_size)
        embedded = self.embedding_to_hidden(embedded)
        embedded = self.dropout(embedded) # (seq_len, batch_size, hidden_size)

        seq_len = embedded.shape[0]
        # 开始训练
        for i in range(seq_len - 1):
            hidden = self.LSTMCell(embedded[i], hidden)
            output_i = self.combined_output_projection(hidden[0])
            output_i = torch.tanh(output_i)
            output.append(output_i)
        output = torch.stack(output, dim=0)
        # output (seq_len, batch, hidden_size * num_directions)
        output = output.permute(1, 0, 2)
        output = F.log_softmax(self.out(output), dim=-1)
        # tensor (batch, seq_len, vocab_len)
        return output

    
    def predict(self, hidden):
        # 对_eos_进行embedding
        output = []
        if(self.start is None):
            self.start = self.embedding_to_hidden(self.embedding(torch.tensor(self.tgt_vocab.sos_id, dtype=torch.long, device=self.device))).unsqueeze_(dim=0)
            # start: tensor(1, hidden_size)
        hidden = self.LSTMCell(self.start, hidden)
        output_i = self.combined_output_projection(hidden[0])
        output_i = torch.tanh(output_i)
        output.append(output_i)
        for i in range(self.max_length - 1):
            hidden = self.LSTMCell(output_i, hidden)
            output_i = self.combined_output_projection(hidden[0])
            output_i = torch.tanh(output_i)
            output.append(output_i)
        output = torch.stack(output, dim=0)
        # output (seq_len, batch, hidden_size * num_directions)
        output = output.permute(1, 0, 2)
        output = F.log_softmax(self.out(output), dim=-1)
        # output: tensor (batch, seq_len, vocab_len)
        return output


class ChatBotModel(nn.Module):
    def __init__(self, batch_size, embed_size, hidden_size, vocab, droprate=0.2):
        ''' Init ChatBotModel

        @param embed_size (int): Embedding size (dimensionality)
        @param hidden_size (int): Hidden Size, the size of hidden states (dimensionality)
        @param vocab (Vocab): Vocabulary object containing src and tgt languages
                              See vocab.py for documentation.
        @param dropout (float): dropout probability
        '''
        super(ChatBotModel, self).__init__()
        if torch.cuda.is_available():
            self.device = torch.device('cuda:0')
        else:
            self.device = torch.device('cpu')
        self.batch_size = batch_size
        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.droprate = droprate
        self.vocab = vocab
        # embed fun
        self.embed = nn.Embedding(num_embeddings=len(self.vocab.src),
                                  embedding_dim=embed_size,
                                  padding_idx=self.vocab.src.pad_id)
        # encoder
        self.encoder = Encoder(batch_size=batch_size,
                               embed_size=embed_size,
                               hidden_size=hidden_size,
                               droprate=droprate)
        # decoder
        self.decoder = Decoder(batch_size=batch_size,
                               embed_size=embed_size,
                               hidden_size=hidden_size,
                               droprate=droprate,
                               tgt_vocab=self.vocab.tgt,
                               device=self.device)

        # model init

    def forward(self, pad_targets_batch, pad_sources_batch, target_len_batch, source_len_batch):
        ''' 前向传播
        @param pad_sources_batch: 输入数据(文本), 已经padding, (List[List[str]]), [batch_size, seq_len]
        @param pad_targets_batch: 目标输出(id), 已padding, (List[List[str]]), [batch_size, seq_len]
        @param target_len_batch: List[int], 每个句子的原始长度
        @param source_len_batch: List[int], 每个句子的原始长度

        @return score: 损失分数
        '''
        # 将list转成tensor(未embed)
        source_padded = torch.tensor(pad_sources_batch, dtype=torch.long, device=self.device)
        # self.vocab.src.to_input_tensor(pad_sources_batch, device=self.device)   # Tensor: (batch_size, seq_len)
        source_len_batch = torch.tensor(source_len_batch, dtype=torch.long, device=self.device)
        target_padded = torch.tensor(pad_targets_batch, dtype=torch.long, device=self.device)
        # self.vocab.tgt.to_input_tensor(pad_targets_batch, device=self.device)   # Tensor: (batch_size, seq_len)
        target_len_batch = torch.tensor(target_len_batch, dtype=torch.long, device=self.device)

        # 训练
        h_n, c_n = self.encoder(source_padded, source_len_batch)
        # h_n tensor(batch_size, seq_len)
        # c_n tensor(btach_size, seq_len)
        output = self.decoder((h_n, c_n), target_padded, target_len_batch)

        # 计算loss
        target_padded = target_padded[:, 1:]
        # target_padded: tensor (batch, seq_len, vocab_len)
        target_masks = (target_padded != self.vocab.tgt['_pad_']).float()
        # target_masks: tensor (batch_size, seq_len)
        target_gold_words_log_prob = torch.gather(output, index=target_padded.unsqueeze(-1), dim=-1).squeeze(-1) * target_masks
        # target_gold_words_log_prob: tensor (batch_size, seq_len)
        scores = target_gold_words_log_prob.sum(dim=1)
        return scores

    def predict(self, pad_sources_batch, source_len_batch):
        ''' 模型预测
        @param pad_targets_batch: 目标输出(id), 已padding, (List[List[str]]), [batch_size, seq_len]
        @param source_len_batch: List[int], 每个句子的原始长度
        @return prediction (str): 预测的语句
        '''
        # 将list转成tensor(未embed)
        source_padded = torch.tensor(pad_sources_batch, dtype=torch.long, device=self.device)
        source_padded.unsqueeze_(dim=0)
        # self.vocab.src.to_input_tensor(pad_sources_batch, device=self.device)   # Tensor: (batch_size, seq_len)
        source_len_batch = torch.tensor(source_len_batch, dtype=torch.long, device=self.device)
        # 预测
        h_n, c_n = self.encoder(source_padded, source_len_batch)
        # h_n tensor(batch_size, seq_len)
        # c_n tensor(btach_size, seq_len)
        output = self.decoder.predict((h_n, c_n))
        # output: tensor (batch, seq_len, vocab_len)
        index = torch.max(output, dim=1)[1]
        return index

    def computeLoss():
        ''' 计算损失
        '''
        pass


def save_model(session, path, overwrite=False):
    '''
    保存模型
    :param session: 训练模型的sessopm
    :param path: 要保存模型的路径
    :param name: 要保存模型的名字
    :param overwrite: 是否覆盖当前模型
    :return:
    '''
    pass

# def delete_file(path):
#     for root, dirs, files in os.walk(path, topdown=False):
#         for name in files:
#             os.remove(os.path.join(root, name))
#         for name in dirs:
#             os.rmdir(os.path.join(root, name))\
#         if overwrite:
#             delete_file(path)
#         print(path)



def get_tensor_name(name):
    return name + ":0"
