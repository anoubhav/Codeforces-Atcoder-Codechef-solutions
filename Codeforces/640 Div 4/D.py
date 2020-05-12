# https://codeforces.com/contest/1352/problems

# 13 mins to solve; Good use of double ended queue data structure

t = int(input())
from collections import deque
for _ in range(t):
    n = int(input())
    sizes = deque(map(int, input().split()))

    alice = 0
    bob = 0
    moves = 0
    last_round = 0

    while sizes:
        if moves == 0:
            moves += 1
            alice += sizes.popleft()
            last_round = alice
            if len(sizes) == 0:
                break
            continue

        if moves%2 == 1:
            # bob
            temp = 0
            while temp<=last_round and sizes:
                temp += sizes.pop()
            
            last_round = temp
            moves += 1
            bob += temp

            if len(sizes) == 0:
                break
            continue

        if moves%2 == 0:
            # alice
            temp = 0
            while temp<=last_round and sizes:
                temp += sizes.popleft()
            
            last_round = temp
            moves += 1
            alice += temp
            if len(sizes) == 0:
                break
            continue

    print(moves, alice, bob)
