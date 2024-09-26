#! /usr/bin/env python3

# Lets make a secret santa picker

#imports
import os
import math
import random

#lets get a list of people

list = []
results = []

people = int(input("How many people are participating?\n"))

i = 0
n = 1

while i < people:
	name = input("What is name #" + str(n) + "?\n")
	list.append(name)
	results.append(" ")
	i += 1
	n += 1

print("\n------- Rolling The Dice -------\n")
pick = list.copy()


#now for picking and assigning pairs at random

x = 0

while len(pick) >= 1:
	y = random.randrange(0,len(pick),)
	if len(pick) == 1:
		results[x] = pick[0]
		x += 1
		del pick[y]
	elif list[x] != pick[y]:
		results[x] = pick[y]
		del pick[y]
		x += 1
	else:
		continue

#print ("List \n" + str(list))
#print ("Santas\n " + str(results))

z = 0

while z < len(results):
	print (list[z] + " has " + results[z] + " as a Santa")
	z += 1

print (" ")
print ("Thanks!\n")

#Greg was here! 252330SEP24

