'''
Created on Jun 9, 2013

@author: psgada
'''


#Note: Even though, the problem does not explicitly say that, we are to assume that there are no negative skill levels


def get_input():
    num_cases = input()
    
    for i in range(1, num_cases+1):
        num_count = input()
        num_list = [int(num) for num in raw_input().split()]
        min_diff = 1000000001
        num_list.sort()
        for i in range(1, num_count):
            if((num_list[i] - num_list[i-1]) < min_diff):
                min_diff = num_list[i] - num_list[i-1]
    
        print min_diff
        
get_input()