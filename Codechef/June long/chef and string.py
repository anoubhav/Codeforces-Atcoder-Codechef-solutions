t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    ans = 0
    i = 0
    while i< n-1:
        if s[i] + s[i+1] in ['xy', 'yx']:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)
