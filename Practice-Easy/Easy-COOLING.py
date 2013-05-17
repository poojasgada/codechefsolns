'''
Created on May 15, 2013

@author: psgada
'''
'''
The chef has just finished baking several pies, and it's time to place them on cooling racks. 
The chef has exactly as many cooling racks as pies. Each cooling rack can only hold one pie, and each pie
 may only be held by one cooling rack, but the chef isn't confident that the cooling racks can support the weight of the pies. 
 The chef knows the weight of each pie, and has assigned each cooling rack a maximum weight limit.
 What is the maximum number of pies the chef can cool on the racks?
  
 Input begins with an integer, the number of test cases. Each test case consists of 3 lines. 
 The first line of each test case contains a positive integer the number of pies (and also the number of racks). The second and third lines each contain exactly positive N integers not exceeding 100. The integers on the second line are the weights of the pies, 
 and the integers on the third line are the weight limits of the cooling racks.
 
Output:

For each test case, output on a line the maximum number of pies the chef can place on the racks.
Sample input:

2
3
10 30 20
30 10 20
5
9 7 16 4 8
8 3 14 10 10
 

Sample output:

3
4
 
'''

def count_pies(num_pies, pie_weight, rack_weight):
    pie_weight.sort()
    rack_weight.sort()
    pie_c = 0
    rack_c = 0
    
    for i in range(0, num_pies):
        if(rack_weight[rack_c] < pie_weight[pie_c]):
            rack_c = rack_c + 1
        else:
            rack_c = rack_c + 1
            pie_c = pie_c + 1
    print min(rack_c, pie_c)
    
def get_input():
    num_test_cases = int(raw_input())
    for num in range(1, num_test_cases+1):
        num_pies = input()
        pie_weight = map(int, raw_input().split())
        rack_weight = map(int, raw_input().split())
        count_pies(num_pies, pie_weight, rack_weight)
        
get_input()
        
 