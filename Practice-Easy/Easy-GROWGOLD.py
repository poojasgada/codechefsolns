'''
Created on Jun 20, 2013

@author: psgada
'''
'''
 Long ago there was a beautiful kingdom in the island of Sona, the golden island, deep inside Africa. 
 The trees in Sona island are made of gold and farmers are the richest group of people and are also heavy 
 tax payers.

As you know that price of gold increases every year, the minister of Sona has proposed the following tax policy.

    Pay initTax units of gold in the first year.

    In each of the next slot1 years, pay one unit of gold more than the previous year.

    In each of the next slot2 years, pay double the units of gold of the previous year.

    In each of the following years, pay number of gold units equal to the product of the number of units paid 
    in K recent years.


Given an integer N, find the number of units of gold to be paid in the Nth year. This result can be huge, 
so output the result modulo 100000007 (108+7).
Input

First line has an integer T (number of test cases, 1  T  3). Each of the next T lines has 5 integers, 
initTax slot1 slot2 K N.
1  initTax, slot1, slot2  50
1  K  slot1 + slot2 + 1
1  N 1000000000 (109)
Output

For each test case, output the tax in units of gold to be paid in the Nth year modulo 100000007 (108+7).
Example

Input:
3
1 3 2 4 4
1 3 2 4 7
1 3 2 4 9

Output:
4
1536
18811834


'''

#Starting tax is the same as init tax
#slot1 years cur_tax = prev_tax+1
#slot2 years cur_tax = 2*prev_tax
#Every othere onwards product of tax of previous k years
#Output has to be mod 100000007

#Only question i still have is, N can take really huge values, upto around 10^6, is storing all the values really required?
#We can possibly save only the last k values in the array, it will surely be space efficient - Need to implement this change

#Question is kinda ridiculous, how can N be 10^9 when both slot1 and slot2 cannot be greater than 50
import sys

def find_tax(init_tax, slot1, slot2, k, n):
    cur_tax_list = []
    cur_tax_list.append(init_tax)
    
    #i will always have the current index
    i = 0
    
    #We only compute the taxes upto the required year
    while(len(cur_tax_list) != n):            
        if slot1 != 0:
            cur_tax_list.append(cur_tax_list[i] + 1)
            slot1 -= 1
        elif(slot2 != 0):
            cur_tax_list.append(cur_tax_list[i] *2)
            slot2 -= 1
        else:
            #Pay for next k years
            temp_tax = 1
            
            for j in range(0, k):
                temp_tax *= cur_tax_list[i - j]
            cur_tax_list.append(temp_tax)
            
        i += 1
    
    #Since we only compute the values upto the year n, the required result will be in the end of the list
    print cur_tax_list[len(cur_tax_list)-1] % 100000007
            

def get_input():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        num_list = map(int, sys.stdin.readline().strip().split())
       
        find_tax(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4])


get_input()