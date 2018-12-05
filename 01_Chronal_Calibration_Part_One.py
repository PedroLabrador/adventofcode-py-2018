#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

""" Advent of Code Day 1 - Part One """

filename = "input-day-1.txt"
file = open("./inputs/" + filename, "r")

data = [int(line) for line in file]
cursor = sum(data)

print ("Output: {}".format(cursor))