#import stanfordnlp
#stanford_nlp = stanfordnlp.Pipeline(processors='tokenize', lang='en')
import nltk

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

'''
def stanford_tokenizer(text):
    text = text.replace(' .', '.')
    doc = stanford_nlp(text)
    sentences = []
    for i, sentence in enumerate(doc.sentences):
        sent = [word.text for word in sentence.words]
        sentences.append(sent)

    return sentences

'''
def sent_tokenizer(text):
    '''
    if type(text) == list:
        return text

    text = text.replace(' .', '.')
    doc = stanford_nlp(text)
    sentences = []
    for i, sentence in enumerate(doc.sentences):
        sent = ' '.join([word.text for word in sentence.words])
        sentences.append(sent)
    '''
    sentences = sent_detector.tokenize(text)
    return sentences


def word_tokenizer(text):
    '''
    text = text.replace(' .', '.')
    doc = stanford_nlp(text)
    words = []
    for i, sentence in enumerate(doc.sentences):
        words += [word.text for word in sentence.words]
    '''
    words = nltk.word_tokenize(text)
    return words


from nltk.stem import SnowballStemmer, WordNetLemmatizer
import re
import contractions # for expanding contractions

from nltk.corpus import stopwords

## Clean text and tokenize
def clean_and_tokenize(text):
    '''
    This function clean and tokenize the text by performing:
    1. remove multiple spaces
    2. remove newline
    3. Fix contraction
    4. Lowering text
    5. Tokenize using nltk word_tokenizer
    6. convert numeric to -NUMBER-
    '''
    ### clean up
    # remove multiple spaces
    text = re.sub(r' +', ' ', text)
    # remove newline
    text = re.sub(r'\n', ' ', text)
    ### Fix contraction such as punctuations - e.g. he's to he is
    #text = contractions.fix(text)
    # Case lowering
    text = text.lower()
    ### convert all numeric into a code and drop 1 char word
    tokens = [w if not w.isnumeric() else '' for w in word_tokenizer(text)]
    #tokens = [w for w in tokens if w not in '''!()-[]{};:'"\,<>./?@#$%^&*_~''']
    #tokens = [t for t in tokens if len(t) > 1]
    return tokens