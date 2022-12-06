#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [[char for char in line] for line in inputfile.read().strip().split('\n')]

def find_marker_positions(datastream, length):
    positions = []
    for data in datastream:
        marker = []
        for i in range(len(data)):
            char = data[i]
            if len(marker) == length:
                positions.append(i)
                break
            elif char not in marker:
                marker.append(char)
            else:
                index = marker.index(char)
                for j in range(index + 1):
                    marker.pop(0)
                marker.append(char)
    return positions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    datastream = read_input(args.input)
    marker_length = 14
    marker_positions = find_marker_positions(datastream, marker_length)
    print(marker_positions)

if __name__ == '__main__':
    main()
