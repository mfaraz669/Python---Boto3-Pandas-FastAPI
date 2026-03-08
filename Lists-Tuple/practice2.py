#palindrome checker in list
list1 = [1, 2, 3, 2, 1]
copy_list = list1.copy()
copy_list.reverse()

if list1 == copy_list:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
