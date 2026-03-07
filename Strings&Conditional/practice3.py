# conditional statements
Marks_English = int(input("Enter your marks in English: "))
Marks_Maths = int(input("Enter your marks in Maths: "))
Marks_Science = int(input("Enter your marks in Science: "))
Marks_Language = int(input("Enter your marks in Language: "))  
Total_Marks = Marks_English + Marks_Maths + Marks_Science + Marks_Language
Percentage = (Total_Marks / 400) * 100
print("Your total marks are: ", Total_Marks)
print("Your percentage is: ", Percentage)

if Percentage >= 90 and Percentage <= 100:
    print("Grade: A")
elif Percentage >= 80 and Percentage < 90:
    print("Grade: B")
elif Percentage >= 70 and Percentage < 80:
    print("Grade: C")
elif Percentage >= 40 and Percentage < 70:
    print("Grade: D")  
elif Percentage <= 0:
    print("Invalid percentage. Please enter a valid marks to get a accurate result.")
else:
    print("You have failed the exam. Better luck next time!")