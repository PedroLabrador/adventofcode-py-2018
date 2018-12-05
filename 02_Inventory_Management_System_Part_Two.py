#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

""" Advent of Code Day 2 - Part One """

filename = "input-day-2.txt"
file = open("./inputs/" + filename, "r")

data = [line for line in file]
chars = "abcdefghijklmnopqrstuvwxyz"
id = ""
pos = -1

for id1 in data:
    for id2 in data:
        if id1 is not id2 and len(id1) is len(id2):
            match = [i for i in range(len(id1)) if id1[i] is not id2[i]]
            if len(match) is 1:
                id = id1
                pos = match[0]
                break
    if pos is not -1:
        break

output = "" if pos is -1 else id[:pos] + id[pos+1:]
print("Output: {}".format(output))