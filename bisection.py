#cube root of a number by bisection method
cube = 000
high = cube
low = 0
count = 0
e = 0.01
guess = (high+low)/2.0

while(abs(guess**3-cube)>=e):
    if guess**3<cube:
        low=guess
    else:
        high=guess
    guess=(high+low)/2.0
    count = count+1

print("Guess count:",count)
print(guess,"is the closest value of cube root of",cube)

