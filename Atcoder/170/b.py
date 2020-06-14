from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

x, y = map(int, input().split())

if y%2==1:
    print('No')
    exit()

if y > 4*x or y < 2*x:
    print('No')
    exit()

print('Yes')
