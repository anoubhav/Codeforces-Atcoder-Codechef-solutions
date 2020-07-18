n = int(input())
print((1000 - n%1000)%1000)



# O(N) solution; in contest
# n = int(input())
# for i in range(0, 20000 , 1000):
#     if i >= n:
#         break
# print(i - n)