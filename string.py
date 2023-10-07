
#to get a random integer from given range of integers
# import random
# print(random.randint(2,63))

# #to get the class type of the value
# print(type(5.6)) 



# #using "," and "+" in a string
# print("hello", "there") #can concatenate values of different data type and puts a space in between two values
# print("hello"+"there") #need values in the same data type and doesnt put space


# #type casting
# x=1
# print(type(x))
# print(type(str(x)))


# x=str(input("Enter any number: "))
# print(x*5)


if("a">"5"):
    print("aaa")

#length of a string by len function
a="helo"
print(len(a)) #describes length of the string
print(a[1]) #describes first element of the string
print(a[-1]) #describes last element of the string
print(a[0:3:2]) #a[start:stop:step] --> slicing of a string
print(a[::]) # a[::] --> a[0:len(a):1]
print(a[::-1]) #a[::-1] --> a[-1:-(len(a)+1:-1)]
