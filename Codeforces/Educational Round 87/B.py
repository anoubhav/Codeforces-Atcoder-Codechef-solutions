# 24 mins. 
# 
# I spent 6 mins extra + 2 wrong submissions on a silly mistake. I initalized my minimum length as the maximum
# possible array size. And not more than that. Test case 27 was an array where the answer was the maximum array size. 
# And i put the condition that if answer is unchanged from intialization sett to 0. 

# This cost me heavily. Don't be stingy with your initializations and careful with wrong submissions.

from sys import stdin, stdout
t = int(input())
for _ in range(t):
    s = stdin.readline().strip()

    d = {'1':0, '2':0, '3':0}

    start = end = 0
    minlen = 2*(10**6)
    
    while end<len(s):
        if minlen == 3:
            break

        if all(d.values()):
            while all(d.values()):
                d[s[start]] -= 1
                start = start + 1
                minlen = min(minlen, end - start + 1)
                

        else:
            if end<len(s): 
                d[s[end]] += 1
            end += 1
    
    # if the last number in the list satisfies the condition (repeat the same steps by incrementing start pointer till the condition is satisfied)
    if all(d.values()):
        while all(d.values()):
            d[s[start]] -= 1
            start = start + 1
            minlen = min(minlen, end - start + 1)
    
    print(0 if minlen == 2*(10**6) else minlen)


