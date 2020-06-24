from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    s = stdin.readline().strip()

    front = ''
    for i in s:
        if i == '0':
            front += '0'
        else:
            break
    
    back = ''
    for i in s[::-1]:
        if i == '1':
            back += '1'
        else:
            break
    
    if '10' in s:
        print(front + '0' + back)
    else:
        print(front + back)
            



    # prev_one_ind = -1
    # prev_zero_ind = -1
    # ans = ''
    # prev = s[0]
    # if prev == '0': prev_zero_ind = 0
    # else: prev_one_ind = 0
    # first = True
    # i = 1
    # # 11001101
    # while i < n:
    #     if s[i] == '0':
    #         if prev_one_ind < prev_zero_ind:
    #             i += 1
    #             continue
    #         else:
    #             # 0 occured after 1s, now back to 0.
    #             if prev_zero_ind!=-1:
    #                 ans +=(prev_one_ind - prev_zero_ind)*'0'
    #                 prev_zero_ind = i
    #             else:
    #                 prev_zero_ind = i

    #     elif s[i] == '1':
    #         if prev_one_ind > prev_zero_ind:
    #             i += 1
    #             continue
    #         else:
    #             # 111100000... 1
    #             if prev_one_ind!=-1:
    #                 if first: ans += '1'
    #                 else: 
    #                     ans += '0'
    #                     first = False

    #                 prev_one_ind = i
    #                 prev_zero_ind = -1
    #             else:
    #                 prev_one_ind = i
    #     i += 1

    # if prev_one_ind > prev_zero_ind:
    #     if prev_zero_ind!=-1:
    #         ans += (prev_one_ind - prev_zero_ind)*'0'
    #     ans += (n-prev_one_ind)*'1'

    # else:
    #     ans += '0'
    
    
    # print(ans)
    
