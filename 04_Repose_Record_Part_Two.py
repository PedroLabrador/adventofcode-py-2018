#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

from collections import defaultdict

""" Advent of Code Day 4 - Part Two """

filename = "input-day-4.txt"
file = open("./inputs/" + filename, "r")
data = ["".join(current.split("\n")) for current in [line for line in file] if current]
data.sort()

guards = []
current_guard = "#-1"

for line in data:
	inputs = line.split(" ")	

	if 'Guard' in inputs:
		try:
			guards.append([inputs[0][1:], int(current_guard[1:]), mins])
		except:
			pass
		mins = [0]*60
		current_guard = inputs[3]
		continue

	hour, minute = [int(o[:2]) for o in inputs[1].split(":")]

	if 'falls' in inputs:
		for min in range(minute, 60):
			mins[min] = 1
	if 'wakes' in inputs:
		for min in range(minute, 60):
			mins[min] = 0

guards.sort(key=lambda x:x[1], reverse=False)
		
guards_id = defaultdict(int)

for guard in guards:
	date, id, minutes = guard
	for minute in minutes:
		if minute:
			guards_id[id] += 1

guards_minutes_asleep = defaultdict(int)

for cant in guards_id:
    min = defaultdict(int)
    for i in range(0,60):
        min[i] = 0

    for guard in guards:
        if cant in guard:
            for k,v in enumerate(guard[2]):
                min[k] += int(v)
    guards_minutes_asleep[cant] = min

pos = None
minute = None
guard_id = None

for key, minutes_asleep in guards_minutes_asleep.items():
    current_guard = key
    for key, minutes in minutes_asleep.items():
        if minute is None or minutes > minute:
            guard_id = current_guard
            minute = minutes
            pos = key
            
print(guard_id, pos)
print(guard_id * pos)