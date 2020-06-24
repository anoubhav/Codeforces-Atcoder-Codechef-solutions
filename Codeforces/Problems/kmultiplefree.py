from sys import stdin
n, k = map(int, stdin.readline().split())

nums = list(map(int, stdin.readline().split()))
nums.sort()

count = 0
new = set()
for i in nums:
    if i%k:
        new.add(i)
    else:
        if i//k in new:
            pass
        else:
            new.add(i)
print(len(new))