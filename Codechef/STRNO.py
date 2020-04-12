import math

def get_factorization(n, k):
    # List of tuples (a, b) where a is the prime number and b is the multiplicity
    prime_factors_count = 0
    div = 2
    count = 0
    while int(n)!=1:
        if n%div == 0:
            count += 1
            n = n/div
        else:
            if count:
                prime_factors_count +=count
                count = 0
            
            if prime_factors_count>=k:
                return 1
            if div>2:
                div+= 2
            else:
                div+= 1

    prime_factors_count +=count
        
    return int(prime_factors_count>=k)


def primeFactors(n, k): 
    prime_factors_count = 0
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        prime_factors_count += 1 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            prime_factors_count += 1 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        prime_factors_count += 1 
    
    return int(prime_factors_count>=k)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x, k = list(map(int, input().split()))

        ## for some reason the below function gives TLE(TIME LIMIT ERROR) work but primeFactor works.
        # print(get_factorization(x, k))
        print(primeFactors(x, k))


