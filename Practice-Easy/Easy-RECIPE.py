'''
Created on May 15, 2013

@author: psgada
'''
'''
The chef has a recipe he wishes to use for his guests, but the recipe will make far more food than he can serve to the guests. The chef therefore would like to make a reduced version of the recipe which has the same ratios of ingredients, but makes less food. The chef, however, does not like fractions. The original recipe contains only whole numbers of ingredients, and the chef wants the reduced recipe to only contain whole numbers of ingredients as well. Help the chef determine how much of each ingredient to use in order to make as little food as possible.
Input

Input will begin with an integer T, the number of test cases. Each test case consists of a single line. The line begins with a positive integer N, the number of ingredients. N integers follow, each indicating the quantity of a particular ingredient that is used.
Output

For each test case, output exactly N space-separated integers on a line, giving the quantity of each ingredient that the chef should use in order to make as little food as possible.
Sample Input

3
2 4 4
3 2 3 4
4 3 15 9 6

Sample Output

1 1
2 3 4
1 5 3 2


'''
import sys
#Find the GCD of the N numbers, then divide the numbers by the GCD

def get_gcd_base(num1, num2):
    while num1:
        num1, num2 = num2%num1, num1
    return num2

# Python has a really cool built-in function reduce, it recursively runs the function in first argument
# with all the elements in the list in the second argument   
def get_min_ingred(ingred_list):
    num_ingred = ingred_list.pop(0)

    gcd = reduce(get_gcd_base, ingred_list)
    for i in range(0,len(ingred_list)):
        ingred_list[i] = ingred_list[i]/gcd
    
    for ingred in ingred_list:
        print ingred,
    #Need to figure out a way to print the list of integers without new line    
         
# Python has yet another cool built-in function map, it runs the same function in the first argument
# with all the elements in the second argument
def get_input():
    num_test_cases = input()
    for num in range(1, num_test_cases+1):
        ingred_list = map(int, raw_input().split())
        get_min_ingred(ingred_list)
get_input()