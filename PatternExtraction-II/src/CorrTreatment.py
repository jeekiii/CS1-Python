#!/usr/bin/python3
# -*- coding: utf-8 -*-


def treatment(data):
    pattern = ""
    current = data.split()[0]
    count = 0
    for c in data.split():
        if c == current:
            count += 1
        else:
            pattern += current + '*' + str(count) + ' '
            count = 1
            current = c
    return pattern
