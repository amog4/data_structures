
import re


class Node():

    def __init__(self,value):
        
        self.value = value
        self.next = None



class LinkedList(Node):

    def __init__(self,value): 

        new_node = Node(value = value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
       
    
    def print_list(self):
        
        temp = self.head
        for _ in range(self.length):
            t = temp
            temp = t.next
            print(t.value)

        
    
    def append(self,value):
        # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = self.head
            self.tail = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        
        

    
    def pop(self):
        # O(N)
        
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None: 
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

       


    def prepend(self,value):
        # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = self.head
            self.tail = self.tail
        else:
            temp = self.head
            new_node.next = temp
            temp = new_node

        self.length += 1
        return True

        

    def pop_first(self):
        if self.length == 0:
            return None

        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp
        

    
    def get(self,index):
        # O(N)

        if index< 0 or index >= self.length:
            return None
        
        temp = self.head
        while _ in range(index):
            temp = temp.next
        
        return temp

    
    def set_values(self,value,index):
        # O(N)
        if index< 0 or index >= self.length:
            return True

        temp = self.head
        while _ in range(index):
            temp = temp.next

        if temp:
            temp.value = value
            return True
        return False
        

        
    def insert(self,index,value):
        # o(N)
        new_node = Node(value)
        if index< 0 or index >= self.length:
            return True

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        temp = self.get(index-1)
        pre = temp
        new_node.next = temp.next
        temp.next = new_node

        self.length +=1

        return True

        
        

    def remove(self,index): pass
        

    
    def reverse(self): 
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        while _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


      

        

        




 

my_linked_list = LinkedList(value=4)


my_linked_list.append(5)
my_linked_list.append(6)
#my_linked_list.pop()
#my_linked_list.pop_first()
print(my_linked_list.print_list())
print(my_linked_list.get(1))




