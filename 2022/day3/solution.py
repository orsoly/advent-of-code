#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [line for line in inputfile.read().strip().split('\n')]

def get_compartments(sack):
    half_length = int(len(sack) / 2)
    compartments = [sack[:half_length], sack[half_length:]]
    return compartments

def get_overlap(sacks):
    overlap = set(sacks[0]).intersection(sacks[1])
    if len(sacks) > 2:
        for i in range(2, len(sacks)):
            overlap = overlap.intersection(sacks[i])
    return overlap

def get_priority(items):
    prio = 0
    for item in items:
        if item.isupper():
            prio += ord(item) - ord('A') + 27
        else:
            prio += ord(item) - ord('a') + 1
    return prio

def get_reorg_priorities(rucksacks):
    priorities = 0
    for sack in rucksacks:
        compartments = get_compartments(sack)
        overlap = get_overlap(compartments)
        priority = get_priority(overlap)
        priorities += priority
    return priorities

def get_badge_prioroties(rucksacks):
    priorities = 0
    for i in range(len(rucksacks)):
        if i % 3 == 0:
            overlap = get_overlap([rucksacks[i], rucksacks[i+1], rucksacks[i+2]])
            priority = get_priority(overlap)
            priorities += priority
        else:
            continue
    return priorities

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    rucksacks = read_input(args.input)
    reorg_priorities = get_reorg_priorities(rucksacks)
    print(reorg_priorities)

    badge_prioroties = get_badge_prioroties(rucksacks)
    print(badge_prioroties)


if __name__ == '__main__':
    main()
