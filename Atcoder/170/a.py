from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

nums = list(map(int, stdin.readline().split()))
for i, elem in enumerate(nums):
    if elem == 0:
        print(i + 1)
        exit()
