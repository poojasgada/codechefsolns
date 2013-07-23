'''
Created on Jul 5, 2013

@author: psgada
'''
import sys
def find_min_rect():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        num_list = map(int, sys.stdin.readline().strip().split())
        
        if num_list[0] == 1:
            if num_list[1] <= 2:
                print 0
                continue
            else:
                print num_list[2]
                continue
            
        if num_list[1] == 1:
            if num_list[0] <= 2:
                print 0
                continue
            else:
                print num_list[2]
                continue
        
        if num_list[2] % 2 == 0:
            print num_list[2]/2
        else:
            print num_list[2]/2 + 1
            
            
find_min_rect()