from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    nummoves = 0

    count = 0
    for i in s:
        if i == '(': count += 1
        else: count -= 1

        if count < 0:
            nummoves += 1
            count = 0
    print(nummoves)




