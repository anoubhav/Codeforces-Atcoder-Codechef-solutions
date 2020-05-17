# 7 mins
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
 
    alist = sorted(alist)
    blist = sorted(blist, reverse = True)
 
    tot = sum(alist[k:]) 
 
    for i in range(k):
        if alist[i] < blist[i]:
            tot += blist[i]
        else:
            tot += alist[i]
 
    print(tot)