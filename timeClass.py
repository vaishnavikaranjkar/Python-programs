import time

def c_to_f(c):
    return c*9/5+32

t0=time.clock() #-->start the clock
print(c_to_f(1000))
t1=time.clock()-t0#-->stop the clock
print("t=",t0,":",t1,"s,")
