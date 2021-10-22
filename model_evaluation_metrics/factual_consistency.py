from tokenizers import *
import os
import json
from allennlp_models.pretrained import load_predictor
p = load_predictor("pair-classification-roberta-mnli")


def te_roberta(given_premise, given_hypothesis):
    result = p.predict(premise=given_premise, hypothesis=given_hypothesis)

    return result

def factual_consistency(ref_summ, cand_summ):
    summary_sentences = sent_tokenizer(cand_summ)
    result_dict = {}

    result_dict['all'] = te_roberta(cand_summ,ref_summ)
    for i in range(len(summary_sentences)):
        result_dict[i] = te_roberta(summary_sentences[i],ref_summ)

    return result_dict

with open('arxiv_abstract.txt','r') as f:
    ref_summaries = [l.strip() for l in f]

model_summaries = os.listdir('abstractive_summaries')

for candidate in model_summaries:
    candidate_path = os.path.join('abstractive_summaries',candidate)
    with open(candidate_path, 'r') as f:
        candidate_summaries = [l.replace('<s>', ' ').replace('<n>', '').replace(' .', '.').strip() for l in f]

    assert len(candidate_summaries) == len(ref_summaries)

    candidate_results = {}

    for i in range(len(candidate_summaries)):
        sum_result = factual_consistency(ref_summaries[i],candidate_summaries[i])

        candidate_results[i] = sum_result

    name = candidate.replace('txt','') + '_fact.json'

    with open(name, 'w') as fp:
        json.dump(candidate_results, fp)