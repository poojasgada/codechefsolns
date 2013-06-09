'''
Created on Jun 7, 2013

@author: psgada
'''
'''
All submissions for this problem are available.

In an attempt to control the rise in population, Archer was asked to come up with a plan. This time he is 
targeting marriages. Archer, being as intelligent as he is, came up with the following plan:

A man with name M is allowed to marry a woman with name W, only if M is a subsequence of W or W is a subsequence 
of M.

A is said to be a subsequence of B, if A can be obtained by deleting some elements of B without changing the 
order of the remaining elements.

Your task is to determine whether a couple is allowed to marry or not, according to Archer's rule.
Input

The first line contains an integer T, the number of test cases. T test cases follow. Each test case contains 
two space separated strings M and W.
Output

For each test case print "YES" if they are allowed to marry, else print "NO". (quotes are meant for clarity, 
please don't print them)
Constraints

    1  T  100
    1  |M|, |W|  25000 (|A| denotes the length of the string A.)
    All names consist of lowercase English letters only.

Example

Input:
3
john johanna
ira ira
kayla jayla

Output:
YES
YES
NO

'''

#Not sure if its a efficient implementation
def find_subsequence(small_sub, large_sub):
    small_sub_len = len(small_sub)
    large_sub_len = len(large_sub)
    
    small_sub = list(small_sub)
    large_sub = list(large_sub)
    
    small_i = 0
    index_list = []
    sort_index_list = []
    
    while(small_i != small_sub_len):
        if(small_sub[small_i] in large_sub):
            index_list.append(large_sub.index(small_sub[small_i]))
            sort_index_list.append(large_sub.index(small_sub[small_i]))
        small_i += 1
        
    sort_index_list.sort()
    if(index_list == sort_index_list):
        print "YES"
    else:
        print "NO"
 
#A more efficient implementation
#Find is a really sweet function in python, you can specify what is the starting and ending index you want to search for
#It also returns the index of the sub string or character where it first occurs
#That way we are ensured that the search always progresses forward

def find_subsequence1(small_sub, large_sub):   
    i = -1
    
    for s_sub in small_sub:
        i = large_sub.find(s_sub, i+1,)
        if(i == -1):
            print "NO"
            break
    if( i!=-1 ):    
        print "YES"     
    
def get_input():
    num_test_cases = int(input())
    for i in range(1, num_test_cases+1):
        m_name, w_name = raw_input().split()
        
        m_name_len = len(m_name)
        w_name_len = len(w_name)
        
        if(m_name_len < w_name_len):
            find_subsequence1(m_name, w_name)
        elif(m_name_len > w_name_len):
            find_subsequence1(w_name, m_name)
        else:
            if(m_name == w_name):
                print "YES"
            else:
                print "NO"

get_input()