try:
    a=int(input("Enter a number:"))    
    b=int(input("Enter another number:"))
    assert b!=0
    print(a/b)
except ValueError:
    print("Couldn't convert to number.")
except ZeroDivisionError:
    print("can't divide by zero")
except:
    print("Invalid input from the user.")
else:
    print("No error in the code")
finally:
    print("Bye")

#else block is executed when execution of associated try block completes with no exceptions

#finally block is always executed after try, except and else clauses. Runs no matter what

#assertion error --> when assert is false, it stops the program right there and give assertion error
a=int(input("Enter a number:"))    
b=int(input("Enter another number:"))
assert b!=0
print(a/b)