from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
import math
from math import sqrt, log, log2
from fractions import Fraction
import random
def simulation(s):
    res = 0
    for init in range(0, 10**6 + 10):
        cur = init
        ok = True
        for i in range(len(s)):
            res = res + 1
            if s[i] == '+':
                cur = cur + 1
            else:
                cur = cur - 1
            if cur < 0:
                ok = False
                break
        if ok:
            break
    return res


t = int(input())
for _ in range(t):
    s = stdin.readline().strip()
    # s = ''.join(random.choices(['+', '-'], k = 100000))

    plus, minus = 0, 0
    plustreak = 0
    n = len(s)

    i = 0
    res = 0
    while i < n:
        if s[i] == '+':
            res += 1
            plus += 1
            plustreak += 1
        else:
            minus+=1
            
            if i>0 and s[i-1] == '+':
                res += 1
            else:
                if plus>=minus:
                    res += 1
                else:
                    # plus < minus:
                    if plustreak:
                        res += 1
                    else:
                        res += ((i+1) + 1)
            plustreak = max(0, plustreak - 1)
        i += 1

    print(res)
    # if res!= simulation(s):
        # print(res, simulation(s), s)
                

