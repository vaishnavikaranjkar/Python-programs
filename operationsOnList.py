#operations
l=[1,2,3,4]

#delete --> while spectifying index
del(l[2]) 
print(l)

#pop --> delete the last element
l.pop()
print(l)

#remove --> while specifying specific element
l.remove(1)
print(l)

#convert string into a list
s="Hello world"
list(s)
print(list(s))

#split list
print(s.split("o"))

#join
a=["a","c","j"]
join="".join(a)
print(join)
join="__".join(a)
print(join)

#sort list -->mutates the list
x=[4,543,2,1]
x.sort()
print(x)
x.sort(reverse = True) 
print(x)

#sorted list --> does not mutate list
print(sorted(x))
print(x)
#reverse the sorted list
print(sorted(x, reverse = True))

#cloning a list
list1=[23,34,45]
list2=list1[:]
print(list1,list2)