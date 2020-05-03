n = int(input())
totsum = 0
for num in range(1, n+1):
  if num%3!=0 and num%5!=0:
    totsum+=num
    
print(totsum)