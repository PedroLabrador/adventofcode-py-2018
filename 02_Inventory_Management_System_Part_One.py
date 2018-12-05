#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

""" Advent of Code Day 2 - Part One """

filename = "input-day-2.txt"
file = open("./inputs/" + filename, "r")

chars = "abcdefghijklmnopqrstuvwxyz"
a, b = (0,)*2

for line in file:
    count = [0, 0]
    for char in chars:
        match = line.count(char)
        if match is 2 and count[0] is 0:
            count[0] = 1
            a += 1
        elif match is 3 and count[1] is 0:
            count[1] = 1
            b += 1
        
print("Output: {}".format(a*b))