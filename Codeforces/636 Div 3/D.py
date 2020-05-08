# # Unsolved in contest 

## Accepted solution: O(n+k) solution
# https://www.youtube.com/watch?v=QouZfBC9CVw&list=RDCMUC4lyxGubhu5u1s1LYCwXtZw&index=2

def prefix_algo():
    t = int(input())
    from collections import defaultdict
    import math
    for _ in range(t):
        n, k = list(map(int, input().split()))
        seq = list(map(int, input().split()))

        prefix_arr = [0]*(2*k+10)
        zero_count = defaultdict(int)
        for i in range(n//2):
            zero_count[seq[i] + seq[n-i-1]] += 1

            a, b = sorted((seq[i], seq[n-i-1]))

            L = a + 1
            R = b + k

            prefix_arr[L] += 1
            prefix_arr[R+1] -= 1
            
        prefsum = 0
        for i in range(2*k + 10):
            prefsum +=  prefix_arr[i]
            prefix_arr[i] = prefsum
        
        ans = n
        for i in range(2, 2*k + 1):
            zero = zero_count[i]
            ones = prefix_arr[i] - zero
            twos = n//2 - ones - zero

            total = ones + twos*2
            ans = min(ans, total)
            
        print(ans)

prefix_algo()


## Naive solution: O(n*k) - TLE
def Naive():
    t = int(input())
    import math
    for _ in range(t):
        n, k = list(map(int, input().split()))
        seq = list(map(int, input().split()))

        ans = 10**6
        for tot in range(2, 2*k + 1):
            counter = 0
            for i in range(n//2):
                a, b = seq[i], seq[n - i - 1]

                if a+b>tot:
                    minchange = max(a-1, b-1)
                    if a+b - minchange > tot:
                        counter += 2
                    else: counter += 1
                
                elif a + b < tot:
                    maxchange = max(k - a, k - b)
                    if a+b+maxchange < tot:
                        counter +=2
                    else: counter += 1
            
            if counter < ans:
                ans = counter
        print(ans)
            

    ### Main mistake was that I diregarded the individual numbers (a, b) and only took the sum. The number5
    ## Failed approach 1
    # ans = 10**6
    # pair_sum = list()
    # for i in range(n//2):
    #     pair_sum.append(seq[i] + seq[n - i - 1])
        
    # for master in pair_sum:
    #     counter = 0
    #     for pair in pair_sum:
    #         if pair!=master:
    #             if abs(pair - master) >= k:
    #                 counter += 2
    #             else:
    #                 counter += 1
    #     if counter<ans:
    #         ans = counter

    # master = k
    # counter = 0
    # for pair in pair_sum:
    #     if pair!=master:
    #         if abs(pair - master) >= k:
    #             counter += 2
    #         else:
    #             counter += 1
    # if counter<ans:
    #     ans = counter
    # print(ans)


    ## Failed approach 2
    # pair_sum = dict()
    # mode_count = 0

    # for i in range(n//2):
    #     temp = seq[i] + seq[n - i - 1]
        
    #     if temp in pair_sum: pair_sum[temp] += 1
    #     else: pair_sum[temp] = 1

    #     if pair_sum[temp]>mode_count:
    #         mode_count = pair_sum[temp]

    # ans = 10**6
    # for key, v in pair_sum.items():
    #     if v == mode_count:
    #         mode_sum = key
    #         counter = 0
    #         for i in range(n//2):
    #             temp = seq[i] + seq[n - i - 1]
    #             if temp!=mode_sum:
    #                 if abs(temp - mode_sum) >= k:
    #                     counter += 2
    #                 else:
    #                     counter += 1
    #                 # print(mode_sum, temp, counter)
                    
    #         if counter<ans:
    #             ans = counter

    # if k//2 not in pair_sum:
    #     mode_sum = k//2
    #     counter = 0
    #     for i in range(n//2):
    #         temp = seq[i] + seq[n - i - 1]
    #         if temp!=mode_sum:
    #             if abs(temp - mode_sum) >= k:
    #                 counter += 2
    #             else:
    #                 counter += 1
    #             # print(mode_sum, temp, counter)
                
    #     if counter<ans:
    #         ans = counter
    
    # ans = min(n//2, ans)
    # print(ans)

