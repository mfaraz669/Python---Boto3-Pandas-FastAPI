#Enter marks for 3 subjects from user and store them in a dictionary
#start with empty dictionary and add key value pairs to it
marks = {}
input1 = int(input("Enter marks for maths: " ))
input2 = int(input("Enter marks for science: " ))
input3 = int(input("Enter marks for english: " ))

marks["maths"] = input1
marks["science"] = input2
marks["english"] = input3
print(marks)