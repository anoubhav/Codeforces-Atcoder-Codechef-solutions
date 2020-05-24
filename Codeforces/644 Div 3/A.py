t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    # a<b
    if a>b: a, b = b, a

    if 2*a > b:
        # square of side 2a is required
        print((2*a)**2)
    
    else:
        # if b is larger than twice a
        print(b**2)
    