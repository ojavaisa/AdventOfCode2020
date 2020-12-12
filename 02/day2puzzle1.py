# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 02:28:23 2020

@author: Olli

--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Puzzle input in file input.txt
"""
f = open("input.txt", "r")

policy = []
password = []

for line in f:
    temp = line.split(":")
    temp2 = temp[0].split()
    temp3 = temp2[0].split("-")
    policy.append([int(temp3[0]), int(temp3[1]), temp2[1]])
    password.append(temp[1].strip())

#print(policy)
#print(password)

valid = 0

for pwd, plcy in zip(password, policy):
    nmbr = pwd.count(plcy[2])
    if(nmbr >= plcy[0] and nmbr <= plcy[1]):
        valid += 1

print(valid)