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
            return int(input("enter input for "+self.label+"(A): "))
        else:
            return self.pina.get_from().get_out()
        
    def getb(self):
        if (self.pinb == None):
            return int(input("enter input for "+self.label+"(B): "))
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

#we are going to make a fulladder class from half adder classes
class Fulladder:
    def __init__(self,lbl):
        self.lbl = lbl
        self.sum = self.Sum(self)
        self.carry = self.Carry(self)
        self.h1 = Halfadder("h1:"+lbl)
        self.h2 = Halfadder("h2:"+lbl)
        self.cor = OrGate("o1:"+lbl)
        self.s1 = Connector(self.h1.sum,self.h2)
        self.c1 = Connector(self.h1.carry,self.cor)
        self.c2 = Connector(self.h2.carry,self.cor)
        self.i1 = None
        self.i2 = None
        self.i3 = None 
        self.pina = None
        self.pinb = None
        self.pinc = None 

    def geta(self):
        if (self.pina == None):
            return int(input("enter input for "+self.lbl+"(A): "))
        else:
            a = self.pina.get_from()
            self.i1 = Connector(a,self.h1)      
    
    def getb(self):
        if (self.pinb == None):
            return int(input("enter input for "+self.lbl+"(B): "))
        else:
            b = self.pinb.get_from()
            self.i2 = Connector(b,self.h1)
    
    def getc(self):
        if (self.pinc == None):
            return int(input("enter Carry input for "+self.lbl+"(C): "))
        else:
            c = self.pinc.get_from()
            self.i3 = Connector(c,self.h2)
        
    class Sum:
        def __init__(self,main):
            self.main = main

        def get_out(self,main):
            self.main.geta()
            self.main.getb()
            self.main.getc()
            return self.main.h2.sum.get_out()
              
    class Carry:
        def __init__(self,main):
            self.main = main
        
        def get_out(self):
            return self.main.cor.get_out()
    
    def set_next_pin(self,source):
        if (self.pina == None):
            self.pina = source
        elif (self.pinb == None):
            self.pinb = source
        elif (self.pinc == None):
            self.pinc = source
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
        if (self.val != 1 and self.val != 0):
            raise ValueError("Invalid Binary input to: "+self.lbl)
        return self.val

class Zero_Input:
    def __init__(self):
        self.val = 0
    
    def get_out(self):
        return 0

def ripple_carry_adder():
    
    #first we define our components

    i_initial_carry = Zero_Input()

    iA1 = Input("A(1)")
    iB1 = Input("B(1)")
    iA2 = Input("A(2)")
    iB2 = Input("B(2)")
    iA3 = Input("A(3)")
    iB3 = Input("B(3)")
    iA4 = Input("A(4)")
    iB4 = Input("B(4)")

    adder1 = Fulladder("Adder1")
    adder2 = Fulladder("Adder2")
    adder3 = Fulladder("Adder3")
    adder4 = Fulladder("Adder4")

    #now we make the connections from the inputs

    c1 = Connector(iA1,adder1)
    c2 = Connector(iB1,adder1)
    c3 = Connector(i_initial_carry,adder1)
    c4 = Connector(iA2,adder2)
    c5 = Connector(iB2,adder2)
    c6 = Connector(iA3,adder3)
    c7 = Connector(iB3,adder3)
    c8 = Connector(iA4,adder4)
    c9 = Connector(iB4,adder4)

    #now we feed the carries to the next adder

    d1 = Connector(adder1.carry,adder2)
    d2 = Connector(adder2.carry,adder3)
    d3 = Connector(adder3.carry,adder4)

    #now we fetch the outputs

    b1 = adder1.sum.get_out(adder1)
    b2 = adder2.sum.get_out(adder2)
    b3 = adder3.sum.get_out(adder3)
    b4 = adder4.sum.get_out(adder4)

    f1 = adder4.carry.get_out()

    print("-----------")
    print(f"sum = {b4}{b3}{b2}{b1}")
    print(f"carry = {f1}")
    print("-----------")
    print(f"in decimal:  {iA4.get_out()*8 + iA3.get_out()*4 + iA2.get_out()*2 + iA1.get_out()*1} + {iB4.get_out()*8 + iB3.get_out()*4 + iB2.get_out()*2 + iB1.get_out()*1} = {f1*16 + b4*8 + b3*4 + b2*2 + b1*1}")

ripple_carry_adder()
