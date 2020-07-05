from sys import stdin, stdout
t = int(input())
answer = []
for _ in range(t):
    s = int(input())

    ans = 0
    back = 10
    while back!=0:
        back, rem = divmod(s, 10)
        ans += (s - rem)
        s = back + rem
    ans += s
    answer.append(ans)

print(*answer, sep = '\n')
