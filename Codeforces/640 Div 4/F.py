# Unsolved: Wasted 1hr 30 mins on this. I should have focused on finishing G and then done this as well.
# I had potential of solving 6/7 :>( . I solved 4 in total. That too in the first 38 mins.

# https://codeforces.com/contest/1352/problems

# I couldn't figure out that there were only 2 cases: n1 == 0 and n1!=0. I made it very convoluted by 
# using many many nested cases.

t = int(input())
for _ in range(t):
    n0, n1, n2 = map(int, input().split())

    # As solution always exists and n1 = 0, only one of n0 and n2 can be nonzero. If both are nonzero, 
    # then when we transition from 0s to 1s or vice-versa, n1 will increase by atleast 1.
    if n1 == 0:
        if n0: print('0'*(n0+1))
        elif n2: print('1'*(n2+1))
    
    else:
        # n1!=0

        # first construct alternating string of 1010101s upto length n1+1, this satisfies all substrings of length 1.
        string = ''.join([str((i+1)%2) for i in range(n1+1)]) 

        # append on the left n2 1s, this satisfies all substrings of length 2 (without disturbing n1)
        string = '1'*n2 + string[0] + '0'*n0 + string[1:]

        # after all 1s add n0 zeros, this all substrings of length 0 (without disturing total n1 #of 1 length substrings)

        print(string)


# Explanation:
# Consider case n1=0 separately and print the sting of n0+1 zeros or n2+1 ones correspondingly.

# Now our string has at least one pair "10" or "01". Let's form the pattern "101010 ... 10" of length n1+1. So, all substrings with the sum 1 are satisfied. Now let's insert n0 zeros before the first zero, in this way we satisfy the substrings with the sum 0. And then just insert n2 ones before the first one, in this way we satisfy the substrings with the sum 2.


def my_incorrect_soln():
    t = int(input())
    for _ in range(t):
        n0, n1, n2 = map(int, input().split())

        string = ''
        
        if n0 == 0 and n1 == 0:
            print('1'*(n2 + 1))
            continue
        elif n0 == 0 and n2 == 0:
            string = ''
            for i in range(n1 + 1):
                if i%2 == 0:
                    string += '1'
                else:
                    string += '0'
            print(string)
            continue
        elif n1 == 0 and n2 == 0:
            print('0'*(n0 + 1))
            continue
        elif n2 == 0:
            if n1%2 == 1:
                string += '10'*((n1+2)//2)
                string += '0'*(n0)
                print(string)
                continue
            else:
                string = ''
                for i in range(n1 + 1):
                    if i%2 == 0:
                        string += '0'
                    else:
                        string += '1'
                
                new = '0'*(n0) + string
                print(new)
                continue


        string = ''
        if n1%2==1:
            string += '1'*(n2)
            string += '10'*((n1+1)//2)
            string += '0'*(n0)
        else:
            string += '1'*(n2 - 1)
            temp = '10'*((n1+2)//2)
            string += (temp[:-1] + '1')
            if n0>0: string += '0'*(n0 + 1)


        print(string)
        # sorted_nums = sorted([(k, v) for k, v in d.items()], key = lambda x: x[1])

        # string = ''

        # k1, v1 = sorted_nums[0]   # lowest
        # k2, v2 = sorted_nums[1]   # second_lowest

        # while v1>0:
        #     if k1 == 0 and k2 == 1:
        #         string +=  
            

        #     v1 -= 1





