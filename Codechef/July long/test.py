from collections import defaultdict as dd
t = int(input())
for _ in range(t):
    n = int(input())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))

    freq_diff = dd(int)

    for i in alist:
        freq_diff[i] += 1
    for i in blist:
        freq_diff[i] -= 1
    
    exitflag = False

    for k in freq_diff.keys():
        if freq_diff[k]%2:
            exitflag = True
            break
    
    if exitflag:
        print(-1)
        continue
    
    pos, neg = [], []
    for pair in freq_diff.items():
        if pair[1] > 0:
            pos.append(pair)
        elif pair[1] < 0:
            neg.append((pair[0], -pair[1]))

    pos.sort(key=lambda x: x[0])
    neg.sort(key=lambda x: x[0])


    pos_start = 0
    cost = 0
    while neg:
        print(pos, neg, cost, pos_start)
        mxneg, freqneg = neg[-1]
        mipos, freqpos = pos[pos_start]

        if freqneg == freqpos:
            numswaps = freqneg
            pos_start += 1
            neg.pop()
            cost += min(mxneg, mipos)*numswaps
        
        elif freqneg < freqpos:
            numswaps = (freqpos - freqneg)
            pos[pos_start] = (mipos, freqpos - numswaps)
            neg.pop()
            cost += min(mxneg, mipos)*numswaps
        
        else: # freqneg > freqpos
            numswaps = (freqneg - freqpos)
            pos_start += 1
            cost += min(mxneg, mipos)*numswaps
            neg[-1] = (mxneg, freqneg - numswaps)
    
    print(cost)