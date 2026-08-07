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
        if (down < 0):
            top = -top
            down = -down
        if (int(top) != top or int(down) != down):
            raise RuntimeError("non integral values for numerator/denominator")            
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
    
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
    
    def __sub__(self, other):
        new_den = lcm(self.den, other.den)
        f1 = new_den/self.den
        f2 = new_den/other.den
        new_num = self.num*f1 - other.num*f2
        return Fraction(new_num,new_den)
    
    def __mul__(self, other):
        new_den = self.den * other.den
        new_num = self.num * other.num
        hcf = gcd(new_den,new_num)
        new_den = new_den/hcf
        new_num = new_num/hcf
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other):
        new_den = self.den * other.num
        new_num = self.num * other.den 
        hcf = gcd(new_den, new_num)
        new_num = new_num/hcf
        new_den = new_den/hcf
        return Fraction(new_num, new_den)
    
    def __gt__(self,other):
        if (self.num*other.den > self.den*other.num):
            return 1
        else:
            return 0
    
    def __ge__(self,other):
        if (self.num*other.den >= self.den*other.num):
            return 1
        else:
            return 0
        
    def __lt__(self,other):
        if (self.num*other.den < self.den*other.num):
            return 1
        else:
            return 0
        
    def __le__(self,other):
        if (self.num*other.den <= self.den*other.num):
            return 1
        else:
            return 0

    def __ne__(self,other):
        if (self.num*other.den != self.den*other.num):
            return 1
        else:
            return 0 
        
    def __iadd__(self,other):
        d = self + other
        self.num = d.num
        self.den = d.den

