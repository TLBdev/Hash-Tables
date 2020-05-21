import math
class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.copy = None
        self.entries = 0
        self.load_factor = 0
    def fnv1(self, key):
        fnv_hash = 14695981039346656037

        enc_key = key.encode()
        for e in enc_key:
            fnv_hash = fnv_hash ^ e
            fnv_hash = fnv_hash * 1099511628211
            
        
        return fnv_hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index] 
        if node == None:
            self.table[index] = HashTableEntry(key, value)
            self.entries += 1
            self.load_factor = self.entries / self.capacity
            print(value, self.load_factor)
            if self.load_factor > 0.7:
                self.capacity = math.ceil(self.capacity * 2)
                self.load_factor = self.entries / self.capacity
                self.resize(self.capacity)
        elif node.key == key:
            node.value = value
        else:
            while node != None:
                
                if node.key == key:
                    node.value = value
                    return
                elif node.next == None:
                    node.next = HashTableEntry(key, value)
                    self.entries += 1
                    self.load_factor = self.entries / self.capacity
                    print(value, self.load_factor)
                    if self.load_factor > 0.7:
                        self.capacity = math.ceil(self.capacity * 2)
                        self.load_factor = self.entries / self.capacity
                        self.resize(self.capacity)
                    return
                node = node.next
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index]
        prev = None 
        if node == None:
            return None
        elif node.key == key:
            if node.next == None:
                self.table[index] = None
                if self.load_factor < 0.2:
                    self.capacity = math.ceil(self.capacity * .5)
                    self.load_factor = self.entries / self.capacity
                    self.resize(self.capacity)
        else:
            while node.next != None:
                prev = node
                node = node.next
                if node.key == key:
                    prev.next = node.next
                    self.entries -= 1
                    self.load_factor = self.entries / self.capacity
                    if self.load_factor < 0.2:
                        self.capacity = math.ceil(self.capacity * .5)
                        self.load_factor = self.entries / self.capacity
                        self.resize(self.capacity)
                    return node
        if self.load_factor < 0.2:
            self.capacity = math.ceil(self.capacity * .5)
            self.load_factor = self.entries / self.capacity
            self.resize(self.capacity)
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index] 
        if node == None:
            return None
        elif node.key == key:
            
            return node.value
            
        else:
            while node != None:
                node = node.next
                if node == None:
                    return None
                if node.key == key:
                    
                    return node.value
                

    def resize(self, new_size):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        if self.load_factor < 0.2 and self.load_factor != 0:
            self.copy = self.table[:]
            
            self.table = [None] * new_size
          
            node = None
            
            for i in range(len(self.copy)):
                node = self.copy[i]
                if node != None:
                    while node != None:
                        self.put(node.key, node.value)
                        node = node.next
            self.copy = None
             
        
        if self.load_factor > 0.7:
            self.copy = self.table[:]
            self.capacity = math.ceil(self.capacity * 2)
            self.table = [None] * (self.capacity)
            
            

            node = None
            
            for i in range(len(self.copy)):
                node = self.copy[i]
                if node != None:
                    while node != None:
                        self.put(node.key, node.value)
                        node = node.next
            
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
