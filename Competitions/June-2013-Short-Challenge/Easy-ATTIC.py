'''
Created on Jun 23, 2013

@author: psgada
'''
import sys

def find_days():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        strpass = sys.stdin.readline().strip()
        j = 0
        curmax = 0
        days = 0
        while j < (len(strpass) - 1 ):
            if strpass[j] == '.':
                k = j+1
                curcnt = 1
                while k < (len(strpass) - 1):
                    if strpass[k] == '.':
                        curcnt += 1
                        k += 1
                    else:
                        break
                    
                if curcnt > curmax:
                    curmax = curcnt
                    days += 1
                
                j = k
            else:
                j += 1
                    
        print days
        
find_days()