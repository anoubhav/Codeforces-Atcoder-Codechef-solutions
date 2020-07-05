from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

n = int(input())
num = list(map(int, list(input().strip())))

mapping = list(map(int, stdin.readline().split()))

mapping = [0] + mapping
start = 0
for i, digit in enumerate(num):
    if mapping[digit] > digit:
        start = 1
        num[i] = mapping[digit]

    elif mapping[digit] < digit and start:
        break

print(*num, sep='')

