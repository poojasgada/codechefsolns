'''
Created on Jun 12, 2013

@author: psgada
'''
'''
Input:

5
140 82
89 134
90 110
112 106
88 90

Output:

1 58
'''

import sys
from math import fabs

def find_lead():
    num_cases = int(input())
    lead_player = -1
    lead_score = -1
    p1_score = 0
    p2_score = 0
    
    for i in range(1, num_cases+1):
        temp_p1_score, temp_p2_score = sys.stdin.readline().split()
        p1_score += int(temp_p1_score)
        p2_score += int(temp_p2_score)
        
        temp_lead = fabs(p1_score - p2_score)
        
        if(temp_lead > lead_score):
            lead_score = temp_lead
            if(p1_score > p2_score):
                lead_player = 1
            else:
                lead_player = 2
    print "%d %d" %(lead_player, lead_score)
        
find_lead() 