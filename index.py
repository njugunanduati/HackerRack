#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = dict((i, ar.count(i)) for i in ar)
    pairs = []
    for k, v in result.items():
        if v != n:
            pairs.append(k)

    return pairs

if __name__ == '__main__':
    fptr = open('index.txt', 'w')

    n = int(input('Enter the number: '))
    
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
