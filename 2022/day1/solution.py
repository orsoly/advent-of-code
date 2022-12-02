#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    full_list = [[int(num) for num in line.split('\n') ] for line in inputfile.read().strip().split('\n\n')]
    calories = []
    for item in full_list:
        cal_sum = 0
        for num in item:
            cal_sum += num
        calories.append(cal_sum)
    return calories

def get_top_three(calories):
    top_three = calories[-3:]
    sum_calories = 0
    for cal in top_three:
        sum_calories += cal
    return sum_calories

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    calories = read_input(args.input)
    print(max(calories))

    calories.sort()
    top_three = get_top_three(calories)
    print(top_three)

if __name__ == '__main__':
    main()
