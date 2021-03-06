'''
Created on Jun 23, 2013

@author: psgada
'''
from math import factorial
import sys

def ncr(n, r):
    
    if n == r :
        return  1
    elif n > r :
        return factorial(n) / (factorial(r) * (factorial(n-r)))
    else:
        return 0

def find_free_place(train_list, r):
    
    count = 0
    
    compt1 = train_list[0] + train_list[1] + train_list[2] + train_list[3] + train_list[52] + train_list[53]
    count+= int(ncr(compt1, r))
        
    compt2 = train_list[4] + train_list[5] +train_list[6] +train_list[7] +train_list[50] +train_list[51]
    count+= int(ncr(compt2, r))
        
    compt3 = train_list[8] +train_list[9] +train_list[10] +train_list[11] +train_list[48] +train_list[49] 
    count+= int(ncr(compt3, r))
        
    compt4 = train_list[12] +train_list[13] +train_list[14] +train_list[15] +train_list[46] +train_list[47] 
    count+= int(ncr(compt4, r))
        
    compt5 = train_list[16] +train_list[17] +train_list[18] +train_list[19] +train_list[44] +train_list[45] 
    count+= int(ncr(compt5, r))
    
    compt6 = train_list[20] +train_list[21] +train_list[22] +train_list[23] +train_list[42] +train_list[43] 
    count+= int(ncr(compt6, r))
    
    compt7 = train_list[24] +train_list[25] +train_list[26] +train_list[27] +train_list[40] +train_list[41] 
    count+= int(ncr(compt7, r))
    
    compt8 = train_list[28] +train_list[29] +train_list[30] +train_list[31] +train_list[38] +train_list[39]
    count+= int(ncr(compt8, r))
    
    compt9 = train_list[32] +train_list[33] +train_list[34] +train_list[35] +train_list[36] +train_list[37]   
    count+= int(ncr(compt9, r))
            
    
    return count

def get_input():
    num_list = map(int, sys.stdin.readline().strip().split())
    
    num_ways = 0
    for i in range(0, num_list[1]):
        train_string = sys.stdin.readline().strip()
        
        train_list = []
        for i in range(0, len(train_string)):
            if(train_string[i] == '1'):
                train_list.append(0)
            else:
                train_list.append(1)
        
        num_ways += find_free_place(train_list, num_list[0])
        
    print num_ways
    
get_input()