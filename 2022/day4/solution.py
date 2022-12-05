#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [[[int(num) for num in interval.split('-')] for interval in line.split(',')] for line in inputfile.read().strip().split('\n')]

def create_range(range_list):
    range_set = set()
    for i in range(range_list[0], range_list[-1] + 1):
        range_set.add(i)
    return range_set

def has_overlap(pair, overlap_type):
    range1 = create_range(pair[0])
    range2 = create_range(pair[1])
    overlap = range1.intersection(range2)
    if overlap_type == 'full':
        if range1 == overlap or range2 == overlap:
            return True
    elif overlap_type == 'partial':
        if overlap:
            return True
    return False

def count_overlaps(pairs, overlap_type):
    sum_overlap = 0
    for pair in pairs:
        if has_overlap(pair, overlap_type):
            sum_overlap += 1
    return sum_overlap

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    pairs = read_input(args.input)
    # overlap types: full, partial
    overlap_type = 'partial'
    overlapping_pairs = count_overlaps(pairs, overlap_type)
    print(overlapping_pairs)

if __name__ == '__main__':
    main()
