#for loop by using a while loop
# n=0
# while n<5:
#     print(n)
#     n=n+1

#for loop in python
# i=1
# for i in range(10):
#     print("a"*i)

#range(start, stop, step)
# for i in range(2, 10, 3):
#     print("b", i, "th time")

s="helloithere"

for i in range(len(s)):
    if s[i]=="i" or s[i]=="u":
        print("There is an i or u")
#or
for c in s:
    if c=="i":
        print("there is an i")

