name = "Faraz"
age = 36
print (name)
print (age)
print ("My name is " + name)


# type
a = 5
b = 3.14
c = None
print (type(a))
print (type(b))
print (type(c))
print(c)

#sum
x  = 34
y = 55
z = x + y
# v = x - y ctrl + / to comment it -shortcut
print (z)
# print (v)
print(type(z))
# print(type(v))

#arithmetic operators
a = 10
b = 3
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a // b) #floor division
print (a % b) #modulus - remainder
print (a ** b) #exponentiation - a to the power of b

#relational operators
print (a > b) #greater than
print (a < b) #less than
print (a >=b) #greater than or equal to
print (a <= b) #less than or equal to
print (a == b) #equal to
print (a != b) #not equal to

#assignment operators
num = 10
num1 = 11
num += 10 # num = num + 10
num1 -= 10 # num = num - 10
print ("Num is now: " + str(num))
print ("Num1 is now: " + str(num1))

#logical operators
x = 5
y = 10
print (x > 3 and y < 15) #and operator
print (x > 3 or y < 5) #or operator anyone should be true
print ( x >y and y < x) #and operator both should be true
print ( x == y or y > x) #or operator anyone should be true
print (not (x > y)) #not operator negates the condition

#type conversion
print ("Conversion topic")

a = 5
b = 3.14
c = a + b
print (c)
print (type(c))

#type casting
a = 5
b = str("51")
c = a + int(b)
print (c)
print (type(c))

#input function
name = input ("Enter your full name: ")
print ("Hello, " + name + ", Welcome to Python programming!")
