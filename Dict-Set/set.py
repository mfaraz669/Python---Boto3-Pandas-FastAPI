#set 
collection = {1,2,3,4,5}
print(collection)
print(type(collection))

#empty set is not created by using empty curly braces because it will create an empty dictionary instead of an empty set. 
# To create an empty set, we need to use the set() function.
empty_set = {}
print(empty_set)
print(type(empty_set))

#null set
null_set = set()
print(null_set)
print(type(null_set))

#duplicate values are not allowed in set and the order of the elements is not preserved in set
collection1 = {1,2,3,4,5,1,2, "world", "hello", "world"}
collection1.add("python")
collection1.add("java")
collection1.remove(1)
#collection1.clear() it will remove all the elements from the set
collection1.pop() # it will remove an arbitrary element from the set
print(collection1)

# set union will return a new set that contains all the elements from both sets, without duplicates.
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

# set intersection will return a new set that contains only the elements that are present in both sets.
intersection_set = set1.intersection(set2)
print(intersection_set)
