from fractions import Fraction
a, b = map(Fraction, input().split())
print(int(a*b))


# This works
a, b = input().split()
a = int(a)
bint, bdec = map(int, b.split('.'))

b = 100*bint + bdec
print((a*b)//100)


## both fail because converion to float leads to precision errors.
# a, b = map(float, input().split())
# print(floor(a, b))
# print(int(a, b))