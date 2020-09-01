class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        # initial size of hash table
        self.hash_data = [None] * (self.capacity)
        # keeps count of hash table entries - adds or subtracts 
        self.entry = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # how big the table is
        return len(self.hash_data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # computes load factor to determine increase or decrease table size
        load_factor = self.entry / self.capacity
                       
        if not self.resize:
            # if load factor is greater than 0.7 increase size by 2
            if load_factor > 0.7:
                self.resize(int(self.capacity * 2))
            elif load_factor < 0.2 and self.capacity != MIN_CAPACITY:
                # if load factor is lower than 0.2 decrease size by 2
                self.resize(int(self.capacity / 2))
                
        return load_factor



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # hashing function
        hashed = 5381
        for c in key:
            hashed = (hashed * 33) + ord(c)
        return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # remainder of the hashing function stored as index
        index = self.hash_index(key)
        cur = self.hash_data[index]
        
        if cur:
            while cur.next != None and cur.key != key:
                cur = cur.next
            # if there is a key overwrite value
            if cur.key == key:
                cur.value = value
            # if key doesn't exist make a new entry and increase count
            else:
                cur.next = HashTableEntry(key, value)
                self.entry += 1
            
        else:
            # if nothing exists in cur make a new entry and increase count
            self.hash_data[index] = HashTableEntry(key, value)
            self.entry += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # remainder of the hashing function stored as index
        index = self.hash_index(key)
        cur = self.hash_data[index]
        
        # if value if empty - return
        if cur is None:
            return
        # loop to check cur.key == key, if there is set cur.next
        while cur:
            if cur.key == key:
                # changes pointer to another index, decrease entry by 1
                self.hash_data[index] = cur.next
                self.entry -= 1
            cur = cur.next
            
        return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        cur = self.hash_data[index]
        # if cur exists
        while cur:
            # checks current key, return value
            if cur.key == key:
                return cur.value
            # switches to next current to continue loop 
            cur = cur.next
        # if key doesn't exist return None
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
         # new_capacity is determine by get_load_factor()
        # creates new table
        new_table = HashTable(new_capacity)
        
        # creates new table and fills with data
        for i in self.hash_data:
            # when the loop reaches the end this runs
            if i != None and i.next == None:
                new_table.put(i.key, i.value)
            else:
                cur_node = i
                while cur_node != None:
                    # adds key value to new table while cur_node exists
                    new_table.put(cur_node.key, cur_node.value)
                    cur_node = cur_node.next
                    
        # updates to new capacity
        self.capacity = new_table.capacity
        self.hash_data = new_table.hash_data
        self.entry = new_table.entry
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
