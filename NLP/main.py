import torch
import torch.nn as nn
import data_read
import EncoderNet
import DecoderNet
import matplotlib.pyplot as plt
import numpy as np


MAX_LENGTH  = 100
def train(device, input_tensor, target_tensor, encoder, decoder, encoder_optimizer, decoder_optimizer, criterion, max_length=MAX_LENGTH):
    encoder_hidden = encoder.initHidden().to(device)

    encoder_optimizer.zero_grad()
    decoder_optimizer.zero_grad()

    input_length = input_tensor.size(0)
    target_length = target_tensor.size(0)
    # initialize encoder output
    encoder_outputs = torch.zeros(max_length, encoder.hidden_size).to(device)

    loss = 0

    for ei in range(input_length):
        encoder_output, encoder_hidden = encoder(input_tensor[ei], encoder_hidden)
        encoder_outputs[ei] = encoder_output[0, 0]
    
    # decoder first input
    decoder_input = torch.tensor([[data_read.SOS_token]]).to(device)
    # decoder hidden vector
    decoder_hidden = encoder_hidden
    for di in range(target_length):
        decoder_output, decoder_hidden, decoder_attention = decoder(
            decoder_input, decoder_hidden, encoder_outputs)
        loss += criterion(decoder_output, target_tensor[di])
        decoder_input = target_tensor[di]

    # backward
    loss.backward()
    encoder_optimizer.step()
    decoder_optimizer.step()

    return loss.item() / target_length


def predict(encoder, decoder, input_lang, output_lang, inpu, device):
    input_tensor = torch.tensor(data_read.indexes_from_sentence(input_lang, inpu)).to(device)
    encoder_hidden = encoder.initHidden().to(device)
    encoder_outputs = torch.zeros(MAX_LENGTH, encoder.hidden_size, device=device)
    for ei in range(input_tensor.shape[0]):
        encoder_output, encoder_hidden = encoder(input_tensor[ei], encoder_hidden)
        encoder_outputs[ei] = encoder_output[0, 0]
    decoder_input = torch.tensor([[data_read.SOS_token]]).to(device)#, device=device)
    # decoder hidden vector
    decoder_hidden = encoder_hidden
    decoder_word = []
    for di in range(100):
            decoder_output, decoder_hidden, decoder_attention = decoder(
                decoder_input, decoder_hidden, encoder_outputs)
            topv, topi = decoder_output.topk(1)
            decoder_input = topi.squeeze().detach()  # detach from history as input
            if decoder_input.item() == data_read.EOS_token:
                decoder_word.append('<EOS>')
                break
            else:
                decoder_word.append(output_lang.index2word[topi.item()])
    return decoder_word

input_lang, output_lang, data = data_read.prepare()
hidden_size = 256
LEARNING_RATE = 0.001
if torch.cuda.is_available():
    device = 'cuda'
else:
    device = 'cpu'
device = torch.device(device)
encoder = EncoderNet.EncoderRNN(4858, hidden_size).to(device=device)
decoder = DecoderNet.AttnDecoderRNN(hidden_size, 7787).to(device=device)

encoder_optimizer = torch.optim.Adam(encoder.parameters(),lr=LEARNING_RATE, weight_decay=0.0005)
decoder_optimizer = torch.optim.Adam(decoder.parameters(),lr=LEARNING_RATE, weight_decay=0.0005)
criterion = nn.NLLLoss()
print_loss_total = 0
plot_loss_total = 0
plot_loss_last = 0
plot_every = 100
print_every = 1000
encoder.load_state_dict(torch.load('NLP/encoder.pkl'))
decoder.load_state_dict(torch.load('NLP/decoder.pkl'))
inpu1 = 'how are you'
inpu2 = 'i am fine thanks'
inpu3 = 'i am very happy to see you'
inpu4 = 'this test is so difficult that i can not finish it'

print(inpu1)
print(predict(encoder, decoder, input_lang, output_lang, inpu1, device))
print(inpu2)
print(predict(encoder, decoder, input_lang, output_lang, inpu2, device))
print(inpu3)
print(predict(encoder, decoder, input_lang, output_lang, inpu3, device))
print(inpu4)
print(predict(encoder, decoder, input_lang, output_lang, inpu4, device))
for i in range(0):
    for j in range(len(data)):
        print(j)
        plot_losses = []
        # get data_pair
        training_pair = data[j - 1]
        input_tensor = torch.tensor(data_read.indexes_from_sentence(input_lang,training_pair[0])).to(device)

        target_tensor = torch.tensor(data_read.indexes_from_sentence(output_lang,training_pair[1]))
        target_tensor = target_tensor.view(-1, 1).to(device)
        # get Loss
        loss = train(device, input_tensor, target_tensor, encoder,
                     decoder, encoder_optimizer, decoder_optimizer, criterion)
        print_loss_total += loss
        plot_loss_total += loss
        # print info
        if j % print_every == 0:
            print_loss_avg = print_loss_total / print_every
            print_loss_total = 0
            print('%d： %.4f' % (j, print_loss_avg))

        # if j % plot_every == 0:
        #     plot_loss_avg = plot_loss_total / plot_every
        #     plot_losses.append(plot_loss_avg)
        #     plot_loss_total = 0
        #     plt.plot(plot_losses)
        #     plt.ioff()
        #     plt.show()

torch.save(encoder.state_dict(), 'NLP/encoder.pkl')
torch.save(decoder.state_dict(), 'NLP/decoder.pkl')
            
