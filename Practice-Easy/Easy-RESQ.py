'''
Created on Jun 8, 2013

@author: psgada
'''
'''
 Our Chef is catering for a big corporate office party and is busy preparing different mouth watering dishes. 
 The host has insisted that he serves his delicious cupcakes for dessert.

On the day of the party, the Chef was over-seeing all the food arrangements as well, ensuring that every item 
was in its designated position. The host was satisfied with everything except the cupcakes. He noticed they were 
arranged neatly in the shape of a rectangle. He asks the Chef to make it as square-like as possible.

The Chef is in no mood to waste his cupcakes by transforming it into a perfect square arrangement. Instead, to 
fool the host, he asks you to arrange the N cupcakes as a rectangle so that the difference between the length 
and the width is minimized.
Input

The first line of the input file contains an integer T, the number of test cases. Each of the following T lines 
contains a single integer N denoting the number of cupcakes.
Output

Output T lines, each indicating the minimum possible difference between the length and the width in a rectangular
 arrangement of the cupcakes.
Constraints

1  T  100

1  N  108
Example

Input:
4
20
13
8
4

Output:
1
12
2
0

'''
from math import floor, sqrt, fabs

def get_input():
    num_cases = int(input())
    for i in range(1, num_cases+1):
        num = int(input())
        
        mid = int(floor(sqrt(num)))
        factor_list = []
        for j in range(1,mid+1):
            if(num % j == 0):
                factor_list.append(j)
        
        smallest_diff = num
        for num1 in factor_list:
            num2 = num/num1
            if(fabs(num1-num2) < smallest_diff):
                smallest_diff = fabs(num1-num2)
        print int(smallest_diff)
        
get_input()
        