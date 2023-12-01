#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [line for line in inputfile.read().strip().split('\n')]

def is_digit(char):
    return ord(char) >= 49 and ord(char) <= 57

def check_for_spelled_out_digit(i, line):
    substring = line[i:i+3]
    if substring == 'one':
        return 1
    elif substring == 'two':
        return 2
    elif substring == 'six':
        return 6
    substring = line[i:i+4]
    if substring == 'four':
        return 4
    elif substring == 'five':
        return 5
    elif substring == 'nine':
        return 9
    substring = line[i:i+5]
    if substring == 'three':
        return 3
    elif substring == 'seven':
        return 7
    elif substring == 'eight':
        return 8
    return -1

def get_calibration_values(document):
    values = []
    for line in document:
        digits = []
        for i in range(len(line)):
            digit = -1
            if is_digit(line[i]):
                digit = int(line[i])
            else:
                digit = check_for_spelled_out_digit(i, line)
            if digit != -1:
                digits.append(digit)
        value = digits[0] * 10 + digits[-1]
        values.append(value)
    return values

def add_values(value_list):
    value_sum = 0
    for value in value_list:
        value_sum += value
    return value_sum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    calibration_document = read_input(args.input)
    calibration_values = get_calibration_values(calibration_document)
    calibration_value_sum = add_values(calibration_values)
    print(calibration_value_sum)

if __name__ == '__main__':
    main()
