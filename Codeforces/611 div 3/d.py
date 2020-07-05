from sys import stdin
from collections import defaultdict as dd
import heapq

def firstn(n):
    return (n*(n+1))//2

nt, m = map(int, input().split())
trees = list(map(int, stdin.readline().split()))
mindist = 0
people = []

left = m
done = set(trees)
people = set()
dist = 1
while left>0:
    # O(N)...
    for tree in trees:
        if left == 0: break

        if left>0 and tree-dist not in done:
            mindist += dist
            left -= 1
            done.add(tree-dist)
            people.add(tree-dist)

        if left>0 and tree+dist not in done:
            mindist += dist
            left -= 1
            done.add(tree+dist)
            people.add(tree + dist)

    dist += 1

print(mindist)
print(*people)


        
        

        


