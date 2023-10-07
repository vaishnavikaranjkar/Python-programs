#one female rabbit and one male rabbit, mate at age of one month, one month gestation

#adding previous two values

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(2))