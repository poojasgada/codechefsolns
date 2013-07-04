'''
Created on Jun 7, 2013

@author: psgada
'''
'''
Chef Datta likes betting in Indian Premier League very much.

He has 10000 rupees. Today the match is between team A and team B. The winning probability of team A is PA, 
and hence winning probability of team B is PB = 1-PA.

Datta is free to bet any integral amount of money on any of the two teams as long as the total amount of money 
bet is at most 10000 rupees.
Help him know the expected amount of money he will eventually have if today he places his bet(s) optimally.
Rules of the game:

If team X with winning probability PX actually wins and someone bets M rupees on this team, he will gain 
(2*(1-PX)) * M rupees

If team X with winning probability PX actually loses and someone bets N rupees on this team, he will just 
lose N rupees.
Input

First line contains single integer T, the number of testcases. Then T lines follow, each line contains PA 
the probability that team A wins.
Output

For each test case output single line containing the expected amount of money Datta will eventually have 
today if he places his bet(s) optimally. Your answer will be accepted if the absolute error is less than 10-6.
Constraints

    1  T  100001 (105+1)
    0.0  PA  1.0
    PA has at most 5 digits after the decimal point.

Example

Input:
1
0.510

Output:
10098

0:00:00.015000
 
'''

#Absolutely clueless about how to optimize it 

from datetime import datetime
def get_input():
    num_test_cases = int(input())
    
    for i in range(1, num_test_cases+1):
        win_prob_a = input()
        win_prob_b = 1 - win_prob_a
        
        
        #For (0,0)
        x = 0
        y = 0        
        amount_won_0 = (x*2*(1-win_prob_a) - y)*win_prob_a + (-x + y*(2*(1-win_prob_b)))*win_prob_b
            
        x = 10000
        y = 0
        amount_won_x = (x*2*(1-win_prob_a) - y)*win_prob_a + (-x + y*(2*(1-win_prob_b)))*win_prob_b
        
        x = 0
        y = 10000
        amount_won_y = (x*2*(1-win_prob_a) - y)*win_prob_a + (-x + y*(2*(1-win_prob_b)))*win_prob_b
        
       
        print max(amount_won_0, amount_won_x, amount_won_y) + 10000

        
get_input()