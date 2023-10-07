class Fraction(object):
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    def __add__(self,other):
        top=self.num*other.denom+self.denom*other.num
        bot=self.denom*other.denom
        return Fraction(top,bot)
    def __sub__(self,other):
        top=self.num*other.denom-self.denom*other.num
        bot=self.denom*other.denom
        return Fraction(top,bot)
    def __float__(self):
        return self.num/self.denom
    def inverse(self):
        return Fraction(self.denom,self.num)

f1=Fraction(12,35)
f2=Fraction(25,33)
f=f1+f2
print(f)
print(float(f))
print(Fraction.__float__(f))
print(f1.inverse())
print(float(f2.inverse())) 