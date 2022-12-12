#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [[item for item in line.split(' ') ] for line in inputfile.read().strip().split('\n')]

def move_right(from_pos):
    return (from_pos[0] + 1, from_pos[1])

def move_left(from_pos):
    return (from_pos[0] - 1, from_pos[1])

def move_up(from_pos):
    return (from_pos[0], from_pos[1] + 1)

def move_down(from_pos):
    return (from_pos[0], from_pos[1] - 1)

def step_head(from_pos, direction):
    if direction == 'R':
        to_pos = move_right(from_pos)
    elif direction == 'L':
        to_pos = move_left(from_pos)
    elif direction == 'U':
        to_pos = move_up(from_pos)
    elif direction == 'D':
        to_pos = move_down(from_pos)
    else:
        to_pos = ('error', 'unknown direction')
    return to_pos

def follow_head(head_pos, from_pos):
    if head_pos == from_pos:
        return from_pos
    elif abs(head_pos[0] - from_pos[0]) <= 1 and abs(head_pos[1] - from_pos[1]) <= 1:
        return from_pos
    else:
        if head_pos[0] > from_pos[0]:
            new_pos = move_right(from_pos)
            if head_pos[1] == from_pos[1]:
                return new_pos
            elif head_pos[1] > from_pos[1]:
                return move_up(new_pos)
            elif head_pos[1] < from_pos[1]:
                return move_down(new_pos)
        elif head_pos[0] < from_pos[0]:
            new_pos = move_left(from_pos)
            if head_pos[1] == from_pos[1]:
                return new_pos
            elif head_pos[1] > from_pos[1]:
                return move_up(new_pos)
            elif head_pos[1] < from_pos[1]:
                return move_down(new_pos)
        elif head_pos[1] > from_pos[1]:
            new_pos = move_up(from_pos)
            if head_pos[0] == from_pos[0]:
                return new_pos
            elif head_pos[0] > from_pos[0]:
                return move_right(new_pos)
            elif head_pos[0] < from_pos[0]:
                return move_left(new_pos)
        elif head_pos[1] < from_pos[1]:
            new_pos = move_down(from_pos)
            if head_pos[0] == from_pos[0]:
                return new_pos
            elif head_pos[0] > from_pos[0]:
                return move_right(new_pos)
            elif head_pos[0] < from_pos[0]:
                return move_left(new_pos)
    return from_pos

def get_visited_positions(motion_list):
    head_pos = (0,0)
    tail_pos = (0,0)
    visited_positions = set()
    visited_positions.add(tail_pos)
    for motion in motion_list:
        direction = motion[0]
        steps = int(motion[1])
        for _ in range(steps):
            head_pos = step_head(head_pos, direction)
            tail_pos = follow_head(head_pos, tail_pos)
            visited_positions.add(tail_pos)
    return visited_positions

def get_long_rope_visited_positions(motion_list):
    rope_positions = [(0,0)] * 10
    visited_positions = set()
    visited_positions.add(rope_positions[-1])
    for motion in motion_list:
        direction = motion[0]
        steps = int(motion[1])
        for _ in range(steps):
            rope_positions[0] = step_head(rope_positions[0], direction)
            for i in range(1, len(rope_positions)):
                rope_positions[i] = follow_head(rope_positions[i-1], rope_positions[i])
            visited_positions.add(rope_positions[-1])
    return visited_positions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input1', help='Input file name')
    args = parser.parse_args()

    motion_list = read_input(args.input)
    visited_positions = get_visited_positions(motion_list)
    print(len(visited_positions))

    long_rope_visited_positions = get_long_rope_visited_positions(motion_list)
    print(len(long_rope_visited_positions))

if __name__ == '__main__':
    main()
