import random


class Animal:
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname=""):
        self.name=newname
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal): #-->inherits all the attributes of animal class
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)
c=Cat(3)
c.set_name("fluffy")
print(c.get_name())
print(c.speak())


class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other):
        diff=self.age-other.age
        print(abs(diff),"year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

p1=Person("jack",30)
p2=Person("jill",25)
print(p1.get_name)
print(p1.get_age)

class Student(Person):
    def __init__(self,name, age,major=None):
        Person.__init__(self, name, age)
        self.major=major
    def change_major(self,major):
        self.major=major
    def speak(self):
        r=random.random()
        if r<0.25:
            print("I have homework")
        elif 0.25<=r<0.5:
            print("I need sleep")
        elif 0.5<=r<0.75:
            print("I should eat")
        else:
            print("I am watching tv")
    def __str__(self):
        return "Student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

s1=Student("alice", 20, "CS")
s2=Student("beth",18)
print(s1.get_name())
s1.speak()
print(s2.get_name())
s2.speak()

