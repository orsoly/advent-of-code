#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    lines = [line for line in inputfile.read().strip().split('\n')]
    numbers = []
    for line in lines:
        winning_numbers = line.split(':')[1].split('|')[0].strip()
        winning_num_list = [int(num) for num in winning_numbers.split()]
        elf_numbers = line.split(':')[1].split('|')[1].strip()
        elf_num_list = [int(num) for num in elf_numbers.split()]
        numbers.append([winning_num_list, elf_num_list])
    return numbers

def get_points(card_data):
    points = 0
    for numbers in card_data:
        winning_numbers = [num for num in numbers[0] if num in numbers[1]]
        if len(winning_numbers) > 0:
            points += pow(2, (len(winning_numbers) - 1))
    return points

def get_total_cards(card_data):
    winning_num_list = []
    card_count_list = [1] * len(card_data)
    for numbers in card_data:
        winning_numbers = [num for num in numbers[0] if num in numbers[1]]
        winning_num_list.append(len(winning_numbers))
    for num in range(0, len(winning_num_list)):
        for i in range (1, winning_num_list[num] + 1):
            card_count_list[num + i] += card_count_list[num]
    return sum(card_count_list)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file type')
    args = parser.parse_args()

    card_data = read_input(args.input)
    points = get_points(card_data)
    print(points)

    total_cards = get_total_cards(card_data)
    print(total_cards)

if __name__ == '__main__':
    main()
