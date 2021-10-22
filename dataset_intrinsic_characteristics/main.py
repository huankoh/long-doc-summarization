from stanford_tokenizer import *
from redundancy import *
from coverage import ext_fragments
from uniformity import uniformity
import json
import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from tfidf import stopwords_output



def intrinsic_characteristic(source_doc, ref_summ,stopw):
    result_dict = {}
    # Tokens and Sents
    source_tokens = clean_and_tokenize(source_doc)
    summ_tokens = clean_and_tokenize(ref_summ)
    source_sents = sent_tokenizer(source_doc)
    summ_sents = sent_tokenizer(ref_summ)
    result_dict['source_tokens'] = len(source_tokens)
    result_dict['source_sents'] = len(source_sents)
    result_dict['summ_tokens'] = len(summ_tokens)
    result_dict['summ_sents'] = len(summ_sents)
    try:
        # Compression Ratio
        result_dict['compress_tokens'] = len(source_tokens)/len(summ_tokens)
        result_dict['compress_sents'] = len(source_sents)/len(summ_sents)
    except:
        result_dict['compress_tokens'] = 'Error'
        result_dict['compress_sents'] = 'Error'

    # Redundancy
    try:
        result_dict['redundancy'] = redundancy(summ_sents)
    except:
        result_dict['redundancy'] = 'Error'
        # Coverage and Density
    try:
        cov_and_den = ext_fragments(source_doc, ref_summ)
        result_dict['coverage'] = cov_and_den['coverage']
        result_dict['density'] = cov_and_den['density']
    except:
        result_dict['coverage'] = 'Error'
        result_dict['density'] = 'Error'
    # Uniformity
    try:
        result_dict['uniformity'] = uniformity(source_doc, ref_summ,'tenth',stopw)
    except:
        result_dict['uniformity'] = 'Error'
    return result_dict


if __name__ == "__main__":
    with open('./datasets/ARXIV/test.txt','r') as f:
        arxiv = [json.loads(l.strip()) for l in f]

    source_summ = [" ".join(i['abstract_text']).replace('<S>','').replace('</S>','').strip() for i in arxiv]
    #stopwords = stopwords_output(source_summ)

    src = " ".join(arxiv[1000]['article_text'])
    summ = "".join(arxiv[1000]['abstract_text']).replace('<S>','').replace('</S>','').strip()

    import spacy
    nlp = spacy.load('en_core_web_sm')
    stopwords = set(list(nlp.Defaults.stop_words) + ['et', 'al'])  # which is far too common in a paper

    test = intrinsic_characteristic(src, summ, stopwords)

    pprint.pprint(test)

