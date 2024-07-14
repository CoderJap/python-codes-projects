class Employee:
  language = "Python"
  salary = 12000

harry = Employee()
harry.language = "Javascript"
print(harry.language,harry.salary)

# Note - instance attributes, take preference over class attributes during assignment and retrieval