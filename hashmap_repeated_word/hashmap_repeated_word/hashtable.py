from .linked_list import LinkedList, Node

class Hashtables:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size 
    
    def get_hash(self, key):
        sum_of_asccii = 0
        for char in key:
            asccii_of_ch = ord(char)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 599
        hashed_key = temp_value % self.size
        return hashed_key
    
    def add(self, key):
        hashed_key = self.get_hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].append(key)
        
    def contains(self,key):
        hashed_key=self.get_hash(key)
        if self.map[hashed_key]:
            return self.map[hashed_key].includes(key)
        return False   

    def find(self, key):
        hashed_key=self.get_hash(key) 
        if self.map[hashed_key]:
           return self.map[hashed_key].return_value(key) 
        else:
            return None            

