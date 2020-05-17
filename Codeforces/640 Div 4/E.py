# Unsolved:Didn't try coz of this warning:
# If you use Python, then submit solutions on PyPy. Try to write an efficient solution.
from sys import stdin
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split()))

    d = defaultdict(int) # frequency of elements in array
    maxnum = 0
    for num in arr:
        d[num] += 1
        if num>maxnum: maxnum = num
    
    special = set()
    ans = 0
    for i in range(n-1):
        ssf = arr[i]
        for j in range(i+1, n):
            ssf += arr[j]
            if ssf>maxnum:break   # TLE without this condition
            if d[ssf] and ssf not in special:
                special.add(ssf)
                ans += d[ssf]
    print(ans)
            

    
