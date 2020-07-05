from sys import stdin
from math import sqrt, floor

def seive(n):
    is_prime = [1]*(n + 1)
    is_prime[0], is_prime[1] = 0, 0

    for num in range(2, n+1):
        if num*num>n:
            break

        if is_prime[num] == 0:
            continue

        for mult in range(2*num, n+1, num):
            is_prime[mult] = 0

    return is_prime

def primeFactors(n): 
    ans = []
    # Print the number of two's that divide n 
    exp = 0
    while n % 2 == 0: 
        exp += 1
        n = n / 2
    if exp > 0: 
        ans.append(2**exp)
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        exp = 0
        while n % i== 0: 
            exp += 1
            n = n / i
        if exp > 0:
            ans.append(i**exp) 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        ans.append(int(n))

    return ans 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
nums = list(map(int, stdin.readline().split()))

isprime = seive(5*(10**5))

d2 = []

for num in nums:
    # prime
    if isprime[num]:
        print(-1, end = " ")
        d2.append(-1)
        continue

    # not a prime; but single prime factor
    divs = primeFactors(num)
    if len(divs) == 1:
        print(-1, end = " ")
        d2.append(-1)
        continue

    # not a prime and more than 1 prime factor
    flag = 1
    for div in divs: 
        if gcd(div, num//div) == 1:
            print(div, end = " ")
            d2.append(num//div)
            flag = 0
            break
    if flag:
        print(-1, end = " ")
        d2.append(-1)
        
print()
print(*d2)
