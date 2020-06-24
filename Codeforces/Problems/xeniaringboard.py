from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

# t = int(stdin.readline())
# for _ in range(t):
n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

numsteps = 0

start = 1

for i in nums:
    if i < start:
        numsteps += (n - start) + 1 + (i - 1)
        start = i
    elif i > start:
        numsteps += (i - start)
        start = i
print(numsteps)