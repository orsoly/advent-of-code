#!/usr/bin/env python3

import argparse

def get_seeds(seed_data):
    seed_numbers = seed_data.split(':')[1]
    seeds = [int(num) for num in seed_numbers.split()]
    return seeds

def create_seed_handling_guide(lines):
    seed_handling_guide = []
    for line in lines:
        guide_type = line.split('\n')[0].split()[0]
        guide_data = []
        for data in line.split('\n')[1:]:
            numbers = [int(num) for num in data.split()]
            guide_data.append(numbers)
        seed_handling_guide.append(guide_data)
    return seed_handling_guide

def read_input(inputfile):
    lines = [line for line in inputfile.read().strip().split('\n\n')]
    seeds = get_seeds(lines.pop(0))
    seed_handling_guide = create_seed_handling_guide(lines)
    return seeds, seed_handling_guide

def calculate_location(seeds, seed_handling_guide):
    locations = []
    for seed in seeds:
        new_number = seed
        for guide in seed_handling_guide:
            match_found = False
            for data in guide:
                if match_found:
                    break
                destination_range_start = data[0]
                source_range_start = data[1]
                range_length = data[2]
                if new_number >= source_range_start:
                    if new_number < source_range_start + range_length:
                        new_number = destination_range_start + (new_number - source_range_start)
                        match_found = True
        locations.append(new_number)
    return locations

# ------------------------------------------------------------------------------
# ^^^^^^^^ part 1 ^^^^^^^^
# vvvvvvvv part 2 vvvvvvvv
# ------------------------------------------------------------------------------

def do_reverse_mapping(num, seed_handling_guide):
    new_number = num
    for guide in reversed(seed_handling_guide):
        match_found = False
        for data in guide:
            if match_found:
                break
            destination_range_start = data[0]
            source_range_start = data[1]
            range_length = data[2]
            if new_number >= destination_range_start:
                if new_number < destination_range_start + range_length:
                    new_number = source_range_start + (new_number - destination_range_start)
                    match_found = True
    return new_number

def seed_exists(seeds, seed_to_check):
    seed_exists = False
    for i in range(0, len(seeds)):
        if i % 2 == 1:
            continue
        else:
            seed = seeds[i]
            seed_range = seeds[i+1]
            if seed_to_check >= seed and seed_to_check <= seed + seed_range:
                seed_exists = True
    return seed_exists

def get_lowest_location(seeds, seed_handling_guide):
    lowest_location = 0
    i = 0
    while(True):
        seed_to_check = do_reverse_mapping(i, seed_handling_guide)
        if seed_exists(seeds, seed_to_check):
            lowest_location = i
            break
        i += 1
    return lowest_location

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file type')
    args = parser.parse_args()

    seeds, seed_handling_guide = read_input(args.input)

    locations = calculate_location(seeds, seed_handling_guide)
    print(min(locations))

    lowest_location = get_lowest_location(seeds, seed_handling_guide)
    print(lowest_location)

if __name__ == '__main__':
    main()
