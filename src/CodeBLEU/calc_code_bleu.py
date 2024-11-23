# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

# -*- coding:utf-8 -*-
import sys
sys.path.append('./CodeBLEU')
import argparse
import bleu
import weighted_ngram_match
import syntax_match
import dataflow_match

def codebleu(ref, hyp, lang, params=(0.25, 0.25, 0.25, 0.25)):
    alpha, beta, gamma, theta = params
    assert len(ref) == len(hyp)

    refs = []
    for r in ref:
        refs.append([r])
    assert len(refs) == len(hyp)

    # calculate ngram match (BLEU)
    tokenized_hyps = [x.split() for x in hyp]
    tokenized_refs = [[x.split() for x in ref] for ref in refs]

    ngram_match_score = bleu.corpus_bleu(tokenized_refs, tokenized_hyps)

    # calculate weighted ngram match
    keywords = [x.strip() for x in open('./CodeBLEU/keywords/' + lang + '.txt', 'r', encoding='utf-8').readlines()]

    def make_weights(reference_tokens, key_word_list):
        return {token: 1 if token in key_word_list else 0.2 \
                for token in reference_tokens}

    tokenized_refs_with_weights = [[[reference_tokens, make_weights(reference_tokens, keywords)] \
                                    for reference_tokens in reference] for reference in tokenized_refs]

    weighted_ngram_match_score = weighted_ngram_match.corpus_bleu(tokenized_refs_with_weights, tokenized_hyps)

    # calculate syntax match
    syntax_match_score = syntax_match.corpus_syntax_match(refs, hyp, lang)

    # calculate dataflow match
    dataflow_match_score = dataflow_match.corpus_dataflow_match(refs, hyp, lang)

    # print('ngram match: {0}, weighted ngram match: {1}, syntax_match: {2}, dataflow_match: {3}'. \
    #       format(ngram_match_score, weighted_ngram_match_score, syntax_match_score, dataflow_match_score))

    code_bleu_score = alpha * ngram_match_score \
                      + beta * weighted_ngram_match_score \
                      + gamma * syntax_match_score \
                      + theta * dataflow_match_score

    # print('CodeBLEU score: ', code_bleu_score)
    return code_bleu_score

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref', type=str, required=True,
                            help='reference file')
    parser.add_argument('--hyp', type=str, required=True,
                            help='hypothesis file')
    parser.add_argument('--lang', type=str, required=True,
                            choices=['java','js','c_sharp','php','go','python','ruby'],
                            help='programming language')
    parser.add_argument('--params', type=str, default='0.25,0.25,0.25,0.25',
                            help='alpha, beta and gamma')

    args = parser.parse_args()
    ref = [x.strip() for x in open(args.ref, 'r', encoding='utf-8').readlines()]
    hyp = [x.strip() for x in open(args.hyp, 'r', encoding='utf-8').readlines()]
    codebleu(ref, hyp, args.lang, (float(x) for x in args.params.split(',')))


