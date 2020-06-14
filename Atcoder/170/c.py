from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

x, n = map(int, input().split())
if n!=0: nums = set(map(int, stdin.readline().split()))

if n == 0:
    print(x)
    exit()

ans = 10**9
for i in range(10000):
    t1 = x + i if x+i not in nums else 10**4
    t2 = x - i if x-i not in nums else 10**4
    if t1!=10**4 or t2!=10**4:
        ans = min(t1, t2)
        print(ans)
        exit()