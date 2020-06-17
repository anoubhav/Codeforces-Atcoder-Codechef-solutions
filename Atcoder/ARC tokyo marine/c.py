from sys import stdin

# Uses accumulated sums technique O(N) + key insight that after log(N) operations the sequence converges to N, N, N..

n, k = map(int, input().split())
intensity = list(map(int, stdin.readline().split()))

# Time complexity: O(N log N)
count = 0
while count < k:
    totsum = 0
    prefs = [0]*n
    zeros = []
    for i in range(n):
        l = i - intensity[i]
        r = i + intensity[i] + 1

        prefs[max(l, 0)] += 1
        if r <= n-1: 
            prefs[r] += -1
            
    for i in range(1, n):
        prefs[i] += prefs[i-1]
        totsum += prefs[i]
    
    # very important to prevent TLE.
    if sum(prefs) == n*n:
        print(*prefs)
        exit()
    
    intensity = prefs
    count += 1

print(*prefs)