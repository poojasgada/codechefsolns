'''
Created on Jun 21, 2013

@author: psgada
'''
'''
 The Little Elephant from the Zoo of Lviv has an array A that consists of N positive integers. Let A[i] be the i-th number in this array (i = 1, 2, ..., N).

Find the minimal number x > 1 such that x is a divisor of all integers from array A. More formally, this x should satisfy the following relations:

A[1] mod x = 0, A[2] mod x = 0, ..., A[N] mod x = 0,

where mod stands for the modulo operation. For example, 8 mod 3 = 2, 2 mod 2 = 0, 100 mod 5 = 0 and so on. If such number does not exist, output -1.
Input

The first line of the input contains a single integer T, the number of test cases. T test cases follow. The first line of each test case contains a single integer N, the size of the array A for the corresponding test case. The second line contains N space separated integers A[1], A[2], ..., A[N].
Output

For each test case output a single line containing the answer for the corresponding test case.
Constraints

1  T  100000

1  N  100000

The sum of values of N in each test file does not exceed 100000

1  A[i]  100000
Example

Input:
2
3
2 4 8
3
4 7 5

Output:
2
-1


'''

#The logic is pretty cool, first find the gcd of all the numbers
#Then find the least prime factor of the gcd
#If the gcd is a prime, then print the gcd itself, else print the least prime factor 

import sys
from math import sqrt

def gcd(num1, num2):
    
    while num2 != 0:
        oldnum1 = num1
        num1 = num2
        num2 = oldnum1 % num2
    
    return num1

def find_least_prime_factor():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        num_count = int(sys.stdin.readline().strip())
        num_list = map(int, sys.stdin.readline().strip().split())
        
        gcd_val = reduce(gcd, num_list)
        
        if gcd_val == 1:
            print -1
            continue
        
        least_prime = -1
        
        for i in range(2, int(sqrt(gcd_val))+1):
            if gcd_val % i == 0:
                least_prime = i
                break
        
        if least_prime > 0:
            print least_prime
        else:
            print gcd_val
        
find_least_prime_factor()