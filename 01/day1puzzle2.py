# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:50:38 2020

@author: Olli

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
import numpy as np
import itertools

expenses = np.loadtxt('input.txt')

# =============================================================================
# for i in expenses:
#     for j in expenses:
#         for k in expenses:
#             if(i != j and i != k and j != k):
#                 if(i + j + k == 2020):
#                     print(i, j, k)
#                     print(int(i*j*k))
# =============================================================================

for i, j, k in itertools.product(expenses, repeat=3):
    if(i + j + k == 2020):
        #print(i, j, k)
        print(int(i*j*k))
        break


