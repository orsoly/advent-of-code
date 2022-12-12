#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return [[int(num) for num in line] for line in inputfile.read().strip().split('\n')]

def print_map(tree_map):
    for line in tree_map:
        print(line)

def get_neighbours(height_map, x, y, row_len, col_len):
    n = {'up': [], 'down': [], 'left': [], 'right': []}
    for c in range(col_len):
        for r in range(row_len):
            height = height_map[c][r]
            if r == x:
                if c < y:
                    n['up'].append(height)
                elif c > y:
                    n['down'].append(height)
            elif c == y:
                if r < x:
                    n['left'].append(height)
                elif r > x:
                    n['right'].append(height)
    return n

def is_visible(height_map, x, y, row_len, col_len):
    visible = 0
    height = height_map[y][x]
    neighbours = get_neighbours(height_map, x, y, row_len, col_len)
    for value in neighbours.values():
        visible_in_line = 0
        if all(n < height for n in value):
            visible_in_line = 1
        if visible_in_line == 1:
            visible = 1
            break
    return visible

def get_visible_trees(height_map):
    row_len = len(height_map[0])
    col_len = len(height_map)
    visible_trees = [[0 for _ in range(row_len)] for _ in range(col_len)]
    for y in range(col_len):
        for x in range(row_len):
            if x == 0 or y == 0 or x == row_len - 1 or y == col_len - 1:
                visible_trees[y][x] = 1
            else:
                visible_trees[y][x] = is_visible(height_map, x, y, row_len, col_len)
    return visible_trees

def count_visible_trees(tree_map):
    sum_visible = 0
    for line in tree_map:
        for num in line:
            sum_visible += num
    return sum_visible

def calculate_scientic_score(tree_height_map, x, y, row_len, col_len):
    score_list = []
    neighbours = get_neighbours(tree_height_map, x, y, row_len, col_len)
    height = tree_height_map[y][x]
    for key, value in neighbours.items():
        view_dist = 0
        if key == 'down' or key == 'right':
            for v in value:
                if v < height:
                    view_dist += 1
                else:
                    view_dist += 1
                    break
        elif key == 'up' or key == 'left':
            for v in value[::-1]:
                if v < height:
                    view_dist += 1
                else:
                    view_dist += 1
                    break
        score_list.append(view_dist)
    score = 1
    for s in score_list:
        score *= s
    return score

def get_scientic_scores(tree_height_map):
    row_len = len(tree_height_map[0])
    col_len = len(tree_height_map)
    scientic_scores = [[0 for _ in range(row_len)] for _ in range(col_len)]
    for y in range(col_len):
        for x in range(row_len):
            if x == 0 or y == 0 or x == row_len - 1 or y == col_len - 1:
                continue
            else:
                scientic_scores[y][x] = calculate_scientic_score(tree_height_map, x, y, row_len, col_len)
    return scientic_scores

def get_highest_score(scientic_score_map):
    highest_score = 0
    for line in scientic_score_map:
        for num in line:
            if num > highest_score:
                highest_score = num
    return highest_score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    tree_height_map = read_input(args.input)
    visible_tree_map = get_visible_trees(tree_height_map)
    num_of_visible_trees = count_visible_trees(visible_tree_map)
    print(num_of_visible_trees)

    scientic_score_map = get_scientic_scores(tree_height_map)
    highest_scientic_score = get_highest_score(scientic_score_map)
    print(highest_scientic_score)

if __name__ == '__main__':
    main()
