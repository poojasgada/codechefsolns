'''
Created on Jun 23, 2013

@author: psgada
'''

import sys 

def find_cup_slot():
    
    num_cases = int(sys.stdin.readline().strip()) 
    
    for i in range(0, num_cases):
        num_list = map(int, sys.stdin.readline().strip().split())
        cur_pos = num_list[1]
        
        for j in range(num_list[2]):
            cup_range = map(int, sys.stdin.readline().strip().split())
            
            #The property to note here is, in the range, sum of first and last numbers is same as first+1 and last-1
            #For ex: 1 2 3 4 5, 1+5 = 2+4, so if cur_pos = 2, new_pos = sum - 2 = 4
            if cur_pos >= cup_range[0] and cur_pos <= cup_range[1]:
                cur_pos = cup_range[0] + cup_range[1] - cur_pos
                
        print cur_pos
        

find_cup_slot()