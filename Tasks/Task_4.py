#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    line = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре'}

    new_line = {}
    for key, value in line.items():
        new_line[value] = key

    print(new_line)