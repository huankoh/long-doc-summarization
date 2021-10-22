from stanford_tokenizers import *

import json
from rouge import Rouge
from statistics import mean,median
import pandas as pd
import os
import swifter
from tqdm.auto import tqdm
import argparse

def content_coverage(model_summary, doc_sum_dict):
    try:
        rouge = Rouge()
        master_dict = {}
        sections = doc_sum_dict['sections']
        # Text of each section
        section_text = {i: "".join(sections[i]) for i in range(len(sections))}
        summary_sentences = sent_tokenizer(model_summary)
        # total number of sections
        master_dict['number_of_sections'] = len(section_text)
        master_dict['section_names'] = doc_sum_dict['section_names']
        master_dict['summary_sentences'] = summary_sentences
        sum_section_rouge = {}
        counter = 0
        # Summary sentence loop
        for sum_sent in summary_sentences:
            sum_sent_rouge = []
            for k, text in section_text.items():
                rouge_dict = rouge.get_scores(sum_sent + '.', text + '.')[0]
                sum_sent_rouge.append((k, rouge_dict))

            sum_section_rouge[counter] = sum_sent_rouge
            counter += 1

        master_dict['sum_section_rouge'] = sum_section_rouge

        return master_dict
    except KeyboardInterrupt:
        None
    except:
        return "Error"


def informativeness(detailed_dict, rouge_type='rouge-l'):
    if detailed_dict == 'Error': return "Error"

    num_of_sections = detailed_dict['number_of_sections']
    sum_section_rouge = detailed_dict['sum_section_rouge']

    sections_max = []
    for k, v in sum_section_rouge.items():
        sorted_list = sorted(v, key=lambda x: x[1][rouge_type]['f'])
        sections_max.append(sorted_list[0][0])

    unique_sections = set(sections_max)

    return len(unique_sections) / len(detailed_dict['summary_sentences'])
