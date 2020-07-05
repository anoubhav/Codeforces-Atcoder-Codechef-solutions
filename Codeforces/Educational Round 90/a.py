from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
import math
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
# n, m = map(int, input().split())
# nums = list(map(int, stdin.readline().split()))

    a, b, c =  map(int, input().split())

    if a < (c/b):
        print(1, -1)
    elif a > c:
        print(-1, b)
    else:
        # c/b < a < c
        if a == c:
            print(-1, b)
        elif a == c/b:
            print(1, -1)
        else:
            print(1, b)

