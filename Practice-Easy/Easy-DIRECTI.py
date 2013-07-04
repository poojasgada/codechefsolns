'''
Created on Jun 23, 2013

@author: psgada
'''
'''
Chef recently printed directions from his home to a hot new restaurant across the town, but forgot to print the directions to get back home. Help Chef to transform the directions to get home from the restaurant.

A set of directions consists of several instructions. The first instruction is of the form "Begin on XXX", indicating the street that the route begins on. Each subsequent instruction is of the form "Left on XXX" or "Right on XXX", indicating a turn onto the specified road.

When reversing directions, all left turns become right turns and vice versa, and the order of roads and turns is reversed. See the sample input for examples.
Input

Input will begin with an integer T, the number of test cases that follow. Each test case begins with an integer N, the number of instructions in the route. N lines follow, each with exactly one instruction in the format described above.
Output

For each test case, print the directions of the reversed route, one instruction per line. Print a blank line after each test case.
Constraints

    1  T  15
    2  N  40
    Each line in the input will contain at most 50 characters, will contain only alphanumeric characters and spaces and will not contain consecutive spaces nor trailing spaces. By alphanumeric characters we mean digits and letters of the English alphabet (lowercase and uppercase).

Sample Input

2
4
Begin on Road A
Right on Road B
Right on Road C
Left on Road D
6
Begin on Old Madras Road
Left on Domlur Flyover
Left on 100 Feet Road
Right on Sarjapur Road
Right on Hosur Road
Right on Ganapathi Temple Road

Sample Output

Begin on Road D
Right on Road C
Left on Road B
Left on Road A

Begin on Ganapathi Temple Road
Left on Hosur Road
Left on Sarjapur Road
Left on 100 Feet Road
Right on Domlur Flyover
Right on Old Madras Road


'''
import sys

def find_reverse_route():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        num_directions = int(sys.stdin.readline().strip())
        
        dir_list = []
        for j in range(0, num_directions):
            direction = sys.stdin.readline().strip().split()
            dir_list.append(direction)
        
        
        cur_val ="Begin"
        
        for j in range(num_directions-1, -1, -1):
            next_val = dir_list[j][0]
            dir_list[j][0] = cur_val
            
            for k in range(0, len(dir_list[j]) - 1):
                print dir_list[j][k],
                
            print dir_list[j][k+1]
            
            #In the reverse route the directions are reversed
            if next_val == "Right":
                cur_val = "Left"
            elif next_val == "Left":
                cur_val = "Right"
                
                
find_reverse_route()