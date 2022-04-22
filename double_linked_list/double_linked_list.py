from curses.panel import new_panel
from pandas import value_counts


class Node():

    def __init__(self,value) -> None:
        
        self.value = value
        self.next= None
        self.prev = None


def DoubleLikedList():

    def __init__(self,value):

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printline(self):

        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True


    def pop(self):
        # O(1)

        if self.length == 0:
            return None

        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1

        return temp

    def prepend(self,value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
        
        self.length += 1
        return True



