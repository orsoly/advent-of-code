#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    gamelist = [line for line in inputfile.read().strip().split('\n')]
    gamedata = {}
    for game in gamelist:
        game_num = int(game.split(':')[0].split()[1])
        cube_data = game.split(': ')[1]
        gamedata[game_num] = []
        for cube_subsets in cube_data.split('; '):
            subsets = {'red': 0, 'green': 0, 'blue': 0}
            for cubes in cube_subsets.split(', '):
                number = int(cubes.split()[0])
                color = cubes.split()[1]
                subsets[color] = number
            gamedata[game_num].append(subsets)
    return gamedata

def get_game_info(game_data, example_bag):
    possible_games = []
    bag_powers = []
    for game_num, cubes in game_data.items():
        game_is_possible = True
        bag_power = 1
        min_cube_bag = {'red': 0, 'green': 0, 'blue': 0}
        for subsets in cubes:
            for color, cube_num in subsets.items():
                if cube_num > example_bag[color]:
                    game_is_possible = False
                if cube_num > min_cube_bag[color]:
                    min_cube_bag[color] = cube_num
        if game_is_possible:
            possible_games.append(game_num)
        for v in min_cube_bag.values():
            bag_power *= v
        bag_powers.append(bag_power)
    return possible_games, bag_powers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    games = read_input(args.input)
    example_bag = {'red': 12, 'green': 13, 'blue': 14}
    possible_games, bag_powers = get_game_info(games, example_bag)
    print(sum(possible_games))
    print(sum(bag_powers))

if __name__ == '__main__':
    main()
