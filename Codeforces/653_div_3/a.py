# got hacked after contest. Very important discussions thread over here https://codeforces.com/blog/entry/79433#comments. Search for 'anoubhav'.



import sys
input = sys.stdin.readline


## Unused imports increase the time by 150ms
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction


t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    mxmult = (n//x)*x

    if mxmult + y <= n:
        # maximum multiple + y
        print(mxmult + y)
    else:
        # second maximum multiple + y. Both below are right. Second is faster.

        # print((n//x - 1)*x + y)
        print(mxmult - x + y)



#  In Python, printing does not flush stdout. It is the call to input that flushes stdout. The implementation of input is that it first flushes and then calls sys.stdin.readline. So to not flush, simply use something like input = sys.stdin.readline

