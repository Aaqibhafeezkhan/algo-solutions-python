<<<<<<< HEAD:practice_problem_solutions (2026)/practice204.py
# HackerRank - Electronics Shop

def getMoneySpent(keyboards, drives, b):
    prices = []
    for kb in sorted(keyboards)[::-1]:
        for d in sorted(drives)[::-1]:
            if kb + d <= b:
                prices.append(kb + d)
    return max(prices) if prices else -1

print(getMoneySpent([40,50,60], [5,8,12], 60)) # 58
print(getMoneySpent([3,1], [5,2,8], 10)) # 9
=======
# HackerRank - Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t_1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t_2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(abs(int((t_1 - t_2).total_seconds())))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice204.py
