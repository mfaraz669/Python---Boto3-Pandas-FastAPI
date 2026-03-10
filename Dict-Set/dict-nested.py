student = {
    "name": "demo",
    "age": 20,
    "subjects": {
        "math": 90,
        "english": 85,
        "chemistry": 95
    }
}
print(student["name"])  # Output: demo
print(student["age"])   # Output: 20
print(student["subjects"]["math"])  # Output: 90
print(student.values())  # Output: dict_values(['demo', 20, {'math': 90, 'english': 85, 'chemistry': 95}])
print(student.keys())  # Output: dict_keys(['name', 'age', 'subjects'])
print(len(student["subjects"]))  # Output: 3
print(student.items())  # Output: dict_items([('name', 'demo'), ('age', 20), ('subjects', {'math': 90, 'english': 85, 'chemistry': 95})])
print(type(student.items()))  # Output: <class 'dict_items'>
print(student.get("subjects"))  # Output: {'math': 90, 'english': 85, 'chemistry': 95}
student.update({"grade": "A"})
print(student)  # Output: {'name': 'demo', 'age': 20, 'subjects': {'math': 90, 'english': 85, 'chemistry': 95}, 'grade': 'A'}

# Updating the name of the student using another dictionary
student2 = {
    "name": "demo2"
}
student.update(student2)
print(student)  # Output: {'name': 'demo2', 'age': 20, 'subjects': {'math': 90, 'english': 85, 'chemistry': 95}, 'grade': 'A'}