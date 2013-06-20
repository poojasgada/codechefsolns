'''
Created on Jun 18, 2013

@author: psgada
'''


'''
Little kids, Jack and Evan like playing their favorite game Glass-and-Stone. Today they want to play something 
new and came across Twitter on their father's laptop.

They saw it for the first time but were already getting bored to see a bunch of sentences having at most 140 
characters each. The only thing they liked to play with it is, closing and opening tweets.

There are N tweets on the page and each tweet can be opened by clicking on it, to see some statistics related 
to that tweet. Initially all the tweets are closed. Clicking on an open tweet closes it and clicking on a 
closed tweet opens it. There is also a button to close all the open tweets. Given a sequence of K clicks by Jack,
 Evan has to guess the total number of open tweets just after each click. Please help Evan in this game.
Input

First line contains two integers N K, the number of tweets (numbered 1 to N) and the number of clicks 
respectively (1  N, K  1000). Each of the following K lines has one of the following.

    CLICK X , where X is the tweet number (1  X  N)
    CLOSEALL


Output

Output K lines, where the ith line should contain the number of open tweets just after the ith click.
Example

Input:
3 6
CLICK 1
CLICK 2
CLICK 3
CLICK 2
CLOSEALL
CLICK 1

Output:
1
2
3
2
0
1

'''

import sys

def find_open_tweets():
    num_list = sys.stdin.readline().split()
    num_tweets = int(num_list[0])
    num_clicks = int(num_list[1])
    
    #Using a list comprehension to set all the list values to 0
    tweet_list = [0 for i in range(0, num_tweets)]
    
    #print tweet_list
    
    open_count = 0
    
    for i in range(0, num_clicks):
        action = sys.stdin.readline().split()
        
        #Check for the action, if its click, then switch the states
        if action[0] == 'CLICK':
            if(tweet_list[int(action[1])-1] == 1 ):
                tweet_list[int(action[1])-1] = 0
                open_count -= 1
            else:
                tweet_list[int(action[1])-1] = 1
                open_count += 1
        else:
            tweet_list = [0 for i in range(0, num_tweets)]
            open_count = 0
        
        #print tweet_list
        print open_count
        
find_open_tweets()