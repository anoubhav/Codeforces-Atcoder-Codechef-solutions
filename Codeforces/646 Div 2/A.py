# 4 submission errors on pretest 2. Total score was 500. But due to 50 point penalty and time delay. I only got 250 points from this.
# I need to stop and think. Generate edge cases which are different from those given to us. 
# In this competition, I learnt that you CANNOT just accept your solution is correct if it passes the given tests.

# Also, think first, get an algorithm in your mind. And then implement. Once again my solution is a bunch of if/else (unnecessary cases were removed by me later). Whereas, the actual solution has none.

# 26 mins. Very slow. Its because I kept getting submission errors and did not think clearly what I was doing.

def my_soln():
    from sys import stdin, stdout
    t = int(input())
    for _ in range(t):
        n, x = map(int, stdin.readline().strip().split())
        nums = list(map(int, stdin.readline().strip().split()))

        oddcount = 0
        evencount = 0

        for num in nums:
            if num%2==1: oddcount +=1
            else: evencount += 1
        
        if oddcount == 0:
            print('NO')

        # atleast 1 odd number

        #  if no even numbers and x is also even (sum of even no. of odd no.s is even)
        elif evencount == 0 and x%2==0:
            print('NO')

        else:
            # I will only use maximum odd number of odd numbers.
            oddcount = oddcount - (0 if oddcount%2==1 else 1)

            # If the remaining can't be filled using even numbers, print NO
            if x - oddcount <= evencount:
                print('YES')
            else:
                print('NO')

def editorial():
    from sys import stdin, stdout
    t = int(input())
    for _ in range(t):
        n, x = map(int, stdin.readline().strip().split())
        nums = list(map(int, stdin.readline().strip().split()))

        evencount, oddcount = 0, 0
        for num in nums:
            if num%2==0: evencount += 1
            else: oddcount += 1
        
        # The no. of odd odd numbers being picked.
        ans = 'NO'
        for i in range(1, min(oddcount, x) + 1, 2):
            if x - i <=evencount:
                ans = 'YES'
                break
        print(ans)
        
editorial()