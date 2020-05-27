# 7 mins. No errors. Took time to understand the question.

from sys import stdin
t = int(input())
for _ in range(t):
    n = int(stdin.readline())
    # n, m = map(int, stdin.readline().strip().split())
    nums = list(map(int, stdin.readline().strip().split()))

    nums.sort()

    prev = nums[0]
    ans = 'YES'
    for num in nums[1:]:
        if (num - prev)%2 == 1:
            ans = 'NO'
            break
    print(ans)

# Editorial soln
# Intuition: The answer is "YES" only if all ai have the same parity (i.e. all ai are odd or all ai are even). That's because placing the block doesn't change the parity of the element and the −1 operation changes the parity of all elements in the array.

# When I solved it, I thought all blocks should differ only by multiples of two. This is same as, they should have same parity.
# for i in range(int(input())):
# 	n = int(input())
# 	cnto = sum(list(map(lambda x: int(x) % 2, input().split())))
# 	print('YES' if cnto == 0 or cnto == n else 'NO')