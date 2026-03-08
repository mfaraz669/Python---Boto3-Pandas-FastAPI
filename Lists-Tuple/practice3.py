#count the number of students with the "A" grade in the following tuple

grades = ("C", "D", "D", "A", "A", "B", "C", "A", "B", "D")
count_grades = grades.count("A")
print(count_grades)
print(type(grades))

grade_list = list(grades)
grade_list.sort()
print(grade_list)
