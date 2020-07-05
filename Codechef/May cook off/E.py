from sys import stdin, stdout
from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().strip().split()))

    # prefix arr [i]: the # of people with strictly greater heights to left of i.

    # if curr < prev: pref arr[curr] = prev + 1; if curr == prev: pref arr[curr] = prev; 
    # if curr > prev: go to the closest elem which is greater than prev.

    pref = [(nums[0], -1)]
    prev = nums[0]
    for num in nums[1:]:
        if num > 
