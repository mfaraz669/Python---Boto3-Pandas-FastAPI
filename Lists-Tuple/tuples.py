# Tuples are immutable sequences in Python, which means that once a tuple is created, 
# its elements cannot be changed, added, or removed. 
# They are defined using parentheses ().
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla)
print(type(tupla))
print(tupla[1:3])  # Slicing a tuple
# tupla.append(4)  # This will raise an error because tuples are immutable
print(tupla)
print(tupla.count(5))  # Count the number of occurrences of an element


#comma is necessary to create a tuple with a single element
single_element_tuple = (5,)
print(single_element_tuple)
print(type(single_element_tuple))

#without the comma, it will be treated as an integer
not_a_tuple = (5)
print(not_a_tuple)
print(type(not_a_tuple))   