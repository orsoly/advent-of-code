#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [[choice for choice in line.split(' ')] for line in inputfile.read().strip().split('\n')]

def calculate_score_fist_version(strategy_for_round):
    score = 0
    if strategy_for_round[1] == 'X':
        score += 1
        if strategy_for_round[0] == 'A':
            score += 3
        elif strategy_for_round[0] == 'C':
            score += 6
    elif strategy_for_round[1] == 'Y':
        score += 2
        if strategy_for_round[0] == 'A':
            score += 6
        elif strategy_for_round[0] == 'B':
            score += 3
    elif strategy_for_round[1] == 'Z':
        score += 3
        if strategy_for_round[0] == 'B':
            score += 6
        elif strategy_for_round[0] == 'C':
            score += 3
    return score

def calculate_score_second_version(strategy_for_round):
    score = 0
    outcome = ''
    if strategy_for_round[1] == 'X':
        score += 0
        if strategy_for_round[0] == 'A':
            score += 3
        elif strategy_for_round[0] == 'B':
            score += 1
        elif strategy_for_round[0] == 'C':
            score += 2
    elif strategy_for_round[1] == 'Y':
        score += 3
        if strategy_for_round[0] == 'A':
            score += 1
        elif strategy_for_round[0] == 'B':
            score += 2
        elif strategy_for_round[0] == 'C':
            score += 3
    elif strategy_for_round[1] == 'Z':
        score += 6
        if strategy_for_round[0] == 'A':
            score += 2
        elif strategy_for_round[0] == 'B':
            score += 3
        elif strategy_for_round[0] == 'C':
            score += 1
    return score

def get_total_score(strategy_guide, strategy_version):
    score = 0
    for single_round in strategy_guide:
        if strategy_version == 'first':
            score += calculate_score_fist_version(single_round)
        elif strategy_version == 'second':
            score += calculate_score_second_version(single_round)
    return score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    strategy = read_input(args.input)
    version = 'second'
    total_score = get_total_score(strategy, version)
    print(total_score)

if __name__ == '__main__':
    main()
