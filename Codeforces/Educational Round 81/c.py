from sys import stdin
# from collections import defaultdict
orda = ord('a')
q = int(input())
for _ in range(q):
    s = stdin.readline().strip()
    t = stdin.readline().strip()
    
    # char_inds = defaultdict(list)
    # for i, elem in enumerate(s):
    #     char_inds[elem].append(i)
    
    char_inds  = [[] for _ in range(30)]
    for i in range(len(s)):
        char_inds[ord(s[i]) - orda].append(i)
    
    i = 0
    n = len(t)
    numops = 0
    exitflag = False
    while i<n:
        if char_inds[(ord(t[i]) - orda)] == []:
            exitflag = True
            break

        start = char_inds[ord(t[i]) - orda][0] # first index occurence of t[i]

        ans = 0
        for j in range(i+1, n):
            if char_inds[(ord(t[j]) - orda)] == []:
                exitflag = True
                break

            lst = char_inds[ord(t[j]) - orda]
            # find the smallest index greater than start
            ans = -1
            lo, hi = 0, len(lst)-1
            while lo<=hi:
                mid = lo + (hi-lo)//2
                if lst[mid] > start:
                    ans = lst[mid]
                    hi = mid - 1
                else:
                    lo = mid + 1

            if ans == -1:
                break
            else:
                start = ans

        if exitflag:
            break
        
        i = j + (1 if ans!=-1 else 0)
        numops += 1
    
    if exitflag:
        print(-1)
    else:
        print(numops)



