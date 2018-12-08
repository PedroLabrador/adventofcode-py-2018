#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import re
import collections

""" Advent of Code Day 3 - Part Two """

filename = "input-day-3.txt"
file = open("./inputs/" + filename, "r")
data = [line for line in file]

m = collections.defaultdict(int)

for line in data:
    split = re.split(r'\s|\D+', line)
    id, left, top, wide, tall = [int(value) for value in split if value]
    for i in range(left, left + wide):
        for j in range(top, top + tall):
            m[i, j] += 1

output = []

for line in data:
    split = re.split(r'\s|\D+', line)
    id, left, top, wide, tall = [int(value) for value in split if value]
    find = True
    for i in range(left, left + wide):
        for j in range(top, top + tall):
            if m[i, j] > 1:
                find = False
                break
        if not find:
            break
    if find:
        output.append(id) 

print("Output: {}".format(output))