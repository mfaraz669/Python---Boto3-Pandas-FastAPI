#find first 2 number sums
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

sum = first_number + second_number
print("The sum of the first two numbers is: ", sum)

#factorial of a first n number
n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is:", factorial)