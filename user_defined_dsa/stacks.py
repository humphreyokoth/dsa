# stacks are implemented using lists in python  
# stack is a collection of elements, which follows the LIFO order
# LIFO: Last In First Out
# stack is a linear data structure
# stack is a collection of elements, which follows the LIFO order

# stack operations 


# push: add an element to the top of the stack
# pop: remove an element from the top of the stack
# peek: get the top element of the stack without removing it
# is_empty: check if the stack is empty
# size: get the number of elements in the stack
# top: get the top element of the stack without removing it
# clear: remove all the elements from the stack

# push operation
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
# pop operation
stack.pop()
print(stack)
# peek operation
print(stack[-1])
# is_empty operation
print(len(stack) == 0)
# size operation
print(len(stack))
# top operation
print(stack[-1])
# clear operation
stack.clear()
print(stack)
print(len(stack) == 0)
# stack implementation using list
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop()
print(stack)
print(stack[-1])
print(len(stack) == 0)
print(len(stack))
print(stack[-1])
stack.clear()
print(stack)
print(len(stack) == 0)
# stack implementation using deque
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop()
print(stack)
print(stack[-1])
print(len(stack) == 0)
print(len(stack))
print(stack[-1])
stack.clear()
print(stack)
print(len(stack) == 0)
# stack implementation using queue module
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
print(stack)
stack.get()
print(stack)
print(stack.qsize())
print(stack.empty())
print(stack.full())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())