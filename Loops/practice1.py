#print number from 1 to 100
count = 1
while count <= 100:
    print(count)
    count += 1

#print number from 100 to 1
count = 100
while count >= 1:
    print(count)
    count -= 1

# #print the multiplication table of n
# number = int(input("Enter a number to do multiplication table: "))
# for i in range(1, 11):
#     print(number, "x", i, "=", number * i)

#print the elements of the following list using a loop
list = [1,4,9,16,25,36,49,64,81,100]
for element in list:
    print(element)

#search for the number x in the tuple using loops
tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to search in the tuple: "))
for i in tuple:
    if i == x:
        print(x, "is found in the tuple.")
        break
else:
    print(x, "is not found in the tuple.")


