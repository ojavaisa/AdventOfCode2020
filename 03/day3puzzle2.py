# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:39:19 2020

@author: Olli

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

"""
import numpy as np

with open('input.txt') as f:
    rows = [line.rstrip() for line in f]
    
answer = []
maxcol = len(rows[0])

trees = 0
column = 0
right = 1
for row in rows:
    prnt = list(row)
    if(row[column] == '#'):
        trees += 1
        prnt[column] = 'X'
    else:
        prnt[column] = 'O'
    if(column+right >= maxcol): #periodic boundary: if out or bounds, wrap back to beginning
        column = (column + right) - maxcol
    else:
        column += right
    #print("".join(prnt), column)
answer.append(trees)

trees = 0
column = 0
right = 3
for row in rows:
    prnt = list(row)
    if(row[column] == '#'):
        trees += 1
        prnt[column] = 'X'
    else:
        prnt[column] = 'O'
    if(column+right >= maxcol):
        column = (column + right) - maxcol
    else:
        column += right
    #print("".join(prnt), column)
answer.append(trees)

trees = 0
column = 0
right = 5
for row in rows:
    prnt = list(row)
    if(row[column] == '#'):
        trees += 1
        prnt[column] = 'X'
    else:
        prnt[column] = 'O'
    if(column+right >= maxcol):
        column = (column + right) - maxcol
    else:
        column += right
    #print("".join(prnt), column)
answer.append(trees)

trees = 0
column = 0
right = 7
for row in rows:
    prnt = list(row)
    if(row[column] == '#'):
        trees += 1
        prnt[column] = 'X'
    else:
        prnt[column] = 'O'
    if(column+right >= maxcol):
        column = (column + right) - maxcol
    else:
        column += right
    #print("".join(prnt), column)
answer.append(trees)

trees = 0
column = 0
nrow = 0
right = 1
for row in rows:
    if(nrow % 2 != 0):
        nrow += 1
        prnt = list(row)
    else:
        prnt = list(row)
        if(row[column] == '#'):
            trees += 1
            prnt[column] = 'X'
        else:
            prnt[column] = 'O'
        if(column+right >= maxcol):
            column = (column + right) - maxcol
        else:
            column += right
        nrow += 1
    #print("".join(prnt), column)
answer.append(trees)

print(answer)
print(answer[0]*answer[1]*answer[2]*answer[3]*answer[4])