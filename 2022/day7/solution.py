#!/usr/bin/env python3

import argparse

def read_input(inputfile):
    return inputfile.read().strip().split('\n')

def get_current_wd(rootdir, path):
    if not path:
        return rootdir
    first = path[0]
    return get_current_wd(rootdir[first], path[1:])

def create_filesystem(command_list):
    filesystem = {}
    wd_list = []
    wd = get_current_wd(filesystem, wd_list)
    for command in command_list:
        if command == '$ cd /' or command == '$ ls':
            continue
        elif command.startswith('dir'):
            dirname = command.split(' ')[-1]
            wd[dirname] = {}
        elif command.startswith('$ cd'):
            if command == '$ cd ..':
                wd_list.pop()
                wd = get_current_wd(filesystem, wd_list)
            else:
                wd_list.append(command.split(' ')[-1])
                wd = get_current_wd(filesystem, wd_list)
        else:
            size = int(command.split(' ')[0])
            filename = command.split(' ')[1]
            wd[filename] = size
    return filesystem

def calculate_dir_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):
            total_size += calculate_dir_size(directory[key])
        else:
            total_size += value
    return total_size

def get_total_size(filesystem, size_list):
    for key, value in filesystem.items():
        if isinstance(value, dict):
            size_list.append(calculate_dir_size(filesystem[key]))
            get_total_size(filesystem[key], size_list)

def get_sum_size_under_limit(size_list, limit):
    sum_size = 0
    for size in size_list:
        if size <= limit:
            sum_size += size
    return sum_size

def get_smallest_dir_to_be_deleted(size_list, space_to_free_up, used_space):
    smallest_size = used_space
    for size in size_list:
        if size >= space_to_free_up and size < smallest_size:
            smallest_size = size
    return smallest_size

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'),
                        default='test_input', help='Input file name')
    args = parser.parse_args()

    command_list = read_input(args.input)
    filesystem = create_filesystem(command_list)
    size_list = []
    get_total_size(filesystem, size_list)

    sum_size_under_limit = get_sum_size_under_limit(size_list, 100000)
    print(sum_size_under_limit)

    total_available_space = 70000000
    required_space = 30000000
    used_space = calculate_dir_size(filesystem)
    unused_space = total_available_space - used_space
    space_to_free_up = required_space - unused_space

    smallest_dir_to_delete = get_smallest_dir_to_be_deleted(size_list, space_to_free_up, used_space)
    print(smallest_dir_to_delete)

if __name__ == '__main__':
    main()
