#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import re
import collections

""" Advent of Code Day 3 - Part One """

filename = "input-day-3.txt"
file = open("./inputs/" + filename, "r")

m = collections.defaultdict(int)

for line in file:
    split = re.split(r'\s|\D+', line)
    id, left, top, wide, tall = [int(value) for value in split if value]
    for i in range(left, left + wide):
        for j in range(top, top + tall):
            m[i, j] += 1

overlap = sum(1 for value in m.values() if value > 1)
print("Output: {}".format(overlap))