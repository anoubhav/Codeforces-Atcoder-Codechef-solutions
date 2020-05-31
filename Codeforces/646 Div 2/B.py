# 1 hr 30 mins. I went fully into implementation mode. And layed out multiple if/else complicated test cases once again. When I had left the contest. I got the trick. A and B are about a basic trick. So instead of implementing as soon as you see the question. Think a bit.

# 5 submission errors. total 1000 points. Got 300 points (the minimum possible: 30%). Very slow. And again too much belief on available cases.

# Intuition: The only valid strings are those with consecutive ones followed by consecutive zeros or vice - versa.

from sys import stdin, stdout
t = int(input())
answers = []
for _ in range(t):
    s = stdin.readline().strip()

    # edge cases
    if len(s)<3: 
        answers.append(0)
    
    elif len(s) == 3:
        if s == '010' or s== '101':
            answers.append(1)
        else:
            answers.append(0)
    else:
        # len > 3
        # prefix sums for O(N) solution. It computes the number of ones (and thus zeros) upto position i.
        pref = [0]*(len(s))
        tot = 0
        for i in range(len(s)):
            tot += int(s[i])
            pref[i] = tot

        ans = 10**4

        for i in range(1, len(s)):
            # Cost of no. of prior zeros + post ones
            a = (i - (pref[i-1])) + (pref[-1] - pref[i])
            # Cost of no. of prior ones + post zeros
            b = (pref[i-1]) + (len(s) - i - 1 - (pref[-1] - pref[i]))
            # answer is the minimum cost over all such strings.
            ans = min(ans, a, b)

        answers.append(ans)

print(*answers, sep = '\n')



#################### USELESS PREVIOUS INCORRECT ATTEMPTS ###########################

#             # if at zero, there are ones in the past and ones in the future
#             if s[i] == '0' and pref[i-1]>0 and pref[-1] - pref[i]>0:
#                 numzeros = 0
#                 for ind in range(i+1, len(s)):
#                     if pref[ind] > pref[i]:
#                         break
#                 numzeros = ind - i
#                 priorones = pref[i-1]
#                 postones = pref[-1] - pref[i]

#                 ans += min(numzeros, priorones, postones)

#                 if ans == numzeros:
#                     flip[i: i + (ind-i)] = [True]*ind
#                 elif ans == priorones:
#                     for ind in range(i):
#                         if s[ind] == '1': flip[ind] = True
#                 else:
#                     for ind in range(i+1):
#                         if s[ind] == '1': flip[ind] = True

#             # if at one, there are zeros in the past and zeros in the future
#             if s[i] == '1' and pref[i-1] < i and pref[-1] - pref[i] < (len(s) - i - 1):
#                 numones = 0
#                 for ind in range(i+1, len(s)):
#                     if pref[ind] == pref[ind - 1]:
#                         break
#                 numones = ind - i

#                 priorzeros = i - (pref[i-1])
#                 postzeros = len(s) - i - 1 - (pref[-1] - pref[i])

#                 ans += min(numones, priorzeros, postzeros)

#         answers.append(ans)

# print(*answers, sep = '\n')



# -------------------------------
# from sys import stdin, stdout
# t = int(input())
# answers = []
# for _ in range(t):
#     s = stdin.readline().strip()

#     # A string is called good if it does not contain "010" or "101" as a subsequence

#     if len(s)<3: 
#         answers.append(0)
    
#     elif len(s) == 3:
#         if s == '010' or s== '101':
#             answers.append(1)
#         else:
#             answers.append(0)
#     else:
#         # len > 3
#         pref = [0]*(len(s))
#         tot = 0
#         for i in range(len(s)):
#             tot += int(s[i])
#             pref[i] = tot

#         ans = 0
#         flip = [False]*(len(s))

#         for i in range(1, len(s)-1):
#             # if curr = 1 and the remaining is all 0s or all 1s and past all 1s, break
#             if s[i] == '1' and (tot - pref[i] == 0 or tot - pref[i] == len(s) - i) and pref[i-1] == i-1:
#                 break
            
#             # there are 0s in the future and 0s in the past. Flip
#             elif s[i] == '1' and tot - pref[i] < len(s) - i and pref[i-1] < i-1:
#                 flip[i] = True
#                 ans += 1
#                 for ind in range(i, len(s)):
#                     pref[ind] -= 1
#                 tot -= 1

#             # 1 before, 0 now, some 1 in the future. Either flip all 0s or all 1s.
#             elif s[i-1 ] == '1' and s[i] == '0' and tot - pref[i] >0 and not flip[i-1]:
#                 ans += min(len(s) - i - (tot - pref[i]) - (1 if s[-1] == '0' else 0), tot-pref[i])
#                 break
#         answers.append(ans)

# print(*answers, sep = '\n')


