def search(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
    return False
    
print(search([2,3,4,5],6))