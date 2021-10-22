import math
import numpy as np
from scipy.stats import entropy
from stanford_tokenizer import *
from nltk.corpus import stopwords
### Keyword Extraction ###
from rake_nltk import Rake



# util func
def roundup(x, places):
    d = 10 ** places
    if x < 0:
        return math.floor(x * d) / d
    else:
        return math.ceil(x * d) / d

def quarter_round(x):
    return math.ceil(x*4)/4


def unigram_distribution(source_text, given_summary, bin_type,stopw):
    distribution = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # Tokenized doc-sum pairs
    src_tokens = np.array([i.lower() for i in clean_and_tokenize(source_text) if (i.lower() not in punctuations)])
    # summ_tokens obtained from RAKE
    given_summary = " ".join(clean_and_tokenize(given_summary))
    rake = Rake()
    rake.extract_keywords_from_text(given_summary)
    summ_tokens = [j for i in rake.get_ranked_phrases()[:50] for j in i.split() if j not in punctuations and j not in stopw]
   #summ_tokens = np.array([i.lower() for i in clean_and_tokenize(given_summary) if (i.lower() not in punctuations) and (i.lower() not in stopw)])

    # salient unigram from summ tokens
    for salient_unigram in summ_tokens:
        distribution.append(list(np.where(src_tokens == salient_unigram)[0]))
    src_length = len(src_tokens)
    # some calculation
    if bin_type == 'quarter':
        distribution = [quarter_round((j + 1) / src_length) for i in distribution for j in i]
    elif bin_type == 'tenth':
        distribution = [roundup((j + 1) / src_length, 1) for i in distribution for j in i]
    elif bin_type == 'hundredth':
        distribution = [roundup((j + 1) / src_length, 2) for i in distribution for j in i]
    # https://math.stackexchange.com/questions/1857794/how-far-the-distribution-from-the-uniform-distribution

    return distribution


def normalized_entropy(labels, base=2):
    value, counts = np.unique(labels, return_counts=True)
    if len(counts) > 1:
        norm_entropy = entropy(counts, base=base) / math.log(len(counts), base)
    else:
        norm_entropy = 0
    return norm_entropy


'''
def uniformity(dist_list):
    n_log2 = math.log(len(dist_list),2)
    #value = n_log2 - entropy_compute(dist_list)
    #normalised_value = value/n_log2
    normalised_value = 1 - entropy_compute(dist_list)/n_log2
    return normalised_value
'''


def uniformity(source_text, given_summary, bin_type,stopw):
    dist_list = unigram_distribution(source_text, given_summary, bin_type,stopw)

    normalized_ent = normalized_entropy(dist_list)

    return normalized_ent

