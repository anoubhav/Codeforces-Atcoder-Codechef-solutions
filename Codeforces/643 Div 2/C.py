# It is given that (1≤A≤B≤C≤D≤5⋅10^5). If we search for x, y, z in those ranges the solution will be greater than O(n).
# With 10^5 constraints the solution needs to be below quadratic runtime.

# Ref: https://www.youtube.com/watch?v=3L61ujaaLzM  -  Using Prefix sums we calculate all the number of all possible x+y in linear time
# and not quadratic. For a triangle, x+y>z. We check this condition in liner time as well separately.

# no. of all possible x+y using prefix sums.
a, b, c, d = map(int, input().split())
prefsum = [0]*(b+c+2)

# O(linear)
for i in range(a, b+1):
    # all (x, y) sums between (i+b, i+c) are possible
    prefsum[i + b] += 1
    prefsum[i+c+1] += -1

# Get the prefix sum
for i in range(1, len(prefsum)):
    prefsum[i] += prefsum[i-1]

# print(prefsum)
# Get the cummulative sum. # of (x, y) where x+y <= i
for i in range(1, len(prefsum)):
    prefsum[i] += prefsum[i-1]

# print(prefsum)
# O(linear)
ans = 0
for z in range(c, d+1):
    # no. of z's for which z<(x+y)
    if z < (b+c+2):
        ans += (prefsum[-1]-prefsum[z])
    else: break
print(ans)




def my_tle_soln():
    a, b, c, d = map(int, input().split())


    ans = 0
    xmin, xmax = a, b
    ymin, ymax = b, c

    for z in range(c, d + 1):

        if xmin + ymin > z:
            ans += (xmax - xmin + 1)*(ymax - ymin + 1)
            continue
        
        elif xmax + ymax <= z:
            break

        else:
            # minimum x possible
            leastx = max(xmin, z - ymax - 1)

            # minimum y possible
            leasty = max(ymin, z - xmax - 1)

            ## Incorrect (wrong answer on test 4) approach 2
            # ans += (min(xmax - leastx + 1, ymax - ymin + 1))
            # ans += (min(ymax - leasty + 1, xmax - xmin + 1))
            # ans -= (min(xmax - leastx + 1, ymax - leasty + 1))

            ## TLE approach 1.
            # for x in range(leastx, xmax+1):
            #     for y in range(ymax, leasty-1, -1):
            #         if x + y <=z:
            #             break
            #         else:
            #             ans += 1

    print(ans)





    