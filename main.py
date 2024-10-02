#! /usr/bin/env python3

# Lets make a secret santa picker

#imports
import os
import math
import random

list = []
results = []
empty = []


#lets get a number and list of people from the user.

people = int(input("How many people are participating?\n"))

i = 0
n = 1

while i < people:
	name = input("What is name #" + str(n) + "?\n")
	list.append(name)
	results.append(" ")
	empty.append(" ")
	i += 1
	n += 1

print("\n------- Rolling The Dice -------\n")

#now for picking and assigning pairs at random
#this also includes a quality check aspect to where if a list item matches a randomly picked pick item, it
#clears everything out and starts from the beginning. And when everything is all clear between list and results,
#we break out of the loop.


x = 0
while len(pick) >= 1:
	y = random.randrange(0,len(pick),)
	if len(pick) == 1:
		if list[x] == pick[0]:
			del results
			results = empty.copy()
			del pick
			pick = list.copy()
			x = 0
		else:
			results[x] = pick[0]
			break
	elif list[x] == pick[y]:
			del results
			results = empty.copy()
			del pick
			pick = list.copy()
			x = 0
	elif list[x] != pick[y]:
		results[x] = pick[y]
		print(results)
		del pick[y]
		x += 1
	else:
		continue



z = 0
while z < len(results):
	print (list[z] + " has " + results[z] + " as a Santa")
	z += 1

print ("\nThanks\n")

#Greg was here! 252330SEP24

