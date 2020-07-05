from sys import stdin, stdout
from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    mat = []
    ans = [[0]*m for _ in range(n)]
    freq = defaultdict(int)

    for _ in range(n):
        nums = list(map(int, stdin.readline().strip().split()))
        for num in nums:
            freq[num] += 1
        mat.append(nums)
    
    if len(freq.keys()) == 1:
        ans = mat
        for row in ans:
            print(row)
        continue

    if len(freq.keys()) == n*m:
        print(-1)
        continue

    # construct the answer
    temp = sorted(freq.items(), key = lambda x: x[1]) # get the number with 

    for num, f in temp:
        if f%2 == 0:
            i = 0
            while i<m//2:
                ans[i] = num
                ans[m - 1 - i] = num
                f -= 2
        


    print(freq)
    print(mat)



    