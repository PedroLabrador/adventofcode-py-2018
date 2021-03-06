#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

""" Advent of Code Day 5 - Part One """

filename = "input-day-5.txt"
file = open("./inputs/" + filename, "r")
polymer = str(file.read())
chars = list('abcdefghijklmnopqrstuvwxyz')

def get(polymer):
    loop = True
    output = polymer

    while loop:
        for char in chars:
            polymer = polymer.replace(char + char.upper(), "").replace(char.upper() + char, "")
        if output is polymer:
            loop = False
            break
        output = polymer
    return output

polymer = get(polymer)

print(len(polymer))