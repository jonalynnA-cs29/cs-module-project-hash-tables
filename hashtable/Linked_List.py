

# Linked List

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, key, value):
        node = Node(key, value)

        node.next = self.head
        self.head = node

    def find(self, key):
        current = self.head

        # walk down the ll
        while current is not None:
            # if the key of current is the key we are looking for
            if current.key == key:
                # Return current
                return current

            # Else: set current as the current's next node
            current = current.next

        # If nothing was found, return None
        return None

    def delete(self, key):
        current = self.head

        # Special case of deleting the head of the list
        if current.key == key:
            self.head = self.head.next
            return current

        # General case
        prev = current
        current = current.next

        while current is not None:
            if current.key == key:  # Delete this one
                prev.next = current.next
                return current

            else:
                prev = prev.next
                current = current.next

        # If nothing was found, return None
        return None

    def updateNode(self, key, value):

        node = self.find(key)
        node.value = value
