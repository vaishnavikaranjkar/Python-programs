def selectionSort(L):
    suffixSt=0
    while suffixSt!=len(L):
        for i in range(suffixSt, len(L)):
            if L[i]<L[suffixSt]:
                L[suffixSt],L[i]=L[i], L[suffixSt]
        suffixSt+=1
    return L
print(selectionSort([2,35,6,46,1]))