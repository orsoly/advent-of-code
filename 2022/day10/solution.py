#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [[item for item in line.split(' ')] for line in inputfile.read().strip().split('\n')]

def create_intruction_per_tick(intructions):
    instructions_per_tick = []
    for i in intructions:
        if len(i) == 2:
            instructions_per_tick.append(['noop'])
        instructions_per_tick.append(i)
    return instructions_per_tick

def print_pixels(pixels):
    line = ''
    for i in range(len(pixels)):
        line += pixels[i]
        if (i + 1) % 40 == 0:
            print(line)
            line = ''

def run_program(instructions):
    cycle = 0
    x_reg = 1
    signal_strength = 0
    pixels = ['.']*240
    for i in instructions:
        if (cycle % 40) in [x_reg - 1, x_reg, x_reg + 1]:
            pixels[cycle] = '#'
        cycle += 1
        if (cycle + 20) % 40 == 0:
            signal_strength += cycle * x_reg
        if len(i) == 2:
            x_reg += int(i[1])
    return signal_strength, pixels

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    intructions = read_input(args.input)

    instructions_per_tick = create_intruction_per_tick(intructions)
    signal_strength, pixels = run_program(instructions_per_tick)
    print(signal_strength)
    print_pixels(pixels)

if __name__ == '__main__':
    main()
