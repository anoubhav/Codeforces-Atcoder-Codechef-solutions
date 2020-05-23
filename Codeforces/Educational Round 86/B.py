# 14 mins. No submission errors. Decent. Confidence in solution could be more, as implementation took 5-6 minutes. But proving that only two cases exist took some time (period 1 and period 2). Also, a simpler implementation existed. I can try thinking a bit more before solving.

from sys import stdin, stdout
t = int(input())
for _ in range(t):
    t = stdin.readline().strip()
    sm = sum([int(i) for i in t])
    if sm == 0 or sm == len(t):
        print(t)
        continue
    
    else: # From editorial
        s = ''
        for i in range(2*len(t)):
            s += ('0' if i%2 == 0 else '1')
        print(s)

    ## Used below code in competition. Both work. But, I made mine a bit more complicated by inserting a different character within repeated characters.

    # else: 
    #      
    #     s = ''
    #     prev = t[0]
    #     for char in t[1:]:
    #         if prev == char:
    #             s += (prev + ('1' if prev == '0' else '0'))
    #             prev = char

    #         else:
    #             s += prev
    #             prev = char


    #     s += char
    #     print(s)