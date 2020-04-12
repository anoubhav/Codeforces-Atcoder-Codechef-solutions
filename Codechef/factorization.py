# get the factorization of a number
def get_factorization(n):
    # List of tuples (a, b) where a is the prime number and b is the multiplicity
    prime_factors = []
    div = 2
    count = 0
    while int(n)!=1:
        if n%div == 0:
            count += 1
            n = n/div
        else:
            if count:
                prime_factors.append((div, count))
                count = 0
            if div>2:
                div+= 2
            else:
                div+= 1

    if count:
        prime_factors.append((div, count))
        
    return prime_factors

if __name__ == '__main__':
    n = int(input())
    print(get_factorization(n))