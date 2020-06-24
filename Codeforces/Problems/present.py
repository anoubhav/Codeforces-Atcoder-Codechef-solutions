n = int(input())
nums = list(map(int, input().split()))

ans = [0]*n

for i, elem in enumerate(nums):
    ans[elem-1] = i + 1

print(*ans)