# Better approach:
# https://www.youtube.com/watch?v=e2HE538GyrI

# I wasted 30 minutes implementing the O(N^2) naive solution below. He looked at constraints and determined
# directly that TLE would occur. Here N <= 2*10^5. For checking N(N-1)/2 pairs it would take 10^10 operations. 
# The time limit for each problem in Atcoder is 2 seconds. Thus your laptop clock speed should be atleast 5 Ghz
# to complete this in time. Which is too high. So naive will definitely give TLE.

# The absolute difference of their attendee numbers is equal to the sum of their heights. Formula -> Hi + Hj = |i-j| . This expands too.
# Hi + Hj = i - j and Hi + Hj = j - i
# Hi - i = - (Hj + j) and Hi + i = j - Hj ; We have to count 4 quantities lhs & rhs of two equations
n = int(input())
hlist = list(map(int, input().split()))

# Hi - i = - (Hj + j) and Hi + i = j - Hj
cnt_height_minus_ind = {}
cnt_minus_height_minus_ind = {}
cnt_height_plus_ind = {}
cnt_ind_minus_height = {}

# 0/1 Indexing does not matter as we are looking at difference. 
for ind in range(n):
    height = hlist[ind]
    if ind - height not in cnt_ind_minus_height:
        cnt_ind_minus_height[ind - height] = 0
    cnt_ind_minus_height[ind - height] += 1

    if ind + height not in cnt_height_plus_ind:
        cnt_height_plus_ind[ind + height] = 0
    cnt_height_plus_ind[ind + height] += 1

    if height-ind not in cnt_height_minus_ind:
        cnt_height_minus_ind[height-ind] = 0
    cnt_height_minus_ind[height-ind] += 1

    if -ind - height not in cnt_minus_height_minus_ind:
        cnt_minus_height_minus_ind[-height-ind] = 0
    cnt_minus_height_minus_ind[-height-ind] += 1

ans = 0
# Hi - i = - (Hj + j)
for val in cnt_height_minus_ind:
    if val in cnt_minus_height_minus_ind:
        ans += cnt_height_minus_ind[val]*cnt_minus_height_minus_ind[val]

# Hi + i = j - Hj
for val in cnt_height_plus_ind:
    if val in cnt_ind_minus_height:
        ans += cnt_height_plus_ind[val]*cnt_ind_minus_height[val]

# as we double count the pair
print(ans//2)

## My approach: TLE

# n = int(input())
# hlist = list(map(int, input().split()))
# alist = list(range(1, n+1))

# shlist = []
# for height in hlist:
#     if height < n - 1:
#         shlist.append(height)

# ans = 0
# # The absolute difference of their attendee numbers is equal to the sum of their heights.
# for i, h1 in enumerate(shlist):
#     for j, h2 in enumerate(shlist[i+1:]):
#         if h1+h2>n:
#             continue
#         if j+1 == h1+h2:
#             ans += 1
# print(ans)