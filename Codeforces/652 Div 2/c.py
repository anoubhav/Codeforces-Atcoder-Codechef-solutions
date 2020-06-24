from sys import stdin
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    integers = list(map(int, stdin.readline().split()))
    toeach = list(map(int, stdin.readline().split()))

    integers.sort()
    toeach.sort()

    integers = deque(integers)

    h = 0
    ind = 0
    rev = k-1
    while integers:
        num_ints = toeach[ind]

        if num_ints == 1:
            h += 2*integers.pop()
            ind += 1
        
        elif num_ints == 2:
            h += (integers.pop() + integers.pop())
            ind += 1

        else:
            # > 2
            num_ints = toeach[rev]
            # if num_ints > 2. give it 1 largest, rest smallest
            h += integers.popleft()
            h += integers.pop()
            num_ints -= 2

            # keep popping off the smallest
            while num_ints and integers:
                integers.popleft()
                num_ints -= 1
            
            rev -= 1

    print(h)
    
            
        




