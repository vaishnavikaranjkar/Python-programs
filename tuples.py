#tuples --> immutable
t = (1, "b", "g")
print(type(t))

# #tuples are used to swap values conveniently
a = 1
b = 2
(a,b)=(b,a)
print(a)
print(b)

#used to return more than one value of the function
def quoAndRem(x,y):
    q=float(x//y)
    r=x%y
    return (q,r)
(q,r)=quoAndRem(4,5)
print((q,r))



