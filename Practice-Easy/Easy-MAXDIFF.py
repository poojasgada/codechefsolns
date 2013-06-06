'''
Created on Jun 3, 2013

@author: psgada
'''
'''
Chef has gone shopping with his 5-year old son. They have bought N items so far. The items are numbered from 1 to N, and the item i weighs Wi grams.

Chef's son insists on helping his father in carrying the items. He wants his dad to give him a few items. Chef does not want to burden his son. But he won't stop bothering him unless he is given a few items to carry. So Chef decides to give him some items. Obviously, Chef wants to give the kid less weight to carry.

However, his son is a smart kid. To avoid being given the bare minimum weight to carry, he suggests that the items are split into two groups, and one group contains exactly K items. Then Chef will carry the heavier group, and his son will carry the other group.

Help the Chef in deciding which items should the son take. Your task will be simple. Tell the Chef the maximum possible difference between the weight carried by him and the weight carried by the kid.
Input:

The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. The first line of each test contains two space-separated integers N and K. The next line contains N space-separated integers W1, W2, ..., WN.
Output:

For each test case, output the maximum possible difference between the weights carried by both in grams.
Constraints:

    1  T  100
    1  K < N  100
    1  Wi  100000 (105)

Example:

Input:
2
5 2
8 4 5 2 10
8 3
1 1 1 1 1 1 1 1

Output:
17
2

'''
def get_max_diff(item_weights, n, k):
    item_weights.sort()
    son_carries = 0
    dad_carries = 0
    
    # Ex: Say the weights are 1,2,3,4,5, if k = 4, n = 5 Sum[1-4] = 10 , Sum [5] = 5 , Diff = 5
    # k = 5-4 = 1, S[1] = 1, S[2-5] = 14. Diff = 13 - Max Weight Diff
    
    if(k > n/2):
        k = n-k
    for i in range(0,k):
        son_carries += item_weights[i]
    
    for i in range(k, n):
        dad_carries += item_weights[i]
    
    print dad_carries - son_carries

def get_input():
    num_test_cases = int(input())
    for i in range(1, num_test_cases+1):
        n, k = raw_input().split()
        n = int(n)
        k = int(k)
        item_weights = map(int, raw_input().split())
        get_max_diff(item_weights, n, k)
get_input()