# 5 mins. No errors. Good.
# Intuition: If palindrome exists, we can always find a 3 length palindrome (remove all middle elements until length is 3). For a 3 length palindrom, first and last characters are same. Thus, I just need to find the occurence of a character twice, ensuring they are not adjacent.

from sys import stdin
t = int(input())
for _ in range(t):
    n = int(stdin.readline())
    # n, m = map(int, stdin.readline().strip().split())
    nums = list(map(int, stdin.readline().strip().split()))

    d = dict()

    ans = 'NO'
    for i, num in enumerate(nums):
        if num in d:
            # prevent adjacent characters
            if i - d[num] > 1:
                ans = 'YES'
                break
        else:
            d[num] = i
    print(ans)