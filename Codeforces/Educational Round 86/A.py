# 6 mins. No submission errors. Decent. Confidence in solution could be more, as implementation took 1-2 minutes. But proving that only two cases exist took some time.

from sys import stdin, stdout
t = int(input())
for _ in range(t):
    x, y = map(int, stdin.readline().split())
    a, b = map(int, stdin.readline().split())

    ans = 0
    if a == 0 and b ==0:
        print(0)
        continue

    if b>=2*a:
        # b is useless
        ans = (x+y)*a
        print(ans)
    else:
        z = min(x, y)
        k = max(x, y)
        ans += b*z
        # decrease both by 1, z times
        ans += a*(k-z)
        print(ans)

