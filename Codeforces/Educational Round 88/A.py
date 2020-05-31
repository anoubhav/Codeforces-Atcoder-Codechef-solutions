from sys import stdin, stdout
from math import ceil
t = int(input())
for _ in range(t):
    n, m, k = map(int, stdin.readline().split())

    if m == 0:
        print(0)

    elif n == k:
        print(1 if m <= 1 else 0)

    elif n/k >= m:
        print(m)

    else:
        ans = (n/k - ceil((m- (n/k))/( k - 1)))
        print(int(ans))

def discpage():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        most = min(m, n//k)
        m -= most
        rest = (m + k - 2)//(k - 1)
        print(most-rest)