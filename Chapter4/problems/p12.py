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

def draw2(big_jug, small_jug):
    big_jug.fill()
    big_jug.transfer(small_jug)

    if big_jug.x == 2:
        print("big jug has 2 litres")
        return
    
    small_jug.clear()
    big_jug.transfer(small_jug)
    draw2(big_jug, small_jug)

def main():
    big_jug = Jug(0,4)
    small_jug = Jug(0,3)
    draw2(big_jug, small_jug)
    
main()