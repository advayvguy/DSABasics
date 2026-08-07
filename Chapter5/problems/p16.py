DELETED = object() #tombstone

class Hashtable:
    def __init__(self):
        self.size = 101
        self.slots = [None]*self.size
        self.data = [None]*self.size
        self.length = 0
        self.load_factor = 0.7
    
    def hash_function(self, key):
        return key%self.size
    
    def rehash(self, old_hash):
        return (old_hash + 1)%self.size
    
    def isfull(self):
        if self.length/self.size > self.load_factor:
            return 1
        return 0
    
    def scale(self):
        self.size *= 2
        new_slots = [None]*self.size
        new_data = [None]*self.size

        for i in range(len(self.slots)):
            if self.slots[i] == None or self.slots[i] == DELETED:
                continue
            index = self.hash_function(self.slots[i])
            while new_slots[index] != None:
                index = self.rehash(index)
            new_slots[index]= self.slots[i]
            new_data[index] = self.data[i]
        
        self.slots = new_slots
        self.data = new_data


    def put(self, key, data):
        if self.isfull():
            self.scale()

        index = self.hash_function(key)
        deleted = None

        if self.slots[index] == None:
            self.slots[index] = key
            self.data[index] = data
            self.length += 1
            return
        
        old_hash = index
        while self.slots[index] is not None:
            if self.slots[index] == DELETED and deleted == None: #we only want to overwrite the first tombstone we encounter
                deleted = index
            if self.slots[index] == key:
                self.data[index] = data
                return
            index = self.rehash(index)
            if old_hash == index:
                if deleted is not None:
                    break
                raise Exception("no space in map")
            
        if deleted is not None:
            self.slots[deleted] = key
            self.data[deleted] = data
        else:
            self.slots[index] = key
            self.data[index] = data
        self.length += 1

    def get(self, key):
        index = self.hash_function(key)
        if self.slots[index] == key:
            return self.data[index]
        
        old_hash = index
        while self.slots[index] != None:
            index = self.rehash(index)
            if self.slots[index] == key:
                return self.data[index]
            if old_hash == index:
                break
        raise ValueError("no such key in the hashtable")
    
    def delete(self, key):
        index = self.hash_function(key)
        old_hash = index
        while self.slots[index] != key:
            index = self.rehash(index)
            if index == old_hash:
                raise ValueError("key not in map")
        self.slots[index] = DELETED
        self.data[index] = None
        self.length -= 1

    
    def __len__(self):
        return self.length
    
    def __contains__(self, data):
        for i in self.data:
            if i == data:
                return True
        return False
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)