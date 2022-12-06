#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    input_lines = inputfile.read().split('\n')
    bucket_count = int((len(input_lines[0]) + 1) / 4)
    crates = [[] for _ in range(bucket_count)]
    instructions = []
    for line in input_lines:
        if line.startswith(' 1') or line == '':
            continue
        elif line.startswith('move'):
            instruction = line.split(' ')
            instructions.append([int(instruction[1]), int(instruction[3]), int(instruction[5])])
        else:
            for i in range(bucket_count):
                crate = line[i * 4 + 1]
                if crate != ' ':
                    crates[i].insert(0, crate)
    return crates, instructions

def rearrange(crates, instructions, cratemover_type):
    for instruction in instructions:
        quantity = instruction[0]
        from_crate = instruction[1]
        to_crate = instruction[2]
        if cratemover_type == 'cratemover_9000':
            for i in range(quantity):
                crates[to_crate - 1].append(crates[from_crate - 1].pop())
        elif cratemover_type == 'cratemover_9001':
            for i in range(quantity):
                crates[to_crate - 1].append(crates[from_crate - 1][i-quantity])
                crates[from_crate - 1].pop(i-quantity)

def get_top_items(crates):
    top_items = ''
    for crate in crates:
        top_items += crate[-1]
    return top_items

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    crates, instructions = read_input(args.input)
    # possible types: cratemover_9000, cratemover_9001
    cratemover_type = 'cratemover_9001'
    rearrange(crates, instructions, cratemover_type)
    top_items = get_top_items(crates)
    print(top_items)

if __name__ == '__main__':
    main()
