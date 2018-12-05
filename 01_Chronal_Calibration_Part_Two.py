#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

""" Advent of Code Day 1 - Part Two """

filename = "input-day-1.txt"
file = open("./inputs/" + filename, "r")

data = [int(line) for line in file]
frequency_list = [0]
cursor = 0
    
loop = True

print("Not optimized code. This process may take few minutes.")
while loop:
    for number in data:
        cursor += number
        if cursor in frequency_list:
            loop = False
            break
        frequency_list.append(cursor)

print("Found: {}, array length: {}".format(cursor, len(frequency_list)))

