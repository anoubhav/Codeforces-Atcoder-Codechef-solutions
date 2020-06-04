# 22 mins. Very very slow. Vlad and Scopula finished it in 9 and 15 mins. The question had a very very clear example. I should have done this in 15 mins tops.
from sys import stdin, stdout
q = int(input())
for _ in range(q):
    n = int(input())
    nums = list(map(int, stdin.readline().strip().split()))

    nums = [0] + nums
    ans = []

    # O(N^2) solution. N<=200.
    for i in nums[1:]:
        count = 1
        found = nums[i]
        while found!=i:
            found = nums[found]
            count += 1

        ans.append(count)

    print(*ans)

    




