#Used HackerRank to solve this problem https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=false

#Might not run beacuse the test cases are missing

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    #-inf allows us to take smaller numbers into consideration incase the array is only negative numbers
    #that way if the max_sum is below 0 we can output that value and not just 0 (which would be incorrect)
    max_sum = float('-inf')
    if len(arr)<6:
        return -1
    else:
        #We use -2 so that the iteration stops to the third to last column or row, that way we can have 
        #enough space for the next hourglass
        for i in range(len(arr)-2):
            for j in range(len(arr)-2):
                #The top row is the usually the first element of the matrix followed by the second and third element 
                # in the same row, we access this through i & j, i remains the same because its the same row, j continuoslly updates
                #because the column for the next value changes
                top_row = arr[i][j]+ arr[i][j+1]+arr[i][j+2]
                middle_row= arr[i+1][j+1]
                # The middle row is always eQual value rows and columns example [3][3], [6][6], thats why i & j are the same value
                bottom_row= arr[i+2][j]+ arr[i+2][j+1]+ arr[i+2][j+2]
                #The bottom row is similar to the top row, same mechanism
                hourglass_sum=top_row+middle_row+bottom_row # total sum of the hourglass
                max_sum=max(max_sum,hourglass_sum) #what we are doing here is checking to see which value is the maximum between the 
                #two variables, which ever one is the maximum, is the one that remains and gets assigned to the variable
    
    return max_sum
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
