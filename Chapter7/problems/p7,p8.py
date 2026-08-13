class containers:
    def __init__(self, big_jug, small_jug):
        self.big = 0
        self.small = 0
        self.big_capacity = big_jug
        self.small_capacity = small_jug

    def fill(self):
        self.small = self.small_capacity
    
    def empty_and_transfer(self):
        self.big = self.small
        self.small = 0
    
    def transfer(self):
        size_left = self.big_capacity - self.big
        if self.small <= size_left:
            self.big += self.small 
            self.small = 0
        else:
            self.big += size_left
            self.small -= size_left
    
    def big_full(self):
        return self.big == self.big_capacity
    
    def small_full(self):
        return self.small == self.small_capacity

def get_quantity(jugs, quantity):
    #maybe use a hashmap and initialize every key value to None. That way state checks would be O(1) instead of O(n)
    state_list = [(0,0)]
    
    while True:
        
        #state machine
        if jugs.big_full():
            jugs.empty_and_transfer()
        elif jugs.small_full():
            jugs.transfer()
        else:
            jugs.fill()

        if (jugs.big, jugs.small) in state_list:
            return None
        
        state_list.append((jugs.big, jugs.small))
        if jugs.big == quantity or jugs.small == quantity:
            return state_list

def jug_problem(size_small, size_big, quantity_to_fetch):
    jugs = containers(size_big, size_small)
    state_list = get_quantity(jugs, quantity_to_fetch)
    if state_list is None:
        print("quantity cant be fetched")
        return 
    for i in state_list:
        print(i)

jug_problem(5,11,9)
jug_problem(4,6,5)