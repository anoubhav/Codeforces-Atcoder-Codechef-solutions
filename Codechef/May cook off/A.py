from sys import stdin, stdout
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().strip().split()))

    # all frequencies are unique
    c = Counter(nums)
    if len(c.values()) != len(set(c.values())):
        print('NO')
        continue

    flag =1
    prev = nums[0]
    visited = set()
    for num in nums:
        if num == prev:
            prev = num
        else:
            if num in visited or prev in visited:
                print('NO')
                flag = 0
                break

            visited.add(prev)
            prev = num

    if flag:
        print('YES')