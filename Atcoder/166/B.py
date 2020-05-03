n, k = map(int, input().split())
 
all_set = set(range(1, n+1))
food_set = set()

for _ in range(k):
    t = input()
    lst = list(map(int, input().split()))
    
    for num in lst:
        food_set.add(num)
        
print(len(all_set - food_set))