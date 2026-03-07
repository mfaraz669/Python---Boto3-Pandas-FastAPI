import random

marks = [random.randint(1, 100) for i in range(4)]

print("Marks:", marks)

total = sum(marks)
percentage = (total / 400) * 100

print("Total:", total)
print("Percentage:", percentage)