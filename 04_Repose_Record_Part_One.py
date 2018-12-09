#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

from collections import defaultdict

""" Advent of Code Day 4 - Part One """

def get_pos_max(cant):
	x = None
	for key, value in cant.items():
		if x is None or value > cant[x]:
			x = key
	return x

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
		
minutes_asleep = defaultdict(int)

for guard in guards:
	date, id, minutes = guard
	for minute in minutes:
		if minute:
			minutes_asleep[id] += 1

guard_id = get_pos_max(minutes_asleep)

min = defaultdict(int)
for i in range(0,60):
	min[i] = 0

for guard in guards:
	if guard_id in guard:
		for key, value in enumerate(guard[2]):
			min[key] += int(value)

pos = get_pos_max(min)

print(guard_id, pos)
print(guard_id * pos)