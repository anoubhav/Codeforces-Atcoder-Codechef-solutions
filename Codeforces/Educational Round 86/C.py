from sys import stdin, stdout
from math import ceil
# Overall Intuition: Basically all the numbers which fall in the range of [k*lcm, k*lcm + max(a,b)) (k is any integer) have equal moduli. If l or r falls in the middle of such a range, the numbers either have to be included or excluded which is handled in these two statements.

# I arrived at this by printing values of the statement for x:1 to 100. So that was smart of me. I got the algorithm but the number theory tripped me.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(input())
for _ in range(t):
    a, b, q = map(int, stdin.readline().split())

    if max(a, b)%min(a, b) == 0:
        for _ in range(q):
            l, r = map(int, stdin.readline().split())
            print(0)

    else:
        lcm = (a*b)//gcd(a, b)
        m = max(a, b)
        how = lcm - m
        ans = []
        for _ in range(q):
            l, r = map(int, stdin.readline().split())

            # From solution page. if b>=a, the statement is NOT satisfied for every LCM-b quantities. We have to find out how many LCM-b quantities exist in [l, r]. Find the quantity in [0, l-1]. Find it in [0, r]. Subtract the two to get [l, r]. https://codeforces.com/contest/1342/submission/78171364
            
            # for [0, l-1]
            x1 = ((l-1)//lcm)*how
            final1 = (l-1)%lcm
            x1 += max(0, final1 - m + 1)

            # repeat above steps for [0, r]
            x2 = ((r)//lcm)*how
            final2 = (r)%lcm
            x2 += max(0, final2 - m + 1)

            ans.append(x2-x1)
        print(*ans)

        # Intuition: if a≤b, and lcm(a,b) is L. Then from **b to L-1** every number satisfies. Therefore we don't even need to check which numbers are good between 0 and L-1 individually and it will always be (L-b). Then just answer each query in O(1) time.


            ### I couldn't find the number of occurences of [LCM, LCM + max(a, b)] in [l, r]. I figured out the algorithm in 20 mins. But, I spent **1 hr 10 mins** on trying to implement the above line, i.e., # of occurrences. Pathetic.
            # ans = 0
            # totnum = r - l + 1

            # if r<m:
            #     print(0)
            #     continue

            # elif (l//(lcm)) != (l//(lcm + m)):
            #     ans += (lcm*(l//lcm) + m - l + 1)
            #     start = lcm*(1 + l//lcm)
            # else:
            #     start = lcm*(1 + l//lcm)

            # if start>r:
            #     print(ans)
            #     continue
            # while True:
            #     if start + m <= r:
            #         ans += m
            #         start += lcm
            #     else:
            #         if start > r:
            #             pass
            #         else:
            #             ans += (r - start + 1)
            #         break                
            # print(totnum - ans)


    # for x in range(100):
    #     if (x%a)%b == (x%b)%a:
    #         print(x, (x%a)%b, (x%b)%a)

    # lr = []
    # for _ in range(q):
    #     lr.append(tuple(map(int, stdin.readline().split())))

    # print(lr)
        