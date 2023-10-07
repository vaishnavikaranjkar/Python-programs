#
#class variables
#
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

class Rabbit(Animal):

    tag = 1 #class variable

    def __init__(self,age,parent1=None,parent2=None):
        Animal.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=Rabbit.tag
        Rabbit.tag+=1 

    def get_rid(self):
        return str(self.rid).zfill(3)#method on a string to pad the beginning with zeroes for example, 001 not 1

    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2

