'''
Created on Jun 20, 2013

@author: psgada
'''
'''
Chef has learned a new technique for comparing two recipes. A recipe contains a list of ingredients in increasing
 order of the times they will be processed. An ingredient is represented by a letter 'a'-'z'. The i-th letter in
  a recipe denotes the i-th ingredient. An ingredient can be used multiple times in a recipe.

The technique is as follows. Compare two recipes by comparing their respective lists. If the sets of ingredients
 used in both recipes are equal and each ingredient is used the same number of times in both of them (processing
  order does not matter), they are declared as granama recipes. ("granama" is the Chef-ian word for "similar".)

Chef took two recipes he invented yesterday. He wanted to compare them using the technique. Unfortunately, Chef
 forgot to keep track of the number of times each ingredient has been used in a recipe. He only compared the
  ingredients but NOT their frequencies. More precisely, Chef considers two recipes as granama if there are no
   ingredients which are used in one recipe and not used in the other recipe.

Your task is to report whether Chef has correctly classified the two recipes (as granama or not granama)
 although he forgot to keep track of the frequencies.
Input

The first line of the input contains a single integer T denoting the number of test cases. The description for
 T test cases follows. Each test case consists of a single line containing two space-separated strings R and S
  denoting the two recipes.
Output

For each test case, output a single line containing "YES" (quotes for clarity) if Chef correctly classified the
 two recipes as granama or not granama. Otherwise, output a single line containing "NO" (quotes for clarity) if
  Chef declared two recipes as granama when they actually are not.
Constraints

1  T  100
1  |R|, |S|  1000
Example

Input:

3
alex axle
paradise diapers
alice bob

Output:

YES
NO
YES

'''
import sys

def find_granama():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        recipe1, recipe2 = sys.stdin.readline().strip().split()
        
        if(set(list(recipe1)) != set(list(recipe2))):
            print "YES"
        else:
            if len(recipe1) != len(recipe2):
                   print "NO"
            #Its better to use list.sort() than sorted, because list.sort() does in place sorting and sorted() creates a new list
            else:
                recipe1 = list(recipe1)
                recipe2 = list(recipe2)
                recipe1.sort()
                recipe2.sort()
                j = 0
                while j < len(recipe1):
                    if(recipe1[j] != recipe2[j]):
                        break
                    j += 1

                if(j != len(recipe1)):
                    print "NO"
                else:
                    print "YES"
                    
find_granama()