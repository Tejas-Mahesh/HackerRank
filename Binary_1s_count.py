import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    binary = bin(n)[2:]
    max_count = 0
    count = 0

    for digit in binary:
        if digit == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
