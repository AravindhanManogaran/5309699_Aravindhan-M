#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period = s[-2:]        # Extract 'AM' or 'PM'
    hour = int(s[:2])      # Extract the hour part as integer
    rest = s[2:-2]         # Extract the minutes and seconds part

    if period == 'AM':
        if hour == 12:
            hour = 0       # Convert 12AM to 00
    else:  # PM case
        if hour != 12:
            hour += 12     # Convert PM hour to 24-hour format

    return '{:02d}{}'.format(hour, rest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
