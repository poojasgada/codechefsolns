'''
Created on May 29, 2013

@author: psgada
'''
'''
A Little Elephant and his friends from the Zoo of Lviv like candies very much.

There are N elephants in the Zoo. The elephant with number K (1  K  N) will be happy if he receives at least AK candies. There are C candies in all in the Zoo.

The Zoo staff is interested in knowing whether it is possible to make all the N elephants happy by giving each elephant at least as many candies as he wants, that is, the Kth elephant should receive at least AK candies. Each candy can be given to only one elephant. Print Yes if it is possible and No otherwise.
Input

The first line of the input file contains an integer T, the number of test cases. T test cases follow. Each test case consists of exactly 2 lines. The first line of each test case contains two space separated integers N and C, the total number of elephants and the total number of candies in the Zoo respectively. The second line contains N space separated integers A1, A2, ..., AN.
Output

For each test case output exactly one line containing the string Yes if it possible to make all elephants happy and the string No otherwise. Output is case sensitive. So do not print YES or yes.
Constraints

1  T  1000

1  N  100

1  C  109

1  AK  10000, for K = 1, 2, ..., N
Example

Input:
2
2 3
1 1
3 7
4 2 2

Output:
Yes
No


'''
def yes_or_candy():
    num_test_cases = int(input())
    for i in range(1, num_test_cases+1):
        num_ele, num_candy = raw_input().split()
        num_ele = int(num_ele)
        num_candy = int(num_candy)
        candy_list = map(int, raw_input().split())
        candy_needed = reduce(lambda x,y:x+y,candy_list)
        if candy_needed > num_candy:
            print 'No'
        else:
            print 'Yes'
yes_or_candy()