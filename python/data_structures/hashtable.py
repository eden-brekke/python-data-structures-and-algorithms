from attr import has
from data_structures.linked_list import LinkedList
class Hashtable:

    def __init__(self, size=1024):
        # initialization here
        self.size = 1024
        self.buckets = [None] * self.size


    def hash(self, key):
        '''
        Arguments: key
        Returns: Index in the collection for that key
        '''
        if type(key) is str:
            hash_key = self.string_to_int_helper(key)
        elif type(key) is int:
            hash_key = key
        index = (hash_key * 599) % self.size
        print(index)
        return index

    def string_to_int_helper(self, string):
        '''
        Argument: String
        Returns: String converted to INT via ASCII values
        '''
        ascii_values = [ord(letter) for letter in string]
        return sum(ascii_values)

    def set(self, key, value):
        '''
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
        '''
        hash_index = self.hash(key)

        bucket = self.buckets[hash_index]

        if bucket is None:
            bucket = LinkedList()
            self.buckets[hash_index] = bucket

        bucket.append((key, value))


    def get(self, key):
        '''
        Arguments: key
        Returns: Value associated with that key in the table
        '''
        hash_index = self.hash(key)
        bucket = self.buckets[hash_index]

        current = bucket.head
        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]
            current = current.next
        return None



    def contains(self, key):
        '''
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        '''
        return bool(self.get(key))

    def keys(self):
        '''
        Returns: Collection of keys
        '''
        bucket = self.buckets[0]
        keys = {}
        current = bucket.head
        while current:
            pair = current.value
            current_key = pair[0]
            keys.add(current_key)
            current = current.next
        return keys
