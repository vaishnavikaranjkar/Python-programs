#function calling another function
# def f1():
#     print("Inside function 1")

# def f2(a):
#     print("Inside function 2")
#     return a()

# print(f2(f1))

#nested functions
def f1(x):
    def f2():
        x="abc"
    x=x+1
    print("f1: x =", x)
    f2()
    return x

func=f1(3)
