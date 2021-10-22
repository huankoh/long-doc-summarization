from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# NLTK and preprocessing libraries
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.util import ngrams
import re
import contractions # for expanding contractions

import spacy
import json



# Initialise stemmer and lemmatizer
sb_stem = SnowballStemmer("english")
wn_lemma = WordNetLemmatizer()

## Define stopwords - from nltk to standardize across all functions and packages
nlp = spacy.load('en_core_web_sm')
spacy_stopwords = list(nlp.Defaults.stop_words) + ['et','al'] # which is far too common in a paper
## Stopwords for stemming and lemmatisation
stem_stopwords = set([''.join(sb_stem.stem(w)) for w in spacy_stopwords]).union(set(spacy_stopwords))
lemma_stopwords = set([''.join(wn_lemma.lemmatize(w)) for w in spacy_stopwords]).union(set(spacy_stopwords))

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
    text = contractions.fix(text)
    # Case lowering
    text = text.lower()
    ### convert all numeric into a code and drop 1 char word
    tokens = [w if not w.isnumeric() else '-NUMBER-' for w in word_tokenize(text)]
    #tokens = [t for t in tokens if len(t) > 1]
    return tokens

def preprocess_m3(tokens, create_bigram = True):
    '''
    Text Preprocessing function method 3 as defined above.
    '''
    # Lemmatise tokens
    lemma_words = [''.join(wn_lemma.lemmatize(w)) for w in tokens if len(w) > 1]
    removed_stopwords = [w for w in lemma_words if w not in lemma_stopwords]
    # Bigrams
    if create_bigram:
        bigrams = ['_'.join(bigram) for bigram in list(ngrams(removed_stopwords, 2))]
    else:
        bigrams = []
    ## Final output
    output = removed_stopwords + bigrams
    return output


## Method 3 class
class preprocess_m3_tfidf:
    def __init__(self):
        self.preprocessor = preprocess_m3

    def __call__(self, doc):
        return self.preprocessor(clean_and_tokenize(doc))

def stopwords_output(corpus):
    model = TfidfVectorizer(analyzer='word', input='content', lowercase=True, max_df=0.5)
    model.fit_transform(corpus)
    stopwords = model.stop_words_
    return stopwords