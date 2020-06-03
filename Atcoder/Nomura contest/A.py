# 3.5 mins slow.
from sys import stdin, stdout
# t = int(input())
# for _ in range(t):
    # n = int(stdin.readline())
h1, m1, h2, m2, k = map(int, stdin.readline().strip().split())
    # nums = list(map(int, stdin.readline().strip().split()))

t = (h2*60 + m2 - (h1*60 + m1) -  k)
print(t if t>0 else 0)