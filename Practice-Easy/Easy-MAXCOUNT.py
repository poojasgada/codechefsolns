'''
Created on May 14, 2013

@author: psgada
'''
'''
Question:
Given an array A of length N, your task is to find the element which repeats in A maximum number of times as 
well as the corresponding count. In case of ties, choose the smaller element first.
Input

First line of input contains an integer T, denoting the number of test cases. Then follows description of T cases. Each case begins with a single integer N, the length of A. Then follow N space separated integers in next line. Assume that 1 <= T <= 100, 1 <= N <= 100 and for all i in [1..N] : 1 <= A[i] <= 10000
Output

For each test case, output two space separated integers V & C. V is the value which occurs maximum number of times and C is its count.
Example

Input:
2
5
1 2 3 2 5
6
1 2 2 1 1 2

Output:
2 2
1 3

Description:
In first case 2 occurs twice whereas all other elements occur only once. 
In second case, both 1 and 2 occur 3 times but 1 is smaller than 2.

'''
import collections

def count_max_num(num_list):
    #Counter is one of the coolest collections python has
    num_count_dict = collections.Counter(num_list)
    
    max_count = 0
    max_num = 0
    num_count_min_list = []
            
    max_count = max(num_count_dict.values())
    for num in num_count_dict:
        if num_count_dict[num] == max_count:
            num_count_min_list.append(int(num))
    max_num = min(num_count_min_list)
    print "%d %d"% (max_num,max_count)

        
    
def get_input():
    num_cases = input()
    
    for i in range(1, num_cases+1):
        num_count = input()
        num_list=[]
        num_list = raw_input().split()
        count_max_num(num_list)
        
get_input()