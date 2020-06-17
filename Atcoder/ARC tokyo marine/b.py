from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2, ceil
from fractions import Fraction

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if w == v:
    print('NO')
elif w > v:
    print('NO')
else:
    # w < v
    if a > b:
        ans = (a-b)/(v-w)
        print('YES' if ceil(ans) <= t else 'NO')
    else:
        ans = (a-b)/(w-v)
        print('YES' if ceil(ans) <= t else 'NO')


