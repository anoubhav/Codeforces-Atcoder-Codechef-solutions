from sys import stdin, stdout
from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    s = stdin.readline().strip()
    # s = a + a + b + b
    freq = defaultdict(int)

    # check if all characters are even, if not, print(0)
    stop = 0
    for k, v in Counter(s).items():
        if v%2==1:
            print(0)
            stop = 1
            break
    if stop: continue

    n = len(s)
    # all characters have even counts (for entire string)
    ans = 0
    for i in range(n-1):
        freq[s[i]] += 1

        # In even length substring, save the freq state IFF all frequencies are even. 
        if i%2==1:
            flag = 1
            # check if palindromic
            if s[:(i+1)//2] == s[(i+1)//2:i+1]:
                if s[i+1: i+1 + (n-i-1)//2] == s[i+1 + (n-i-1)//2:]:
                    ans += 1
            
            # # check if even frequency
            # for k, v in freq.items():
            #     if v%2!=0:
            #         flag = 0
            #         break
            # if flag:
            #     ans += 1
    print(ans)
                





    