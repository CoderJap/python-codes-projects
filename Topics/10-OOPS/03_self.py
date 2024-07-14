# self parameter 

class Employee:
  language = "Python"
  salary = 12000

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")
  
  @staticmethod # to avoid giving self in args
  def greet():
    print("Good morning")


harry = Employee()
# harry.language = "Javascript"

harry.getInfo()
# Employee.getInfo(harry)

harry.greet() # without self greet function would also have given error when this line would have been executed but now i have marked it as a static func