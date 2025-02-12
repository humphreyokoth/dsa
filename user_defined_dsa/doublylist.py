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

