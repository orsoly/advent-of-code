#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    lines = [line.split(':')[1] for line in inputfile.read().strip().split('\n')]
    times = [int(time) for time in lines[0].split()]
    distances = [int(distance) for distance in lines[1].split()]
    data = list(zip(times, distances))
    return data

def get_possible_strategies(data):
    distances = []
    for sec in range(data[0] + 1):
        distance = (data[0] - sec) * sec
        if distance > data[1]:
            distances.append(distance)
    return len(distances)

def get_record_beating_ways(race_data):
    product = 1
    for data in race_data:
        product *= get_possible_strategies(data)
    return product

def get_single_race_data(race_data):
    time = ''
    distance = ''
    for data in race_data:
        time += str(data[0])
        distance += str(data[1])
    return [int(time), int(distance)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file type')
    args = parser.parse_args()

    race_data = read_input(args.input)

    part1_result = get_record_beating_ways(race_data)
    print(part1_result)

    single_race_data = get_single_race_data(race_data)
    part2_result = get_possible_strategies(single_race_data)
    print(part2_result)

if __name__ == '__main__':
    main()
