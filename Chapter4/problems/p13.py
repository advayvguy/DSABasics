from math import gcd

class Jug:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def clear(self):
        self.x = 0
        print("clearing ",self.y)
    
    def fill(self):
        self.x = self.y
        print("filling ",self.y)
    
    def transfer(self, to_jug):
        if self.x < to_jug.y - to_jug.x:
            to_jug.x += self.x
            self.x = 0
        else:
            self.x = self.x - (to_jug.y - to_jug.x)
            to_jug.x = to_jug.y
        print("transfering from ", self.y, " -> ", to_jug.y)

def draw2(big_jug, small_jug, amount):
    if big_jug.x == amount:
        print(amount, " litres obtained")
        return 

    #state machine
    if big_jug.x == 0:
        big_jug.fill()
    elif small_jug.x == small_jug.y:
        small_jug.clear()
    else:
        big_jug.transfer(small_jug)
    
    draw2(big_jug, small_jug, amount)

def main():
    big_jug = Jug(0,7)
    small_jug = Jug(0,5)
    amount = 3
    if (amount%gcd(big_jug.y,small_jug.y) != 0) or amount > big_jug.y:
        print("cant draw ",amount," amount of water")
    else:
        draw2(big_jug, small_jug, amount)
    
main()