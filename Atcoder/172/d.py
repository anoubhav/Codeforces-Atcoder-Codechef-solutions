n = int(input())

# Check out atcoder editorial for this, beautifully explained. Same as geothermal's but it also shows how this idea was thought
# https://img.atcoder.jp/abc172/editorial.pdf 
def sieve(n):
    # 1.9 seconds.

    # 1 and n are divisors for every n.
    is_prime = [2]*(n + 1)
    is_prime[0], is_prime[1] = 0, 0

    # is_prime holds the number of positive divisors of N. Instead of being a bool of 0/1 for prime/not prime. for example of N=24--->  is_prime[24] = 6 (1, 2, 3, 4, 6 ,24)

    for num in range(2, n+1//2):
        for mult in range(2*num, n+1, num):
            is_prime[mult] += 1
        
    ans = 1

    # i is N. elem is f(N)
    for i, elem in enumerate(is_prime[2:]):
        ans += (elem)*(i + 2)

    print(ans)

def geothermal(n):
    # Source: https://codeforces.com/blog/entry/79438
    # Let's reframe the problem by considering the total contribution each divisor makes to the answer. For any given i, i contributes K to the sum for each K from 1 to N such that K is a multiple of i.
    ans = 0
    for i in range(1, n+1):
        mult = n//i
        ans += (mult*(mult + 1)*i)//2
    print(ans)

# O(N) solution; 170ms
geothermal(n)

# O(N* some log factors) much slower than geo's; 1940ms
sieve(n)




