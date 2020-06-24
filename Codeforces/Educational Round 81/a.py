# Read the question wrong. implemented a wrong correct solution for 30 mins. 

from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(stdin.readline())
for _ in range(t):
    n = int(input())
    if n%2:
        print('7' + '1'*((n-3)//2))
    else:
        print('1'*(n//2))


