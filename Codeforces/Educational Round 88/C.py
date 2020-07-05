# If there are even number of cups, the attained temperature is always: (h+c)/2. If there are odd number of total cups (let it be 2*x - 1). There are x hot cups and (x-1) cold cups. The attained temperature is given by (h*x + c*(x-1))/2*x-1 = t_attained ---- EQN 1

# In the odd no. of cups case, the no. of hot cups is ALWAYS one more than no. of cold cups, so t_attained > (h+c)/2. 

# If t_desired < (h+c)/2 --> the answer is two cups.

# If t_desired > (h+c)/2 --> the answer consists of odd no. of cups. This can be obtained by solving EQN 1 for x by substituting t_attained by t_desired.

# x = (t_desired - c)/ (h + c - 2*t_desired). Solving this we get a fractional value for x.

# The answer will be 2*min(t_desired - t_attained_floor_x, t_desired - t_attained_ceil_x)-1.

# As x, gives us the number of h cups. The answer is total number of cups which is 2*x - 1

# Solve above equation for x (no. of hot cups) by replacing t_attained with t_desired.

## Failing on the test case:
# 1
# 999977 17 499998

# Output = 499979
# Answer = 499981


from sys import stdin, stdout
from decimal import Decimal # tried using decimal module to get more precision.

t = int(input())
for _ in range(t):
    h, c, t = map(int, stdin.readline().split())
  
    if (h+c) >= 2*t:
        print(2)
    else:
        x1 = (c-t)//(h+c- 2*t) # floor x
        x2 = x1 + 1 # ceil x

        # get both average temperature and check which is minimum
        t1 = Decimal((h*x1 + c*(x1 - 1))/((2*x1) - 1))
        t2 = Decimal((h*x2 + c*(x2 - 1))/((2*x2) - 1))

        # print(t1, t2, abs_avg_x1, abs_avg_x2)

        t = Decimal(t)
        abs_avg_x1 = Decimal(abs(t - t1))
        abs_avg_x2 = Decimal(abs(t - t2))

        if abs_avg_x1<=abs_avg_x2: 
            print(2*x1 - 1)
        else: 
            print(2*x2 - 1)




            
