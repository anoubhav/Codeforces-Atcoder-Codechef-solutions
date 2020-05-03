


### Better approach
# https://www.youtube.com/watch?v=FPYUkSe2c_o

# x >= (a+1)**5 - a**5 
# x >= 5a^4 + 10a^3 + 10a^2 + 5a + 1
# x >= 5a^4
# |a| <= (x/5)^0.25

# As x <= 10**9, calculate |a| <= (10**9/5)^0.25 ~ 118. 
# Instead of using two breaks, exit() can be used. This below code works.

x = int(input())
for a in range(-120, 120):
  for b in range(-120, 120):
    if a**5-b**5 == x:
      print(a, b)
      exit()


### My approach which worked in contest ###
# Assumed that the root a and b lie near the 5th root of X; Don't know how useful this is.
root = int(x**(0.2))

# I tried to use the fact that a^5 - b^5 = (a-b)*(a^4 + a^3b + ab^3 + a^2b^2 + b^4) = x
# Thus (a-b) divides x

flag = 0 # to break from upper for loop

# Ranges obtained using trial and error on test cases (gradually increased)
for i in range(root - 400, root + 400):
    for j in range(-100, root + 400):
        if i!=j: # to avoid ZeroDivisionError
            if x%(i-j) == 0:
                if i**5-j**5 == x:
                    print(i, j)
                    flag = 1
                    break
    if flag:
        break