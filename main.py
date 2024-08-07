#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    page_count = 0
    if (p > n // 2):
        if (n % 2 == 0 and p % 2 == 0):
            page_count = ((n - p) // 2)
        elif (n % 2 == 0 and p % 2 != 0):
            page_count = ((n - p) // 2) + 1
        else:
            page_count = ( n - p ) // 2
    else:
        page_count = p // 2
    
    print(page_count)
            
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    # fptr.write(str(result) + '\n')

    # fptr.close()