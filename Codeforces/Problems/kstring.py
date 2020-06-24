from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

k = int(stdin.readline())
s = input()

from collections import Counter

c = Counter(s)
onecopy = ''
for key, v in c.items():
    if v%k:
        print(-1)
        exit()
    
    onecopy += key*(v//k)

print(onecopy*k)

    