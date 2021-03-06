'''
Created on Jun 8, 2013

@author: psgada
'''
'''
You are given a set of points in the 2D plane. You start at the point with the least X and greatest Y value, and end at the point with the greatest X and least Y value. The rule for movement is that you can not move to a point with a lesser X value as compared to the X value of the point you are on. Also for points having the same X value, you need to visit the point with the greatest Y value before visiting the next point with the same X value. So, if there are 2 points: (0,4 and 4,0) we would start with (0,4) - i.e. least X takes precedence over greatest Y. You need to visit every point in the plane.
Input

You will be given an integer t(1<=t<=20) representing the number of test cases. A new line follows; after which the t test cases are given. Each test case starts with a blank line followed by an integer n(2<=n<=100000), which represents the number of points to follow. This is followed by a new line. Then follow the n points, each being a pair of integers separated by a single space; followed by a new line. The X and Y coordinates of each point will be between 0 and 10000 both inclusive.
Output

For each test case, print the total distance traveled by you from start to finish; keeping in mind the rules mentioned above, correct to 2 decimal places. The result for each test case must be on a new line.
Example

Input:
3

2
0 0
0 1

3
0 0
1 1
2 2

4
0 0
1 10
1 5
2 2

Output:
1.00
2.83
18.21

For the third test case above, the following is the path you must take:
0,0 -> 1,10  
1,10 -> 1,5
1,5 -> 2,2
= 18.21

'''

from operator import itemgetter
from math import sqrt

def find_distance(points_list, num_points):
    points_list = sorted(points_list, key=itemgetter(1), reverse=True)
    points_list = sorted(points_list, key=itemgetter(0),reverse=False)
    sum = 0
    for i in range(0,num_points-1):
        sum += sqrt((points_list[i][0]-points_list[i+1][0])**2+(points_list[i][1]-points_list[i+1][1])**2)
    
    print "%.2f" %sum
def get_input():
    num_cases = int(input())
    for i in range(1, num_cases+1):
        points_list = []
        raw_input()
        num_points = int(input())
        for i in range(1, num_points+1):
            point = map(int, raw_input().split())
            points_list.append(point)
        
        find_distance(points_list, num_points)

get_input()