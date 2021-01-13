# link tables thru each other, can reverse it
class Node: 
    def __init__(self, value=None):
        self.value = value 
        self.nextvalue = None

class LinkedList:
    def __init__(self):
        self.head = None

list1 = LinkedList()
list1.head = Node('Blue')
e2 = Node('Red')
e3 = Node('Yellow')
#linking nodes together here
list1.head.nextvalue = e2
e2.nextvalue = e3

print(list1)
print(e2.value)
print(e3.value)