class Hashtable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size
    
    def hash_function(self, key):
        return key%self.size
    
    def rehash(self, old_hash):
        return (old_hash + 1)%self.size
    
    def put(self, key, data):
        index = self.hash_function(key)
        
        if self.slots[index] == None:
            self.slots[index] = key
            self.data[index] = data
            return 
        
        old_hash = index
        
        while (self.slots[index] != None):
            if self.slots[index] == key:
                self.data[index] = data
                return 
            index = self.rehash(index)
            if (index == old_hash):
                return
        
        self.data[index] = data
        self.slots[index] = key

    def get(self, key):
        start_slot = self.hash_function(key)
        if self.slots[start_slot] == key:
            return self.data[start_slot]
        
        slot = start_slot
        while(self.slots[slot] != key):
            slot = self.rehash(slot)
            if (slot == start_slot):
                return None
        
        return self.data[slot]
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
