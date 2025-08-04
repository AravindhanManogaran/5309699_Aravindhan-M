#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
        total = sum(arr)
        min_val = min(arr)
        max_val = max(arr)
    
        min_sum = total - max_val
        max_sum = total - min_val
    
        print(f"{min_sum} {max_sum}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
