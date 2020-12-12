# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 03:10:34 2020

@author: Olli

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

"""
import numpy as np
f = open("input.txt", "r")

policy = []
password = []

for line in f:
    temp = line.split(":")
    temp2 = temp[0].split()
    temp3 = temp2[0].split("-")
    policy.append([int(temp3[0]), int(temp3[1]), temp2[1]])
    password.append(temp[1].strip())

valid = 0

for pwd, plcy in zip(password, policy):
    indx1 = plcy[0]-1
    indx2 = plcy[1]-1
    if(np.logical_xor(pwd[indx1] == plcy[2], pwd[indx2] == plcy[2])):
        valid += 1

print(valid)