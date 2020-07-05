from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    q  = (n//m)*m
    left = n - q

    left = min(left, m//2)
    print(q + left)