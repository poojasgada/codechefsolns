'''
Created on Jun 11, 2013

@author: psgada
'''
'''
6
3
60
100
1024
23456
8735373

0
14
24
253
5861
2183837
'''
def find_num_zeros(num):
    #The number of zeros will directly depend on the number of 5's
    #num=25, num of 5's = 5,10,15,20,25 = 6, num/5 + num/25
    #num = 60, num of 5's = num/5+num/25
    divisor = 5
    num_count = 0
    while num/divisor > 0 :
        num_count += num/divisor
        divisor *= 5
        
    print num_count
    
    
def get_input():
    num_cases = int(input())
    for i in range(1, num_cases+1):
        num = int(input())
        
        find_num_zeros(num)

get_input()