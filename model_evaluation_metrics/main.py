import argparse
import json
import os
from informativeness import content_coverage, informativeness

parser = argparse.ArgumentParser()

parser.add_argument('--candidate_summaries', type=str, default='led_and_bb', help='path to txt candidates')
parser.add_argument('--ref_summaries', type=str, default='arxiv_abstract.txt', help='path to txt candidate')
parser.add_argument('--original_doc', type=str, default='test.txt', help='path to txt candidate')
parser.add_argument('--output_dir',type=str,default='led_and_bb_results',help='path to output dir')
args = parser.parse_args()

if __name__ == "__main__":
    with open(args.original_doc, 'r') as f:
        corpus = [json.loads(l.strip()) for l in f]

    with open(args.ref_summaries, 'r') as f:
        ref_summaries = [l.strip() for l in f]

    model_summaries = os.listdir(args.candidate_summaries)

    for candidate in model_summaries:
        candidate_path = os.path.join(args.candidate_summaries,candidate)
        with open(candidate_path, 'r') as f:
            candidate_summaries = [l.replace('<s>',' ').replace('<n>','').replace(' .','.').strip() for l in f]

        assert len(candidate_summaries) == len(corpus)
        assert len(candidate_summaries) == len(ref_summaries)

        for i in range(len(candidate_summaries)):
            cc = content_coverage(candidate_summaries[i],corpus[i])
            info = informativeness(cc,'rouge-l')

            model = candidate.replace('.txt','')
            with open(args.output_dir + '/'+model+'_cc.txt','a+') as f:
                f.write(str(cc) + '\n')

            with open(args.output_dir + '/' + model+'_info.txt','a+') as f:
                f.write(str(info) + '\n')