#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    monkey_list = [[line.strip() for line in monkey.split('\n')] for monkey in inputfile.read().strip().split('\n\n')]
    monkey_data = {}
    mod_num = 1
    for monkey in monkey_list:
        monkey_id = int(monkey[0].split(' ')[1][0])
        starting_items = [int(num) for num in monkey[1].split(': ')[-1].split(', ')]
        operation = monkey[2].split('= ')[-1]
        check = int(monkey[3].split(' ')[-1])
        throws = [int(monkey[4].split(' ')[-1]), int(monkey[5].split(' ')[-1])]

        monkey_data[monkey_id] = {}
        monkey_data[monkey_id]['item_list'] = starting_items
        monkey_data[monkey_id]['operation'] = operation
        monkey_data[monkey_id]['check'] = check
        monkey_data[monkey_id]['throws'] = throws
        monkey_data[monkey_id]['inspect_count'] = 0
        mod_num *= check
    return monkey_data, mod_num

def calculate_worry_level(original_level, operation, mod_num):
    if original_level > mod_num:
        original_level = original_level % mod_num
    old = original_level
    worry_level = eval(operation)
    # following line is necessary for part1 only
    # worry_level = int(worry_level/3)
    return worry_level

def passes_check(level, check):
    passes = False
    if level % check == 0:
        passes = True
    return passes

def simulate_rounds(monkey_data, mod_num, round_num):
    for r in range(round_num):
        for monkey, data in monkey_data.items():
            while data['item_list']:
                data['inspect_count'] += 1
                worry_level = calculate_worry_level(data['item_list'].pop(0), data['operation'], mod_num)
                if passes_check(worry_level, data['check']):
                    monkey_data[data['throws'][0]]['item_list'].append(worry_level)
                else:
                    monkey_data[data['throws'][1]]['item_list'].append(worry_level)

def print_items(monkey_data):
    for monkey, data in monkey_data.items():
        print('Monkey {}: {}'.format(monkey, data['item_list']))
        print('Monkey {} inspected {} items'.format(monkey, data['inspect_count']))

def calculate_monkey_business(monkey_data):
    activeness_levels = []
    for data in monkey_data.values():
        activeness_levels.append(data['inspect_count'])
    activeness_levels.sort(reverse=True)
    business = activeness_levels[0] * activeness_levels[1]
    return business

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    monkey_data, mod_num = read_input(args.input)
    round_num = 10000
    simulate_rounds(monkey_data, mod_num, round_num)
    monkey_business = calculate_monkey_business(monkey_data)
    print(monkey_business)

if __name__ == '__main__':
    main()
