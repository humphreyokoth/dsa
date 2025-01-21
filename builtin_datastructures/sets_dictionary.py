# set and dictionary are two data structures in python
# dictionary is a key value pair data structure
# dictionary ={key1: value1, key2: value2, key3: value3}
dict1 = {'name': 'John', 'age': 25, 'city': 'New York'}
print(dict1)

d ={1: 'apple', 2: 'banana', 3: 'orange'}
print(d)

d=dict()
# dictionary does not allow duplicate keys, if we try to add duplicate keys, it will overwrite the value
d[1] = 'apple'
# dictionaries are unordered, so we can not access the elements using index
d  = {"1":{1:2}}
print(d)


# Sets
# set is a collection of unique elements
# set is enclosed within the curly braces and elements are separated by comma
set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))
# sets we dont have key value pair, we have only values
# sets are unordered and unindexed
# set constructor
s=set()
print(s)

s = set([1, 2, 3, 4, 5])
print(s)
print(type(s))

# set does not allow duplicate elements
s = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(s)
print(type(s))
# set is mutable, we can add or remove elements from the set
s.add(6)
print(s)
s.remove(6)
print(s)
# set does not support indexing
# set does not support negative indexing
# set does not support nested set
# set does not support nested list
# set does not support nested tuple
# set does not support nested dictionary
# set does not support nested set
for i in s:
    print(i)


