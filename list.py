#lists are mutable
l1=[1,4,5]
l1[1]=3
print("List 1",l1)

#add one element
l1.append(23)

#extend with another list
l2=[2,3,4,6]
print("List 2",l2)
l1.extend(l2)
print(l1)

#concetenate two lists
l3=l1+l2
print("List 3",l3)
