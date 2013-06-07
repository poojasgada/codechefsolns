'''
The chef is preparing a birthday cake for one of his guests, and his decided to write the age of the guest in candles on the cake. 
There are 10 types of candles, one for each of the digits '0' through '9'. The chef has forgotten the age of the guest, however, 
so doesn't know whether he has enough candles of the right types. For example, if the guest were 101 years old, the chef would need 
two '1' candles and one '0' candle. Given the candles the chef has, your task is to determine the smallest positive integer that cannot 
be represented with those candles.
Input:

Input will begin with an integer T100, the number of test cases. Each test case consists of a single line with exactly 10 integers, 
each between 0 and 8, inclusive. The first integer of each test case represents the number of '0' candles the chef has, the second 
integer represents the number of '1' candles the chef has, and so on.
Output:

For each test case, output on a single line the smallest positive integer that cannot be expressed with the given candles.
Sample input:

3
2 1 1 4 0 6 3 2 2 2
0 1 1 1 1 1 1 1 1 1
2 2 1 2 1 1 3 1 1 1
 

Sample output:

4
10
22
'''
#For any given age, find the digits in the age and find out if there are enough candles
#Brute force way gives time limit exceeded, is there any other way? 
#Determine how much time it is taking
 

def get_smallest_candle(candle_list_count):
    age_found = False
    smallest_age = 0
    age = 1
    while not age_found:
        temp_age = age
        temp_candle_list_count = []
        for i in range(0,10):
            temp_candle_list_count.append(candle_list_count[i])
        while temp_age != 0:
            candle = temp_age%10
            if temp_candle_list_count[candle] > 0:
                temp_candle_list_count[candle] -= 1
            else:
                age_found = True
                smallest_age = age
                temp_age = 0
            temp_age /=10
        age += 1


def get_smallest_candle1(candle_list_count):
    
    min_cand = min(candle_list_count)
    #The logic behind this is - Say the numbers of zeros is least in the candle list
    #That means the least age will always be of the form 1 followed by number_of_zeroes+1
    result = "1" + "0"*(min_cand+1)
    
    for i in range(1, 10):
        if(candle_list_count[i] == min_cand):
            #if the min in the candle list is not in zero index
            #Then count of digits+1 will be our solution
            result = str(i)*(min_cand+1)
            break
            
    print int(result)

def get_input():
     num_test_cases = int(input())
         
     
     for i in range(1, num_test_cases+1):
         candle_list_count = map(int, raw_input().split()) 
         get_smallest_candle1(candle_list_count)
     
get_input()