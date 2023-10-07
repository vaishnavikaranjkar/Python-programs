#
#
#without init
#
#
class Robot:
    def introduce_self(self):
        print("My name is "+self.name) #self is temporary object created for the class
r1 = Robot() #r1 object created for class robot
#here self=r1
r1.name="Tom" #name is the attribute of r1 object
r1.introduce_self() #calling the function of class


#
#
#with init
#
#
class Pet:
    def __init__(self, name1, color1, weight1):
        self.name=name1
        self.color=color1
        self.weight=weight1
        
    def intro(self):
        print("My name is "+self.name)

p1 = Pet("brady", "blue", 30)
p2= Pet("cherry", "red", 20)

p1.intro()
p2.intro()