'''
Created on May 30, 2013

@author: psgada
'''
'''
 Did you know that there are over 40,000 varieties of Rice in the world ? There are so many dishes that can be
  prepared with Rice too. A famous chef from Mumbai, Tid Gusto prepared a new dish and named it 'Tid Rice'. He 
  posted the recipe in his newly designed blog for community voting, where a user can plus (+) or minus (-) the
   recipe. The final score is just the sum of all votes, where (+) and (-) are treated as +1 and -1 respectively. 
   But, being just a chef ( and not a codechef ) he forgot to take care of multiple votes by the same user.

A user might have voted multiple times and Tid is worried that the final score shown is not the correct one. 
Luckily, he found the user logs, which had all the N votes in the order they arrived. Remember that, if a user 
votes more than once, the user's previous vote is first nullified before the latest vote is counted ( see 
explanation for more clarity ). Given these records in order ( and being a codechef yourself :) ), calculate 
the correct final score.
Input

First line contains T ( number of testcases, around 20 ). T cases follow. Each test case starts with N ( 
total number of votes, 1 <= N <= 100 ). Each of the next N lines is of the form "userid vote" ( quotes for 
clarity only ), where userid is a non-empty string of lower-case alphabets ( 'a' - 'z' ) not more than 20 in 
length and vote is either a + or - . See the sample cases below, for more clarity.
Output

For each test case, output the correct final score in a new line
Example

Input:
3
4
tilak +
tilak +
tilak -
tilak +
3
ratna +
shashi -
ratna -
3
bhavani -
bhavani +
bhavani -

Output:
1
-2
-1


Explanation

Case 1 : Initially score = 0. Updation of scores in the order of user tilak's votes is as follows,

( + ): +1 is added to the final score. This is the 1st vote by this user, so no previous vote to nullify. score = 1
( + ):  0 should be added ( -1 to nullify previous (+) vote, +1 to count the current (+) vote ). score = 1
( - ) : -2 should be added ( -1 to nullify previous (+) vote, -1 to count the current (-) vote ). score = -1
( + ): +2 should be added ( +1 to nullify previous (-) vote, +1 to count the current (+) vote ). score = 1
'''

def get_score():
    num_test_cases = int(input())
    for i in range(1, num_test_cases+1):
        num_votes = int(input())
        voter_dict = {}
        count = 0
        for i in range(1, num_votes+1):
            voter, vote = raw_input().split()
            if voter in voter_dict.keys():
                if(voter_dict[voter] == '+' and vote == '-'):
                    count -= 2
                if(voter_dict[voter] == '-' and vote == '+'):
                    count += 2
                voter_dict[voter] = vote
            else:
                voter_dict[voter] = vote
                if(vote == '+'):
                    count += 1
                else:
                    count +=-1
        print count
get_score()
                    
        
            