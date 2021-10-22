from itertools import combinations, permutations
from stanford_tokenizer import *
from rouge import Rouge
from statistics import mean

rouge = Rouge()


def redundancy(sent_list):
    scores = []
    unique_pairs = combinations(range(len(sent_list)), 2)
    for pair in unique_pairs:
        try:
            sent1 = sent_list[pair[0]].lower()
            sent2 = sent_list[pair[1]].lower()
            rouge_l = rouge.get_scores(sent1, sent2)[0]['rouge-l']['f']
            scores.append(rouge_l)
        except:
            return 'Error'
    if len(scores) > 0:
        score = mean(scores)
        return score
    else:
        return 'Error'