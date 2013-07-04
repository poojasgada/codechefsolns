'''
Created on Jul 3, 2013

@author: psgada
'''
import sys
from math import floor

#Ha, we dont really need to find primes
def primes_sieve_way(n):
        
    prime_dict = {}
    
    for i in range(2, n+1):
        prime_dict[i] = True
    
    for i in range(2, n+1):
        for j in range(i+i, n+1, i):
            
            prime_dict[j] = False
        
    #print prime_dict
    count = 0
    
    for i in prime_dict.keys():
        if prime_dict[i] == True:
            count += 1
    
    return count
    
def get_input():
    num_cases = int(sys.stdin.readline().strip()) 
    
    for i in range(0, num_cases):
        num_list = map(int, sys.stdin.readline().strip().split())
        
        if num_list[1] == 1:
            print 1
            continue
        
        if num_list[1] > floor(num_list[0]/2):
            print -1
            continue
        
        init_val = 2
        for i in range(0, num_list[1] -1):
            print init_val,
            init_val += 2
            
        print init_val
        
get_input()