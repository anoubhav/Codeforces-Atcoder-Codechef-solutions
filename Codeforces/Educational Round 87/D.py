from sys import stdin, stdout
n, q = map(int, stdin.readline().strip().split())
alist = list(map(int, stdin.readline().strip().split()))
klist = list(map(int, stdin.readline().strip().split()))


# If the multiset is empty after all queries, print 0. Otherwise, print any integer that belongs to the resulting multiset.

# case1: multiset is empty when all queries are negative. PRINT 0
# case2: if the last query is positive, print that number. As that is added to multiset last.

if klist[-1]>0: 
    print(klist[-1])

elif all([k<0 for k in klist]):
    print('0')

else:
    # traversing in order is very important for this problem. Outer loop is O(n), can't be minimized.
    # the inner loop operations have to be made either logarithmic or constant.

    # using linkedlist + dictionary. We can do constant time insertion + deletion with linked list IFF we know where to do the operation. Dictionary allows us to locate the node in O(1), for deletion. (index, node): (key, value) pair.

    # for insertion of k into linked list. The index for inserting ki can be found using binary search on the node values. We can use the list(Dictionary.values().value).

    # to save memory we convert alist into a dictionary (index, node) + linkedlist. (node.value, node.next, node.prev). No additional memory is required so this should fit the contraints.

    # As a 10^6 sized list of ints (4 bytes) = 4 mb. We have klist (4mb), linkedlist(12mb), dictionary (8mb).
    # Total capacity is 25 mb.


    for k in klist:
        if k<0:
            # deletion index if given. So O(1) to find deletion location in list. 
            # But shifting of elements takes O(n). 
            # As n <=10**6, only a O(nlogn) solution will be accepted at best.
            pass
        
        
        elif k>0:
            # insertion location can be found int log n using binary search. 
            # But shifting of elements takes O(n) in list.
            pass





