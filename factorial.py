#function is called repeatedly inside the same function
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)
print(fact(4))