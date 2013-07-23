'''
Created on Jul 21, 2013

@author: psgada
'''
import sys

def find_chopsticks():
    num, d = sys.stdin.readline().strip().split()
    num = int(num)
    d = int(d)
    cp_list = []
    cp_list_sel = []
    count = 0
    
    for i in range(0, num):
        cp = int(sys.stdin.readline().strip())
        cp_list.append(cp)
        cp_list_sel.append(False)
        
    cp_list.sort(cmp=None, key=None, reverse=False)
    
    
    for i in range(0, num-1):
        if cp_list_sel[i] == False:
            if cp_list[i+1] - cp_list[i] <= d:
                cp_list_sel[i] = True
                cp_list_sel[i+1] = True
                count += 1
                
                
    print count
    
find_chopsticks()