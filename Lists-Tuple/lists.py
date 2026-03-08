marks = [23, 45, 67, 89, 90]
print(marks[1])
print(type(marks))

student = ["John", 21, "Computer Science", 87.5, True]
student[0] = "Jane"
print(type(student[4]))
print(student)
student.append("A+") # adds "A+" to the end of the list
print(student)
print(student[0:3]) # prints the first three elements of the list
print(student[-2:]) # prints the last two elements of the list
print(student[::2]) # prints every second element of the list
print(student[:4]) # prints the first four elements of the list
print(student[-4:-1]) # prints elements from index -1 to -3 (exclusive)

# append() method is used to add an element to the end of the list
list1 = [1, 2, 3]
list1.append(4)
print(list1)
list2 = [1, 4, 2, 4, 5]
list2.sort() # sorts the list in ascending order
print(list2)
# list2.reverse()
# print(list2) # reverses the order of the list
list2.insert(1, 8) # inserts 8 at index 1
print(list2)

list3 = [1, 2, 1, 3, 4, 5, 6]
list3.remove(1) # removes the first occurrence of 1 from the list
print(list3)
list3.pop(3) # removes the element at index 3 and returns it
print(list3)
