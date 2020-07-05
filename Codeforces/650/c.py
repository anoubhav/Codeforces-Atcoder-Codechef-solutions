from sys import stdin

t = int(input())
for _ in range(t):

    n, k = map(int, input().split())
    s = input()

    ## Prefix sum calculation for number of ones
    ## prefones[i]: number of ones from nums[:i+1] (including i)
    prefones = [0]*n
    for ind, i in enumerate(s):
        if i == '1':
            prefones[ind] = 1
    for i in range(1, n):
        prefones[i] += prefones[i- 1]
    
    # index
    i = 0
    # answer
    ans = 0
    while i<n:
        # if current is 0. 
        if s[i] == '0':
            # Then check if there is any '1' in the next k elements. If not, make this 1. And skip ahead by (k + 1)
            if (prefones[min(n-1, i + k)] - prefones[i]) == 0:
                ans += 1
                i += (k + 1)

            # If 1 is there in the next k elements, you want to move till reaching that '1'
            else:
                i+=1

        # if current is 1. skip ahead by k + 1
        else:
            i += (k+1)
        

    print(ans)


