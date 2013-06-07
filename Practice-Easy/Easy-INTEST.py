'''
Created on May 16, 2013

@author: psgada
'''
'''
Question:
The purpose of this problem is to verify whether the method you are using to read input data is sufficiently 
fast to handle problems branded with the enormous Input/Output warning. 
You are expected to be able to process at least 2.5MB of input data per second at runtime.
Input

The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.
Output

Write a single integer to output, denoting how many integers ti are divisible by k.
Example

Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
'''
import sys

#After trying input(), turns out, the faster way to do io in python is sys.stdin.readline()

def get_input():
    num_list_count, divisor = map(int, raw_input().split())
    result_count = 0
    for i in range(1, num_list_count+1):
        num = int(sys.stdin.readline())
        if num%divisor == 0: 
            result_count = result_count + 1
            
    print result_count
    
get_input()