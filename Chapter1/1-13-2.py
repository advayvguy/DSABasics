'''
            |- unary gate - not 
logic gate -
            |- binary gate - and, or
'''

class Logicgate:
    def __init__(self, lbl): #the 'self' here refers to the Andgate child class not this class itself.
                             #if logicgate is initialized directly then self is the logicgate class.
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.performlogic()
        return self.output
    
class Binarygate(Logicgate):
    def __init__(self,lbl):
        Logicgate.__init__(self,lbl)
        self.pin_a = None
        self.pin_b = None

    def get_a(self):
        if self.pin_a == None:
            return int(input(f"enter pin A for input gate {self.get_label()}:"))
        else:
            return self.pin_a.get_from().get_output()
    
    def get_b(self):
        if self.pin_b == None:
            return int(input(f"enter pin B for input gate {self.get_label()}:"))
        else:
            return self.pin_b.get_from().get_output()
    
    def set_pin(self,source):
        if self.pin_a == None:
            self.pin_a = source
        elif self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
    
class Unarygate(Logicgate):
    def __init__(self,lbl):
        Logicgate.__init__(self,lbl) #can be replaced by super().__init__(lbl)
        self.pin = None
    
    def get(self):
        if self.pin == None:
            return int(input(f"enter pin for input gate {self.get_label()}:"))
        else:
            return self.pin.get_from().get_output()
    
    def set_pin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
    
class Andgate(Binarygate):
    def __init__(self,lbl):
        super().__init__(lbl) #super here calls Binarygate

    def performlogic(self):
        a = self.get_a()
        b = self.get_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class Orgate(Binarygate):
    def __init__(self,lbl):
        super().__init__(lbl) #super here calls Binarygate

    def performlogic(self):
        a = self.get_a()
        b = self.get_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class Xor(Binarygate):
    def __init__(self,lbl):
        super().__init__(lbl) #super here calls Binarygate

    def performlogic(self):
        a = self.get_a()
        b = self.get_b()
        if (a == 1 and b == 1) or (a == 0 and b == 0):
            return 0
        else:
            return 1
        
class Notgate(Unarygate):
    def __init__(self,lbl):
        super().__init__(lbl) #super here calls unarygate

    def performlogic(self):
        a = self.get()
        if a == 1:
            return 0
        else:
            return 1

#to make a connecter 

class Connect:
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_pin(self)

    def get_from(self):
        return self.fromgate
    
    def get_to(self):
        return self.togate 

def main():
    g1 = Xor("g1")
    g2 = Notgate("g2")
    c1 = Connect(g1,g2)
    print(g2.get_output())
main()