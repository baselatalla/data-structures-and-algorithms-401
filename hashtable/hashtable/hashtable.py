from hashtable.linked_list import LinkedList, Node

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
    
    def add(self, key, value):
        hashed_key = self.get_hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].append((key,value))
        
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



if __name__ == '__main__':
    # hashtable = Hashtables(1024)
    # hashtable = Hashtables(1024)
    # hashtable.add('good', True)
    # hashtable.add('doog', False)
    # print(hashtable.map[623])
    # hashtable.add('niv', 88)
    # hashtable.add('nin', 55)
    # hashtable.add('bib', False)
    # hashtable.add('rir', 'Hey women')
    # hashtable.add('course', 'Python-401d4')
    # print(hashtable.find('rir'))
    # for index, item in enumerate(hashtable.map):
    #     if item:
    #         print(index, item)
    hashtable = Hashtables(10)
    hashtable.add('niv', 88)
    for index, item in enumerate(hashtable.map):
        if item:
            actual = (index, item)
    print(actual[0], actual[1])