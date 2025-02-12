class Node:
    def __init__(self,data):
         self.data = data
         self.nref = None
         self.pref = None


class doublyLL:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end = "")
                n = n.nref
    

    def print_LL_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "---->", end = "")
                n = n.pref

dl1 =   doublyLL()
dl1.print_LL()
dl1.print_LL_reverse()
# Doubely linked list  is a type of linked list in which each node apart from storing its data has two links. The first link points to the previous node in the linked list and the second link points to the next node in the linked list. The first node of the linked list has its previous link pointing to null similarly the last node of the linked list has its next link pointing to null.

# Add node to a doubely linked list.
def add_begin(self, data):
    new_node = Node(data)
    new_node.ref = self.head
    if self.head is not None:
        self.head.prev = new_node
    self.head = new_node
    new_node.prev = None

def add_end(self,data):
    new_node = Node(data)
    if self.head is None:
        new_node.prev = None
        self.head = new_node
    else:
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
        new_node.prev = n
        new_node.ref = None

def add_inbetween(self,data,x):
    if self.head is None:
        print("Linked list is empty")
        return
    new_node = Node(data)
    n = self.head
    while n is not None:
        if x == n.data:
            break
        n = n.ref
    if n is None:
        print("Node is not present in the linked list")
    else:
        new_node.ref = n.ref
        new_node.prev = n
        if n.ref is not None:
            n.ref.prev = new_node
        n.ref = new_node

def delete_begin(self):
    if self.head is None:
        print("Linked list is empty")
        return
    if self.head.ref is None:
        self.head = None
        return
    self.head = self.head.ref
    self.head.prev = None

def delete_end(self):
    if self.head is None:
        print("Linked list is empty")
        return
    if self.head.ref is None:
        self.head = None
        return
    n = self.head
    while n.ref is not None:
        n = n.ref
    n.prev.ref = None

def delete_by_value(self,x):
    if self.head is None:
        print("Linked list is empty")
        return
    if self.head.ref is None:
        if x == self.head.data:
            self.head = None
        else:
            print("Node is not present in the linked list")
        return
    if self.head.data == x:
        self.head = self.head.ref
        self.head.prev = None
        return
    n = self.head
    while n.ref is not None:
        if x == n.data:
            break
        n = n.ref
    if n.ref is not None:
        n.prev.ref = n.ref
        n.ref.prev = n.prev
    else:
        if n.data == x:
            n.prev.ref = None
        else:
            print("Node is not present in the linked list")



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(30)
LL1.add_inbetween(40,10)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(10)
LL1.print_LL()
