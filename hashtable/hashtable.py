from Linked_List import LinkedList
from Linked_List import Node


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
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        length = len(self.capacity)
        return length

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hash = 14695981039346656037
        prime = 1099511628211

        key_bytes = key.encode()

        for byte in key_bytes:
            hash ^= byte
            hash *= prime
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Start from an arbitrary large prime
        hash_value = 5381
        # Bit-shift and sum value for each character
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value

    def hash_index_for_new_capacity(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the NEW hash table.
        """
        return self.fnv1(key) % self.resizingNewCapacity

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # increment size of hash table
        self.size += 1

        # compute index using hash function
        hash_index = self.hash_index(key)

        # if bucket at index is empty, create new node and insert
        node = self.storage[hash_index]
        if node is None:
            self.storage[hash_index] = HashTableEntry(key, value)
            return

        # if not empty, collision occured
        # iterate to end of list and add new node at end
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # compute hash
        # iterate linked listed of nodes, continue until found or end
        # if key is not found, return none
        # else remove node from linked list
        index = self.hash_index(key)
        node = self.storage[index]
        prev = node
        if node.key == key:
            self.storage[index] = node.next
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            print(f'{key} not found')
            return None
        else:
            self.size -= 1
            prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # compute index
        index = self.hash_index(key)

        # go to bucket at index
        node = self.storage[index]

        # iterate the nodes in linked list until key or end is found
        while node is not None and node.key != key:
            node = node.next

        # return the value if found, or none if not found
        if node is None:
            return None
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


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
