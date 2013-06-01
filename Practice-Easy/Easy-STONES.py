'''
Created on May 29, 2013

@author: psgada
'''
'''
Soma is a fashionable girl. She absolutely loves shiny stones that she can put on as jewellery accessories. 
She has been collecting stones since her childhood - now she has become really good with identifying which ones
 are fake and which ones are not. Her King requested for her help in mining precious stones, so she has told him
  which all stones are jewels and which are not. Given her description, your task is to count the number of jewel 
  stones. More formally, you're given a string J composed of latin characters where each character is a jewel. 
  You're also given a string S composed of latin characters where each character is a mined stone. You have to 
  find out how many characters of S are in J as well.
Input

First line contains an integer T denoting the number of test cases. Then follow T test cases. Each test case 
consists of two lines, each of which contains a string composed of English lower case and upper characters. 
First of these is the jewel string J and the second one is stone string S. You can assume that 1 <= T <= 100, 
1 <= |J|, |S| <= 100
Output

Output for each test case, a single integer, the number of jewels mined.
Example

Input:
4
abc
abcdef
aA
abAZ
aaa
a
what
none

Output:
3
2
1
0
'''
def find_jewels(jewels, stones):
    jewel_list = list(jewels)
    stone_list = list(stones)
    jewels_count = 0
    jewels_dict = {}
    
    for jewel in jewel_list:
        if jewel in jewels_dict:
            a = 0
        else:
            jewels_dict[jewel] = 1
    
    for stone in stone_list:
        if stone in jewels_dict:
            jewels_count += 1
    print jewels_count
    

def get_input():
    num_test_cases = int(input())
    
    for i in range(1, num_test_cases+1):
        jewels = raw_input()
        stones = raw_input()
        find_jewels(jewels, stones)
        
get_input()
    