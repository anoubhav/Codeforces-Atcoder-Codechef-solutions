t = int(input())

# def repeat(s, n):
#     count = 0
#     ind = 0
#     while ind < n:
#         if ind+1<n and s[ind+1]!=s[ind]:
#             a, b = s[ind], s[ind+1]

#             lc, rc = 0, 0
#             for i in range(ind-1, -1, -1):
#                 if s[i] == a:
#                     lc += 1
#                 else:
#                     break

#             for i in range(ind+1 + 1, n):
#                 if s[i] == b:
#                     rc += 1
#                 else:
#                     break
            
#             count += (1 + min(lc, rc))
#             ind += (2 + min(lc, rc))
#         else:
#             ind += 1
#     return count
    
from collections import Counter
for _ in range(t):
    s = input()
    n = len(s)

    c = Counter(s)

    if c['0'] == 0 or  c['1'] == 0:
        print('NET')
    else:
        mi = min(c['0'], c['1'])
        if mi%2:
            print('DA')
        else:
            print('NET')
    # count1 = repeat(s, n)
    # count2 = repeat(s[::-1], n)

    # if count1%2 or count2%2:
    #     print('DA')
    # else:
    #     print('NET')
        
