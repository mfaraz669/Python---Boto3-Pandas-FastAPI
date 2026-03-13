#figure out the way to store the 9 and 9.0 as a seprate value in a set
my_set = {int(9), str(9.0)}
print(my_set) # {9, '9.0'} because 9 and 9.0 are considered different values in a set

my_set1 = {9, 9.0}
print(my_set1) # {9} because 9 and 9.0 are considered the same value in a set, and sets do not allow duplicate values.
