#! /usr/bin/env python3

# Lets make a secret santa picker

#imports
import os
import math
import random

#lets get a list of people

list = []
results = []
empty = []

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

#def dice_roll():
results = empty.copy()
pick = list.copy()
x = 0
while len(pick) >= 1:
	y = random.randrange(0,len(pick),)
	if len(pick) == 1:
		if list[x] == pick[0]:
#			print (list[x] + " has " + pick[y] + "\n Reroll")
			del results
			results = empty.copy()
			del pick
			pick = list.copy()
			x = 0
		else:
			results[x] = pick[0]
			print (results)
			break
	elif list[x] == pick[y]:
#			print (list[x] + " has " + pick[y] + "\n Reroll")
			del results
			results = empty.copy()
			del pick
			pick = list.copy()
			x = 0
	elif list[x] != pick[y]:
		results[x] = pick[y]
		print(results)
#		print(results[x] + " results <> pick " + pick[y])
#		print(list[x] + " list <> results " + results[x])
#		print (list[x] + " has " + results[x]) 
		del pick[y]
		x += 1
	else:
		continue


#print(results)
z = 0
while z < len(results):
	print (list[z] + " has " + results[z] + " as a Santa")
	z += 1

print ("\nThanks\n")

#Greg was here! 252330SEP24

