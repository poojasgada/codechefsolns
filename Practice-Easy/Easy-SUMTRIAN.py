'''
Created on Jun 11, 2013

@author: psgada
'''
'''
Input:
2
3
1
2 1
1 2 3
4 
1 
1 2 
4 1 2
2 3 1 1 

Output:
5
9
'''

#Edge cases
#Only one line with one number
import sys

def find_max_path(num_list, num_lines, line_i, num_i):
    if(line_i+1 == num_lines):
        return num_list[line_i][num_i]

    return max(num_list[line_i][num_i]+find_max_path(num_list, num_lines,line_i+1, num_i), 
               num_list[line_i][num_i]+find_max_path(num_list, num_lines,line_i+1, num_i+1))

    
#May have to change raw_input() to sys.stdin.readline, if TLE

def get_input():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(1, num_cases+1):
        num_lines = int(sys.stdin.readline().strip())
        num_list = []
        for j in range(1, num_lines+1):
            num_line = [int(x) for x in sys.stdin.readline().split()]
            num_list.append(num_line)
        #Send the entire list of numbers, number of lines, current line index, current number index, current max sum
        if(num_lines == 1):
            print num_list[0][0]
        else:
            print find_max_path(num_list, num_lines, 1, 0) + num_list[0][0]

get_input()