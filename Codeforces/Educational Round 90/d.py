from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
import math
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, stdin.readline().split()))

    sumeven = 0
    for i in range(0, n, 2):
        sumeven += nums[i]
    print(sumeven)

