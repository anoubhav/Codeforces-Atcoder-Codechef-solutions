t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))

    ans = 0
    for p in prices:
        if p>k:
            ans += p - k
    print(ans)