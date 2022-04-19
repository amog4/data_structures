from http.client import NETWORK_AUTHENTICATION_REQUIRED
import re
from requests import head


class Node():

    def __init__(self,value):
        
        self.value = value
        self.next = None



class LinkedList(Node):

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    
    def print_list(self):
        temp = self.head
        print(temp)
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def append(self,value):
        # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head =  new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

        return True

    
    def pop(self):
        # O(N)

        if self.lenght == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.lenght -= 1

        if self.lenght == 0:
            self.head = None
            self.tail = None




        

    def prepend(self,value):
        pass

    def inset(self,index,value):
        pass


 

my_linked_list = LinkedList(value=4)


print(my_linked_list.append(5))

print(my_linked_list.print_list())


