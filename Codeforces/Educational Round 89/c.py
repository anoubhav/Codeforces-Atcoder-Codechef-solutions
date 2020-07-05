from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
n, m = map(int, input().split())
matrix = []
for r in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# answer
ans = 0
# I arrived at the end of the range - (m+n-2)//2, by pen-paper, worst case I also have used the 'visited' list to ensure I am not checking the same elements from beggining and end.
for dist in range(1 + (m+n-2)//2):
    beg = {0: 0, 1: 0} # freq of 0s/1s at dist from start
    end = {0: 0, 1: 0} # freq of 0s/1s at dist from end
    visited = [] 
    for i in range(min(dist + 1, n)):
        j = dist - i  # i + j = dist
        if j < m :
            # from start
            beg[matrix[0 + i][0 + j]] += 1
            # from end
            end[matrix[n-1 - i][m-1 - j]] += 1
            # append indices
            visited.append((i, j))
            visited.append((n-1-i, m-1-j))

    # checking if index of element from beginning is not same as index of element from end
    if len(visited)!= 2*len(set(visited)): 
        # if num0s > num1s
        if beg[0] + end[0] >= beg[1] + end[1]:
            ans += beg[1] + end[1]
        # if num1s > num0s
        else:
            ans += beg[0] + end[0]
print(ans)





        
