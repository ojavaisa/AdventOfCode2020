# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:11:28 2020

@author: Olli
"""

test = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
arrangements = 1

def noOfChoices(x):
    return len([n for n in test if (n>x and n<=x+3)])

            