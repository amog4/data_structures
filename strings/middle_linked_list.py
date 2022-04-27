from pandas import value_counts


class Node():

    def __init__(self,value):

        self.value = value
        self.next = None
        
def middlenode(head:list):

    pre = head
    after = head

    while head.next:
        pre = pre.next
        after = after.next.next

    return pre
