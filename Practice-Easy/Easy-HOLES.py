'''
Created on May 14, 2013

@author: psgada
'''
'''
Question:
 Chef wrote some text on a piece of paper and now he wants to know how many holes are in the text. What is a hole? If you think of the paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. For example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each have one hole. Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say that the number of holes in the text is equal to the total number of holes in the letters of the text. Help Chef to determine how many holes are in the text.
Input

The first line contains a single integer T <= 40, the number of test cases. T test cases follow. The only line of each test case contains a non-empty text composed only of uppercase letters of English alphabet. The length of the text is less then 100. There are no any spaces in the input.
Output

For each test case, output a single line containing the number of holes in the corresponding text.
Example

Input:
2
CODECHEF
DRINKEATCODE

Output:
2
5
'''
holes_dict = {'A':1,'B':2,'C':0,'D':1,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':1,'P':1,'Q':1,'R':1,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

def count_holes(some_text):
    global holes_dict
    
    count = 0
    
    for ch in some_text:
        count = count+holes_dict[ch]
    print count
    
def get_input_test():
    num_input = input()
    
    for i in range(1,num_input+1):
        some_text = raw_input()
        count_holes(some_text)

get_input_test()  