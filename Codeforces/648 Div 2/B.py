# def bubbleSort(n, arr, blist): 
#     tags = list(range(n))
#     tagtype = dict()
#     for ind, elem in enumerate(tags):
#         tagtype[elem] = blist[ind]


#     for i in range(n-1): 
#         for j in range(0, n-i-1): 
#             if arr[j] > arr[j+1]: 
#                 if tagtype[tags[j]]==tagtype[tags[j+1]]:
#                     flag = 0
#                     for k in range(j+2, n-i-1):
#                         if arr[j] > arr[k] and tagtype[tags[j]]!=tagtype[tags[k]]:
#                             arr[j], arr[k] = arr[k], arr[j]
#                             tags[j], tags[k] = tags[k], tags[j]
#                             flag = 1
#                             break
#                     if flag:
#                         continue
#                     else:
#                         return ('No', arr, tags, tagtype)
#                 else:
#                     arr[j], arr[j+1] = arr[j+1], arr[j]
#                     tags[j], tags[j+1] = tags[j+1], tags[j]

#     return ('Yes', arr, tags, tagtype)

from sys import stdin, stdout
t = int(input())
for _ in range(t):
    n = int(input())
    alist = list(map(int, stdin.readline().strip().split()))
    blist = list(map(int, stdin.readline().strip().split()))

    if alist == sorted(alist):
        print('Yes')
    else:
        if 1 in blist and 0 in blist:
            print('Yes')
        else:
            print('No')
    # ans = bubbleSort(n, alist, blist)
    # if ans[0] == 'Yes':
    #     print(ans[0])
    # else:
    #     print(ans[0])
    #     # _, arr, tags, tagype = ans




