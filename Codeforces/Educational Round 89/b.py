from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
n,x, m = map(int, input().split())
flag = 0
rsf = None #rsf: range so far
for tup in range(m):
    l, r = map(int, input().split())
    if l <= x <= r or flag:
        flag = 1
        if not rsf: rsf = [l, r]
        else:
            # if they intersect expand
            if l <= rsf[0] <= r or l <= rsf[1] <= r:
                rsf = [min(rsf[0], l), max(rsf[1], r)]

print((rsf[1] - rsf[0] + 1) if not rsf else 1)

    
                

        
