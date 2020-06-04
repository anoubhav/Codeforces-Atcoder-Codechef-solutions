# 12 mins. Very slow. No submision errors. Scopula took 4 mins.

from sys import stdin, stdout
q = int(input())
answers = []
for _ in range(q):
    n = int(input())
    nums = list(map(int, stdin.readline().strip().split()))
    d = dict()

    for i in nums:
        d[i] = 0

    ans = 1
    for i in nums:
        if i+1 in d:
            ans = 2 
            break
    
    answers.append(ans)

print(*answers, sep = '\n')