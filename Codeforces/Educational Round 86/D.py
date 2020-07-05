from sys import stdin, stdout
n, k = map(int, stdin.readline().split())
sizes = list(map(int, stdin.readline().split()))
constraints = list(map(int, stdin.readline().split()))

from collections import Counter
c = Counter(sizes)

revsizes = sorted(c.items(), key = lambda x: x[0], reverse= True)
tests = []

for size, freq in revsizes:
    temp = freq
    while temp!=0:
        if temp>constraints[size]:
            temp -= constraints[size]


        elif temp == constraints[size]:


# References:
# - https://stackoverflow.com/questions/37873954/what-are-pythons-equivalents-of-stdlower-bound-and-stdupper-bound-c-algor
# - https://www.youtube.com/watch?v=FXk5beUOGtE
# - https://www.youtube.com/watch?v=XeK6lYKd8W4
# https://codeforces.com/blog/entry/76633
# https://codeforces.com/contest/1342/problems