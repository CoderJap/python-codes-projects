class Employee:
  company = "ITC"
  name="Default Name"
  salary=0

  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def show(self):
    print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Coder:
  language = "Pyhton"
  def printLanguage(self):
    print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee,Coder): # Code is inheriting from both employee class and coder class . this is an exmaple of multiple inheritance 
  company = "ITC Infotech"
  def showLanguage(self):
    print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("Prakash",120)
b = Programmer("Alex",12389)


a.show()
b.show()
