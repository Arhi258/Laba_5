#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    u = set('cehnfkxbprsg')

    a = {'c', 'e', 'h', 'n'}
    b = {'e', 'f', 'k', 'n', 'x'}
    c = {'b', 'c', 'h', 'p', 'r', 's'}
    d = {'b', 'e', 'g'}

    no_b = u.difference(b)

    x = a.difference(b).intersection(c.union(d))
    y = a.intersection(no_b).union(c.difference(d))

    print(x)
    print(y)
