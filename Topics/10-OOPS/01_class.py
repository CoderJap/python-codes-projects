class Employee: #class kese bnate hai python mei
  language = "Python" #This is a class attribute
  salary = 120000

harry = Employee() #obj instantiated
Rohan = Employee()

harry.name = "Harry" # This is a instance attribute
Rohan.name = "Rohan"
print(harry.name,harry.language,harry.salary)

print(Rohan.name,Rohan.language , Rohan.salary)

# Here name is an instance attribute whereas language and salary are class attributes as they directly belong to the class