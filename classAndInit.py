#to get distance between two points in 2d plane

class Coordinate(object):
    def __init__(self,x,y): 
        #__init__ is always executed when the class is being initiated
        #self parameter is a placeholder for the class object, OR it is a reference to the current instance of the class, and is used to access variables that belongs to the class
 
        self.x=x 
        self.y=y
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5

    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

#creating class objects
#parameters not including self
c=Coordinate(3,4) 
origin=Coordinate(0,0)
print("test",c.distance(origin))
print(origin.x)

#classes can also be used as
#along with self parameter
print(Coordinate.distance(c,origin))


#simple class and object example
# class MyClass():
#     x=5
# c1=MyClass()
# print(c1.x)
