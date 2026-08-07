class Logicgate:
    def __init__(self,lbl):
        self.lbl = lbl
        self.out = None

    def get_out(self):
        self.out = self.perform_logic()
        return self.out

    def get_lbl(self):
        return self.lbl

class Unarygate(Logicgate):
    def __init__(self,lbl):
        Logicgate.__init__(self,lbl)
        self.pin = None

    def get(self):
        if (self.pin == None):
            return int(input("enter input for "+ self.get_lbl() +": "))
        else:
            return self.pin.get_from().get_out() #connector.get_from().get_out() = source.get_out()

    def set_next_pin(self,source):
        if (self.pin == None):
            self.pin = source
        else:
            print ("Cannot connect no empty pins")

class Binarygate(Logicgate):
    def __init__(self,lbl):
        Logicgate.__init__(self,lbl)
        self.pina = None
        self.pinb = None

    def geta(self):
        if (self.pina == None):
            return int(input("enter input for "+ self.get_lbl() +" (A): "))
        else:
            return self.pina.get_from().get_out() #connector.get_from().get_out() = source.get_out()

    def getb(self):
        if (self.pinb == None):
            return int(input("enter input for "+ self.get_lbl() +" (B): "))
        else:
            return self.pinb.get_from().get_out()

    def set_next_pin(self,source):
        if (self.pina == None):
            self.pina = source
        elif (self.pinb == None):
            self.pinb = source
        else:
            print ("Cannot connect: no empty pins")

class Notgate(Unarygate):
    def __init__(self,lbl):
        Unarygate.__init__(self,lbl)
    
    def perform_logic(self):
        if (self.get() == 1):
            return 0
        else:
            return 1

class AndGate(Binarygate):
    def __init__(self,lbl):
        Binarygate.__init__(self,lbl)
    
    def perform_logic(self):
        if (self.geta() == 1 and self.getb() == 1):
            return 1
        else:
            return 0

class OrGate(Binarygate):
    def __init__(self,lbl):
        Binarygate.__init__(self,lbl)
    
    def perform_logic(self):
        if (self.geta() == 1 or self.getb() == 1):
            return 1
        else:
            return 0

class XorGate(Binarygate):
    def __init__(self,lbl):
        Binarygate.__init__(self,lbl)
    
    def perform_logic(self):
        if ((self.geta() == 1 and self.getb() == 0) or (self.geta()==0 and self.getb() == 1)):
            return 1
        else:
            return 0

class Halfadder:
    def __init__(self,lbl):
        self.label = lbl
        self.pina = None 
        self.pinb = None
        self.sum = self.Sum(self)
        self.carry = self.Carry(self)

    def geta(self):
        if (self.pina == None):
            return int(input("enter input for "+self.lbl+"(A): "))
        else:
            return self.pina.get_from().get_out()
        
    def getb(self):
        if (self.pinb == None):
            return int(input("enter input for "+self.lbl+"(B): "))
        else:
            return self.pinb.get_from().get_out()
        
    class Sum:
        def __init__(self,main):
            self.main = main
        def get_out(self):
            a = self.main.geta()
            b = self.main.getb()
            if ((a==0 and b==1) or (a==1 and b ==0)):
                return 1
            else:
                return 0
            
    class Carry:
        def __init__(self,main):
            self.main = main

        def get_out(self):
            a = self.main.geta()
            b = self.main.getb()
            if (a == 1 and b == 1):
                return 1
            else:
                return 0

    def set_next_pin(self,source):
        if (self.pina == None):
            self.pina = source
        elif (self.pinb == None):
            self.pinb = source
        else:
            print ("Cannot connect: no empty pins")    
        

class Connector:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

        dest.set_next_pin(self)

    def get_from(self):
        return self.source
    
    def get_to(self):
        return self.dest

class Input: #sneaky 
    def __init__(self, lbl):
        self.lbl = lbl
        self.val = None 
    
    def get_out(self):
        if (self.val == None):
            self.val = int(input("enter value for "+ self.lbl + " : "))
        return self.val

h1 = Halfadder("h1")
h2 = Halfadder("h2")
i1 = Input("A")
i2 = Input("B")
ic = Input("Carry input")
c1 = Connector(i1,h1)
c2 = Connector(i2,h1)
c4 = Connector(h1.sum, h2)
c3 = Connector(ic,h2)
o =  OrGate("ogate")
c5 = Connector(h1.carry,o)
c6 = Connector(h2.carry,o)
print("sum:   ",h2.sum.get_out())
print("carry: ",o.get_out())