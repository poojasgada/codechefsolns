'''
Created on Jun 8, 2013

@author: psgada
'''

from math import sqrt

def get_input():
    num_cases = input()
    for i in range(1, num_cases+1):
        range_r = input()
        
        chef_pt = map(int, raw_input().split())
        head_pt = map(int, raw_input().split())
        sous_pt = map(int, raw_input().split())
        
        dist1 = sqrt((chef_pt[0]-head_pt[0])**2+(chef_pt[1]-head_pt[1])**2)
        dist2 = sqrt((chef_pt[0]-sous_pt[0])**2+(chef_pt[1]-sous_pt[1])**2)
        dist3 = sqrt((sous_pt[0]-head_pt[0])**2+(sous_pt[1]-head_pt[1])**2)
        count = 0
        if(dist1 <= range_r):
            count += 1
        if(dist2 <= range_r):
            count += 1
        if(dist3 <= range_r):
            count += 1
        
        if(count >=2):
            print "yes"
        else:
            print "no"
            
get_input()