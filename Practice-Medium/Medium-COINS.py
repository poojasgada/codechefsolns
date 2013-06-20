'''
Created on Jun 14, 2013

@author: psgada
'''

'''
In Byteland they have a very strange monetary system.

Each Bytelandian gold coin has an integer number written on it. A coin n
can be exchanged in a bank into three coins: n/2, n/3 and n/4.
But these numbers are all rounded down (the banks have to make a profit).

You can also sell Bytelandian coins for American dollars. The exchange
rate is 1:1. But you can not buy Bytelandian coins.

You have one gold coin. What is the maximum amount of American dollars
you can get for it?
Input

The input will contain several test cases (not more than 10). Each
testcase is a single line with a number n, 0 <= n <= 1 000 000 000.
It is the number written on your coin.
Output

For each test case output a single line, containing the maximum amount
of American dollars you can make.
Example

Input:
12
2

Output:
13
2

'''
import sys

#The recursive solution is quite simple, but have to use memoization to speed things up and to avoid the annoying TLE
# Using a dict instead of list, for quick access

dict_vals = {}

def find_max_dollars(num):
    
    if num in dict_vals.keys():
        return dict_vals[num]
    if num >= (num/2 + num/3 + num/4):
            dict_vals[num] = num
    else:
        dict_vals[num] = find_max_dollars(num/2) + find_max_dollars(num/3) + find_max_dollars(num/4)
    
    return dict_vals[num]

def get_input():
    for cnt in range(1,11):
        num = input()
        print find_max_dollars(num)
        

get_input()