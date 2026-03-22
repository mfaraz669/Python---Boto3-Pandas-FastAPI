#print the length of a list, list is a parameter

cities_list = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
def length_of_list(list):
    print(len(list))

length_of_list(cities_list)

#print the elements of a list in a single line

list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
def print_elements(list):
    for element in list:
        print(element, end=' ')
print_elements(list)

#find the factorial of a n
print("\nnew program")
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
       factorial *= i
    print(factorial)

factorial(5)

#find the usd conversion of a given amount in usd to inr
print("\nnew program")
def usd_to_inr(usd):
    inr = usd * 93
    print("INR value:",inr, "of USD:",usd)
usd_to_inr(107)

#write a number to find out the input function is even or odd
print("\nnew program")

def even_odd(n):
    if n % 2 == 0:
        print(n, "is an even number.")
    else:
        print(n, "is an odd number.")

input = int(input("Enter a number: "))
even_odd(input)