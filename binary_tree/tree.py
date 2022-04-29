def Node():

    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None

class Tree():

    def __init__(self):

        self.root = None

    def insert(self,value):
        # logn
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        # logn

        if self.root is None:
            return False
        
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value(self,temp):

        while temp.left is not None:
            temp = temp.left
        return temp


        


             