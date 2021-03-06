'''
Created on Jun 3, 2013

@author: psgada
'''
import itertools
from math import factorial, pow

def anagram_count(anagram_word):
    
    comb = set([ ''.join(word) for word in  itertools.permutations(anagram_word, len(anagram_word))])
    print len(comb)

def anagram_count1(anagram_word):
    anagram_list = list(anagram_word)
    anagram_dict = {}
    
    for anagram in anagram_list:
        if anagram in anagram_dict.keys():
            anagram_dict[anagram] += 1
        else:
            anagram_dict[anagram] = 1

    perm_anagram = factorial(len(anagram_word))
    temp_denom = 1
    for i in anagram_dict.keys():
        temp_denom *= factorial(anagram_dict[i])
    
    perm_anagram /= temp_denom    
    perm_anagram = perm_anagram % (1000000007)
    
    print int(perm_anagram)
    
def get_input():
    num_test_cases = int(input())
    for i in range(1, num_test_cases+1):
        anagram_word = raw_input()
        anagram_count1(anagram_word)
    
get_input()    