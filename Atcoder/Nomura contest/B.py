# 5 mins. Slow
from sys import stdin, stdout
s = stdin.readline()

# ans= 0
# for i, char in enumerate(s):
#     if i+1<len(s):
#         if s[i] == 'P' and s[i+1] == 'D':
#             ans += 1
    
#     if s[i] == '?' or s[i] == 'D':
#         ans += 1
# print(ans)

print(s.replace('?', 'D'))

