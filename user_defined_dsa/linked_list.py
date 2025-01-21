# linked list is chain of node in which each node contains data and a pointer to the next node
# Nodes are connected using pointers
# head /front is the first node of the linked list
# tail/end is the last node of the linked list which points to null

# its a dynamic data structure
# it is not stored in contiguous memory location. It is stored in random memory locations

# Advantages of linked list 
# 1. Dynamic data structure
# 2. Memory utilization is efficient
# 3. Insertion and deletion of elements are easy
# 4. Size of the linked list can be changed dynamically
# 5. Implementation is easy
# 6. No need to specify the size of the linked list
# 7.can be used to implement stack queue and graph
# 8.Respresent and manipulate polynomials.  Polynomial can be represented as a linked list where each node contains the coefficient and the power of the variable in the polynomial term.

# Disadvantages of linked list
# 1. Random access is not allowed. We have to access the elements sequentially starting from the head node.
# 2. Extra memory is required for the pointer to the next node.
# 3. Reverse traversing is difficult in a singly linked list.
# 4. Memory utilization is inefficient as pointers require extra memory.


# Types of linked list
# 1. Singly linked list
# 2. Doubly linked list
# 3. Circular linked list


# singly linked list
# is a chain of data structures where each data structure contains data and a pointer to the next data structure in the chain
# head is the first node of the linked list
# tail is the last node of the linked list which points to null
# singly linked list is a linear data structure
# singly linked list is a dynamic data structure
# singly linked list is not stored in contiguous memory locations
# singly linked list is not indexed
# singly linked list is not ordered
# singly linked list is not mutable
# singly linked list is not nested
# singly linked list is not nested list
# singly linked list is not nested tuple
# singly linked list is not nested dictionary
# singly linked list is not nested set

# Operations 
# 1. Insertion
# 2. Deletion
# 3. Traversing


# Adding elements to the linked list 
# 1. At the beginning of the linked list
# 2. At the end of the linked list
# 3. At the middle or inbetween of the linked list

# Adding elements to the linked list
# 1.Create a node
# 2.Change new node next to head
# 3.Point head to the new node

# Add element to the end of a linked list 
# 1. Create a node
# 2. Go to the last node
# 3. Change the next of the last node to the new node

# Add node inbetween two nodes
# 1. Create a node
# 2. Go to the previous node

# Deleting elements from the linked list
# 1. At the beginning of the linked list
# 2. At the end of the linked list
# 3. At the middle or inbetween of the linked list



# Traverse the linked list

# 1. Start from the head node
# 2. Traverse the linked list until we reach the last node



# singly linked list implementation
class Node :
    
     def __init__(self,data):
          self.data = data
          self.ref = None
 