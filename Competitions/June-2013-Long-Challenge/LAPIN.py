'''
Created on Jun 7, 2013

@author: psgada
'''
'''


Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
Your task is simple. Given a string, you need to tell if it is a lapindrome.
Input:

First line of input contains a single integer T, the number of test cases.

Each test is a single line containing a string S composed of only lowercase English alphabet.


Output:

For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.

Constraints:

    1  T  100
    2  |S|  1000, where |S| denotes the length of S

Example:

Input:

6
gaga
abcde
rotor
xyzxy
abbaab
ababc


Output:

YES
NO
YES
YES
NO
NO

'''
import sys 

def find_lapin():
    num_test_cases = int(input())
    for i in range(1, num_test_cases+1):
        str_test = str(sys.stdin.readline().strip())
        if(len(str_test) % 2 == 0):
            len_mid = len(str_test)/2
        else:
            len_mid = len(str_test)/2 + 1
        
        sub1_dict = {}
        sub2_dict = {}
        

        for i in range(0,len(str_test)/2):
            if str_test[i] in sub1_dict.keys():
                sub1_dict[str_test[i]] += 1
            else:
                sub1_dict[str_test[i]] = 1
                       
        for i in range(len_mid, len(str_test)):
            if str_test[i] in sub2_dict.keys():
                sub2_dict[str_test[i]] += 1
            else:
                sub2_dict[str_test[i]] = 1
        
        lapin = "YES"
        for i in sub1_dict.keys():
            if(i in sub2_dict.keys()):
                if(sub1_dict[i] != sub2_dict[i]):
                    lapin = "NO"
                    break
            else:
                lapin ="NO"
                break
        
        print lapin
        
find_lapin()
        
        
        
    