n, k = map(int, input().split())

if n == 1 and k>0:
    print(-1)
elif n == 1 and k == 0:
    print(1)
else:

    nums = []

    if k < n//2:
        print(-1)
        exit()

    x = k - (n//2 - 1)

    # 1st pair
    nums.append(x)
    nums.append(2*x)

    # n//2 - 1 pairs.
    if x > 2*(n//2 - 1):
        nums.extend(range(1, 2*(n//2 - 1) + 1))
    else:
        nums.extend(range(2*x + 1, 2*x + 1 + 2*(n//2 - 1) + 1))


    if len(nums) < n:
        nums.append((nums[-1] + 1) if (nums[-1] + 1)!=x else (nums[-1] + 2))

    print(*nums[:n])