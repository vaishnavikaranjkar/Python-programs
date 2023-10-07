#slowest sort is monkey sort/slowsort/bogo sort

def bubble_sort(L):
    swap=False
    count=0
    while not swap:
        swap=True
        for i in range(1,len(L)):
            if L[i-1]>L[i]:
                count+=1
                swap=False
                temp=L[i]
                L[i]=L[i-1]
                L[i-1]=temp
    return (L,count)

print(bubble_sort([2,4,5,6,3,1]))