from sys import stdin
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2, floor, ceil
# from fractions import Fraction

t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())

    ops = 0
    while max(a, b) <= n:
        a, b = max(a, b), a+b
        ops += 1

    print(ops)
