# #break example
# while True:
#     name = input("Enter your name: ")
#     if name == "stop":
#         break
#     print("Hello " + name)

# #continue example
# while True:
#     name = input("enter your name: ")
#     if name == "faraz":
#         continue
#     print("Hello " + name)
#     if name == "stop":
#         break

char = "apna college"
for i in char:
    print(i)
    if i == "n":
        break
    else:
        continue

#print the element from the list using loops
mylist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in mylist:
    print(i)

# search of a number x in this tuple using list
mytuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# while True:
#     x = int(input("Enter a number to search: "))
#     if x in mytuple:
#         print("Found, well done")
#         break
#     else:
#         print("Not found, try again")

#range
my_range = range(5) #range(stop)
for i in my_range:
    print(i)
    
my_range1 = range(10, 15) #range(start, stop)
for i in my_range1:
    print(i)

my_range2 = range(0, 10, 2) #range(start, stop, step)
for i in my_range2:
    print(i)

#print 1 to 100 using range
for i in range(1, 101):
    print(i)

#print number 100 to 1 using range
for i in range(100, 0, -1):
    print(i)

#print multiplication table of number n
n = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))

n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
    
#pass
for i in range(5):
    pass
print("This is a placeholder for future code")
