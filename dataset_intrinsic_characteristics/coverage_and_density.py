from stanford_tokenizer import *
import math

# util func
def roundup(x, places):
    d = 10 ** places
    if x < 0:
        return math.floor(x * d) / d
    else:
        return math.ceil(x * d) / d

def quarter_round(x):
    return math.ceil(x*4)/4

def ext_fragments(source_txt, given_summary):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # punctuations = ''
    # Tokenized doc-sum pairs
    src_tokens = [i.lower() for i in clean_and_tokenize(source_txt) if i not in punctuations]
    summ_tokens = [i.lower() for i in clean_and_tokenize(given_summary) if i not in punctuations]
    src_length = len(src_tokens) - 1
    summ_length = len(summ_tokens) - 1
    # print(src_length)
    i = 0  # summary index
    j = 0  # source index
    fragments = []
    # Compute coverage
    while i <= summ_length:
        fragment = []
        while j <= src_length:
            if (summ_tokens[i] == src_tokens[j]) and (i == summ_length or j == src_length):
                if len(fragment) <= 1:
                    fragment = [summ_tokens[i]]
                j += 1  # +1 makes it > than src_length
            elif summ_tokens[i] == src_tokens[j]:
                temp_i = i
                temp_j = j
                while summ_tokens[temp_i] == src_tokens[temp_j]:
                    temp_i += 1
                    temp_j += 1
                    if temp_i == summ_length or temp_j == src_length: break
                if len(fragment) < (temp_i - i):
                    fragment = summ_tokens[i:temp_i]
                j = temp_j
            else:
                j += 1
        # Fragment length
        frag_length = len(fragment)
        i = i + max([frag_length, 1])
        j = 0
        # Add our fragment into master fragments list
        if len(fragment) > 0:
            fragments.append(fragment)
    print(fragments)
    coverage = sum([len(i) for i in fragments]) / summ_length
    density = sum([len(i) ** 2 for i in fragments]) / summ_length

    results = {
        'coverage': coverage,
        'density': density
    }

    return results