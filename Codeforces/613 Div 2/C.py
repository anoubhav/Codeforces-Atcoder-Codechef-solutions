# 45 mins. Slow. but no submission errors. Also, checked google for dividing list into all possible combinations of two lists. And also for the insight of generating pairs (a, b) given LCM X. 
# 
# Pros: The algorithm I had in mind (even though I didn't know how to implement parts of it) was correct.

from sys import stdin, stdout
import math 

# Intuition: let's prime factorize X. Since there will be at most 11 distinct primes, we can distribute them between a and b with a bruteforce. Why 11? If we multiple the 11 smallest primes we get ~2x10^12, which is just higher than the X upper limit in question.

# There will always be a solution where a and b are coprime. To see why, let's prime factorize a and b. If they share a prime factor we can omit all its occurrences from one of them, precisely from the one that has fewer occurrences of that prime, without affecting their LCM.

# e.g. LCM = 24. Prime factorization is 2^3, 3. The primeFactors function will return [8, 3]. We have to divide this list of numbers into two lists. Such that the product of numbers in both lists are as close to each other as possible. As we want min max(a, b). So if a or b is small. The other will be very large as LCM is fixed. So we want a and b to be close to each other. In this case (8, 3) is the only possibility of (a, b)

# eg. LCM = 140. Prime factorization is 2^2, 5, 7. The primeFactors function will return [4, 5, 7]. Now (a, b) can be (4*5, 7), (4, 5*7), (4*7, 5). In this case (20, 7) gives the minimum (a, b) of 20.


X = int(input())
  
def primeFactors(n): 
    ans = []
    # Print the number of two's that divide n 
    temp = 1
    while n % 2 == 0: 
        temp*=2
        n = n / 2
    if temp!=1: ans.append(int(temp))

    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        temp = 1
        while n % i== 0: 
            temp *= i
            n = n / i 

        if temp!=1:
            ans.append(int(temp))

    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        ans.append(int(n))
    return ans

pfactors = primeFactors(X)

from itertools import *
from operator import mul
from functools import reduce

diff = 10**12 # we want to minimize the difference between a and b. 
mina, minb = None, None

# All possibilies of splitting a list into two lists. And obtaining their respective product. These are the (a, b)
for pattern in product([True,False],repeat=len(pfactors)):
    a = reduce(mul, [x[1] for x in zip(pattern,pfactors) if x[0]], 1)
    b = reduce(mul, [x[1] for x in zip(pattern,pfactors) if not x[0]], 1)

    if abs(a-b) < diff:
        diff = abs(a-b)
        mina, minb = a, b

print(mina, minb)

## Nice resources for understanding why I am finding the prime factorization of X to get the coprime factors.
# https://www.youtube.com/watch?v=4yV4UudMcvc
# https://math.stackexchange.com/questions/4152/pairs-of-numbers-with-a-given-lcm
# https://math.stackexchange.com/questions/62417/a-fast-way-to-compute-number-of-pairs-of-positive-integers-a-b-with-lcm?noredirect=1&lq=1

## Coding implementation copied from these two sources during contest. 
# Learnt some awesome commands like product from itertools, reduce from functools.

# https://stackoverflow.com/questions/40709488/all-possibilities-to-split-a-list-into-two-lists
# https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list

