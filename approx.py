cube = 1234
e = 0.01
guess = 0.0
inc = 0.0001
count = 0

while abs(guess**3 - cube) >=e and guess<cube:
    guess = guess+inc
    count = count+1

print("Guess count is:", count)
if abs(guess**3 - cube)>=e:
    print("Failed on cube root of",cube)
else:
    print(guess,"is close to the cube root of",cube)
