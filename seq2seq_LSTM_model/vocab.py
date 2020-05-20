
class Vocab(object):
    def __init__(self, in_language: str, out_language: str):
        """ Init Vocab Instance.
        @param word2id (dict): dictionary mapping words 2 indices
        """
        self.word2id = dict()
        self.word2id['PAD'] = 0 # Pad Token
        self.word2id['SOS'] = 1 # Start Token
        self.word2id['EOS'] = 2 # End Token
        self.word2id['UNK'] = 3 # Unknown Token

        pass

    def read_languages(in_language: str, out_language: str):
        print('Reading lines ....')
        filename = './data/%s-%s.txt' % (in_language, out_language)
        lines = open(filename).read().strip().split('\n')

        # split every line to pairs and normalize
        pairs = [[normalize_string(s) for s in l.split('\t')] for l in lines]

        # the option to reverse:
        input_lang = Lang(lang1)
        output_lang = Lang(lang2)
        return input_lang, output_lang, pairs

    def 