import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_positive = 0
    count_negative = 0
    count_zero = 0
    for i in arr:
        if i > 0 :
            count_positive = count_positive + 1
        elif i < 0:
            count_negative = count_negative + 1
        elif i == 0:
            count_zero = count_zero + 1
    positive_ratio = count_positive/len(arr)
    negative_ratio = count_negative/len(arr)
    zero_ratio = count_zero/len(arr)
    return print_format(positive_ratio), print_format(negative_ratio),print_format(zero_ratio)


def print_format(ratio):
    return print('{0:6f}'.format(ratio))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
