# Reference: https://www.youtube.com/watch?v=m_N4B436LCo

# Intuition: unique possible k-periodic strings are of the form i, i+k, i+2k, i+3k,... for i in [0, k-1]
# For each configuration(out of k ; as there are k starting points),
# we have to see how many operations are required to make it k-periodic.
# totsum = # of 1s in string. NumOperations(in one config) = totsum - 1s in config + 0s in config
# NumOperations(in one config) = totsum - (1s in config - 0s in config)
# Answer = Min(NumOperations(in all config)) = totsum - Max((1s in config - 0s in config))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    totsum = len(s.replace('0', ''))
    ans = totsum

    # O(n) : each element in s is only visited once
    for i in range(0, k):
        prefsum = 0
        for j in range(i, n, k):
            prefsum += (1 if s[j] == '1' else -1)  # add 1 if '1' , subtract -1 if '0'
            prefsum = max(prefsum, 0)
            ans = min(ans, totsum - prefsum) 
    print(ans)

         

# Incorrect solution, which worked on test cases 1(given by organizer) but not 2.
# Tried to hard code a solution using multiple cases. 
def my_failed_soln():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()

        # scan through .. find the longest current k-periodic sequence. delete tot ones by that
        only1 = dict()
        maxlen = 0
        for i, lamp in enumerate(s):
            if lamp == '1':
                if i-k in only1:
                    only1[i] = only1[i-k] + 1
                    if only1[i]>maxlen:
                        maxlen = only1[i]
                else:
                    only1[i] = 1
                    if only1[i]>maxlen:
                        maxlen = only1[i]    
        
        ans = 0
        temp = list(only1.items())

        # print(only1.items())

        for key,v in temp:
            if key+k in only1 or v!=1:
                if only1[key] == 1:
                    del only1[key]
                pass
            else:
                del only1[key]
                ans += 1

        totones = sum(only1.values())
        temp = list(only1.items())
        for i in range(len(temp)-1):
            pk, pv = temp[i]
            nk, nv = temp[i+1]

            if (nk-pk)%k!=0:
                # chuck previous
                prev = ans + pv
                # chuck future
                fut = totones - pv

                if fut<=prev:
                    ans = ans + fut
                    break
                else:
                    ans = prev
            
            else:
                add1s = (nk-pk)//k 
                prev = ans + pv
                fut = totones - pv

                if add1s<prev and add1s<fut:
                    ans += add1s
                    break
                if fut<=prev:
                    ans = ans + fut
                    break
                else:
                    ans = prev


        print(ans)


