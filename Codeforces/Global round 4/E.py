# https://codeforces.com/blog/entry/68534
from sys import stdin, stdout
s = stdin.readline().strip()
# s = input().strip()
n = len(s)
 
if n <= 3:
    print(s[0])
    # print s[0]
else:
    ans = ''
    start, end = 0, n-1
    while start + 1 < end - 1:
        if s[start] == s[end] or s[start] == s[end-1]:
            ans += s[start]
        else:
            ans += s[start+1]
            
        start += 2
        end -= 2
    
    t = len(ans)
    if 2*t < n//2:
        ans = ans + s[start] + ans[::-1]
        print(ans)
        # print ans 
        # stdout.write(ans)
    else:
        print(ans + ans[::-1])
        # print ans + ans[::-1]
        # stdout.write(ans + ans[::-1])