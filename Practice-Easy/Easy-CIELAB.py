'''
Created on May 22, 2013

@author: psgada
'''
'''
 In Ciel's restaurant, a waiter is training. Since the waiter isn't good at arithmetic, sometimes he gives
  guests wrong change. Ciel gives him a simple problem. What is A-B (A minus B) ?

Surprisingly, his answer is wrong. To be more precise, his answer has exactly one wrong digit. Can you 
imagine this? Can you make the same mistake in this problem?
Input

An input contains 2 integers A and B.
Output

Print a wrong answer of A-B. Your answer must be a positive integer containing the same number of digits 
as the correct answer, and exactly one digit must differ from the correct answer. Leading zeros are not allowed. 
If there are multiple answers satisfying the above conditions, anyone will do.
Constraints

1  B  A  10000
Sample Input

5858 1234

Sample Output

1624

Output details

The correct answer of 5858-1234 is 4624. So, for instance, 2624, 4324, 4623, 4604 and 4629 
will be accepted, but 0624, 624, 5858, 4624 and 04624 will be rejected. 
'''
#Note, B can be 1, but A > B. so A cannot be 1. so A-B = 0 will never occur
def get_cielab(num1, num2):
    sub_val = num1 - num2
    new_val = 0
    if(sub_val < 9):
        sub_val += 1
    if(sub_val == 9):
        sub_val -=1
    
    if(sub_val > 9):
        new_val = sub_val%10
        if(new_val < 9):
            sub_val += 1
        if(new_val == 9):
            sub_val -=1
    
    print sub_val
    
    

def get_input():
    num_list = map(int, raw_input().split())
    num1 = num_list[0]
    num2 = num_list[1]
    get_cielab(num1, num2)
    
get_input()