def remove_dups(l1,l2):
    l1_copy=l1[:]
    for e in l1:
        if e in l2:
            l1_copy.remove(e)
    print(l1_copy)
L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups(L1,L2)