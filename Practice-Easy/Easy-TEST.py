'''
Created on May 14, 2013

@author: psgada
'''
'''
Question
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. 
More precisely... rewrite small numbers from input to output. 
Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
'''

def life():
    num_list = []   
    num = 0
    
    while num!= 42:
        num = input()
        if num!=42:
            print num
        
life()