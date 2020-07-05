from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2, ceil
from fractions import Fraction

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a== 0 or b == 0:
        print(0)
        continue


    if b>a:
        a, b = b, a

    if a >= 2*b:
        print(b)
        continue
    else:
        # a < 2*b
        ans = 0
        diff = a - b
        ans += diff
        a = a - 2*diff
        b = b - diff

        ans += 2*(a//3) + (1 if a%3 == 2 else 0)

        print(ans)
    
    # diff = a - b
    # ans += diff//2
    # b = b - diff
    # a = a - 2*(diff//2)

    # if b>a:
    #     a, b = b, a

    # while a > 0 and b>0:
    #     if a <=1 and b <= 1:
    #         break
    #     if a > b and a > 1:
    #         ans += 1
    #         a -= 2
    #         b -= 1
    #     elif b >= a and b > 1:
    #         ans += 1
    #         b -= 2
    #         a -= 1
    # print(ans)

