# https://codeforces.com/contest/1335/problems
# Solved
from collections import Counter

def my_solution(n, a):
    d = Counter(a)
    if n<2:
        print(0)
        return
    maxx = n//2
    # The most frequent skills in set 2.
    modekey, mode = d.most_common()[0]
    maxx = mode
 
    # d.keys() ensures that repeated elements are only present once in this list. Rem also contains modekey.
    rem = list(d.keys())
    
    # more distinct skills than same skills
    if len(rem)>=maxx+1:
        print(maxx)

    # If distinct skills is one less than same skills. Rem also contains one instance of modekey.
    elif len(rem) == maxx:
        print(len(rem) - 1)
        
    # If distinct skills is less than same skills discounting one common modekey.
    elif len(rem) <= maxx - 1:
        print(len(rem))

def editorial_solution(n, a):
    # https://codeforces.com/blog/entry/75993
    d = Counter(a)
    diff = len(list(d.keys()))
    modekey, mode = d.most_common()[0]

    print(max(min(mode, diff-1), min(mode-1, diff)))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # my_solution(n, a)
    editorial_solution(n, a)
    
