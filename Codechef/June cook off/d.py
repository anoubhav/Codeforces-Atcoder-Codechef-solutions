from sys import stdin
from collections import defaultdict as dd

t = int(input())
for _ in range(t):
    n, c = map(int, stdin.readline().split())
    reduced = dd(list)

    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        k = (x - x%c)//c
        reduced[(x%c, y - k*c)].append((x, y))
    
    numpts = len(reduced)
    nummoves = 0

    # print(reduced)
    for points in reduced.values():
        points.sort(key = lambda x: x[0])
        l = len(points)
        if l%2:
            median = points[(l-1)//2]
        else:
            median = points[(l)//2]

        # all points on the same line need not be reachable to the median. Which point is this reachable too?

        for x1, _ in points:
            nummoves += abs((median[0] - x1)//c)

        # print(points, median, nummoves)            
    print(numpts, nummoves)
