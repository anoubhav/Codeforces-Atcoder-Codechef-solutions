from itertools import product
def gcd(a, b, c):
    z = min(a, b, c)
    for i in range(z, 0, -1):
        if a%i==0 and b%i==0 and c%i==0:
            return i

k = int(input())

d = {}

totsum = 0
for i in range(1, k+1):
    for j in range(i, k+1):
        for k in range(j, k+1):
            if i ==j ==k:
                totsum += i
                continue

            elif i==j or i==k or j==k: factor = 3
            else: factor = 6

            if i ==1 or j==1 or k==1: 
                totsum += 1*factor
                continue

            totsum += gcd(i, j, k)*factor

# for config in list(product(range(1, k+1), range(1, k+1), range(1, k+1))):
#     a, b, c = config
#     if a==1 or b==1 or c==1: 
#         totsum+=1
#     elif a==b==c:
#         totsum+=a

#     else:
#         try :
#             ans = d[tuple(sorted((a, b, c)))]
#         except: 
#             ans = gcd(a, b, c)
#             d[tuple(sorted((a, b, c)))] = ans

#         totsum += ans
# print(d)
print(totsum)


