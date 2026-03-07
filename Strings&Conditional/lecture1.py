value = "I am learning Python"
print(value[0])  # I
print(value.lower())  # i am learning python
print(value.upper())  # I AM LEARNING PYTHON
print(value.split())  # ['I', 'am', 'learning', 'Python']
print(value.find("on"))  # 17
print(value.replace("Python", "Java"))  # I am learning Java
print(value.partition("learning"))  # ('I am ', 'learning', ' Python')
print(value.startswith("I am"))  # True
print(value.endswith("Python"))  # True
print(value.casefold())  # i am learning python
print(value.isupper())  # False
print(value.islower())  # False
print(value.find("q"))  # -1 as index of "q" is not found and it returns -1
print(value.count("a"))  # 2
