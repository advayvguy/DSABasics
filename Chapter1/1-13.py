#f1 == f2 if they are the reference to the same object <- shallow equality 
#deep equality -> the contents of the fraction class are the same

def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a/gcd(a,b))*b

class Fraction:
    #fraction 

    def __init__(self, top, down): #this is called while initialization
        self.num = top
        self.den= down
    
    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        if (self.num%self.den == 0):
            return "%d" %(self.num/self.den)
        return "%d/%d" %(self.num, self.den) #__str__ controls how the object behaves when its converted to a string

    def __add__(self, other):
        new_den = lcm(self.den, other.den)
        f1 = new_den/self.den
        f2 = new_den/other.den
        new_num = self.num*f1 + other.num*f2
        return Fraction(new_num,new_den)
    
    def __eq__(self, other): #when f1 == f2 is encountered- f1.__eq__(f2) is called
        c1 = self.num * other.den
        c2 = self.den * other.num 
        return c1 == c2

f1 = Fraction(1,4)
f2 = Fraction(11,4)

print(f1+f2)

f3 = Fraction(2,8)

print(f1 == f2)
print(f1 == f3)

