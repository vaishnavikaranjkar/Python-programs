
a=input("Enter the word that you want me to cheer: ")
n=int(input("How enthusiastic are you: "))
aUp=a.upper()

for i in range(len(a)):
    print("Give me an",aUp[i],"!",aUp[i])

for i1 in range(n):
    print(aUp,"!!!")
