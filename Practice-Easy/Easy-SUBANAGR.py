'''
Created on Jul 4, 2013

@author: psgada
'''
'''
Recently, Ann received a set of strings consisting of small Latin letters a..z. 'What can I do with them?' -- 
she asked herself. 'What if I try to find the longest string which is a subsequence of every string from the set?
'. Ann spent a lot of time trying to solve the problem... but all her attempts happened to be unsuccessful. She 
then decided to allow the sought string to be an anagram of some subsequence of every string from the set. This 
problem seemed to be easier to Ann, but she was too tired to solve it, so Ann asked for your help.

So your task is, given a set of strings, to find the longest non-empty string which satisfies Ann. Moreover, if 
there are many such strings, choose the lexicographically smallest one. 
'''
import sys

def find_sub_anagram():
    num_strings = int(sys.stdin.readline().strip())
    
    sub_anagram_dict = {}
    
    init_string = sys.stdin.readline().strip()
    for i in range(0, len(init_string)):
        if init_string[i] in sub_anagram_dict.keys():
            sub_anagram_dict[init_string[i]] += 1
        else:
            sub_anagram_dict[init_string[i]] = 1
            
    anagram = True
    for i in range(0, num_strings-1):
        t_str = sys.stdin.readline().strip()
        t_str_dict = {}
        
        for j in range(0, len(t_str)):
            if t_str[j] in t_str_dict.keys():
                t_str_dict[t_str[j]] += 1
            else:
                t_str_dict[t_str[j]] = 1
                
        for key in sub_anagram_dict.keys():
            if key in t_str_dict.keys():
                sub_anagram_dict[key] = min(sub_anagram_dict[key], t_str_dict[key])
            else:
                sub_anagram_dict.pop(key)
    
        if len(sub_anagram_dict) == 0:
            anagram = False
            break
    #print sub_anagram_dict
    if anagram:
        result_list = [key*sub_anagram_dict[key] for key in sub_anagram_dict.keys()]
        result_list.sort()
        print ''.join(result_list)
    else:
        print "no such string"
    
find_sub_anagram()
