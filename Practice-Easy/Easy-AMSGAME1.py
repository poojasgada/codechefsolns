'''
Created on Jun 20, 2013

@author: psgada
'''
'''
Chef is playing a game on a sequence of N positive integers, say A1, A2, ... AN. The game is played as follows.

    If all the numbers are equal, the game ends.
    Otherwise
        Select two numbers which are unequal
        Subtract the smaller number from the larger number
        Replace the larger number with the result from above (see the explanation section for clarity)

Chef has already figured out that the game always terminates. He also knows, for a given sequence of integers, the game will always terminate on the same value, no matter how the game is played. Chef wants you to simulate the game for him and tell him on which value will the game terminate for a given sequence of integers.
Input

The first line of the input contains an integer T, the number of test cases. Then follow the description of T test cases. The first line of each test case contains a single integer N, the length of the sequence. The second line contains N positive integers, each separated by a single space.
Output

For each test case, output a single integer - the value of all the numbers when they are equal (and the game terminates), on a line by itself.
Constraints

1  T  100
1  N  1000
1  Ai  109
Sample

Input
3
2
10 12
2
5 9
3
6 10 15

Output
2
1
1

One more example:

4 
20 15 45 60
20 15 45 40 
20 15 25 40
20 15 25 20
20 15 5 20
5 15 5 20
5 15 5 15
5 10 5 15
5 10 5 10
5 5 5 10
5 5 5 5
gcd(20, 15, 45, 60)
'''

#This is a really simple problem, all one has to do is fine the gcd of all the numbers in the list
import sys

#Double check this
def gcd(num1, num2):
    
    while num2:
        oldnum1 = num1
        num1 = num2
        num2 = oldnum1 % num2
    
    return num1

def get_input():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        num_count = int(sys.stdin.readline().strip())
        
        num_list = map(int, sys.stdin.readline().strip().split())
        
        temp_gcd = num_list[0]
        for j in range(1, num_count):
            temp_gcd = gcd(temp_gcd, num_list[j])
            
        print temp_gcd
        
get_input()