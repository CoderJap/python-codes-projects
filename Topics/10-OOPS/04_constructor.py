class Employee:
  language = "Pyhton"
  salary = 12000

  def __init__(self , name , salary , language):
     # dunder method which is automatically called
     self.name = name
     self.language = language
     self.salary = salary
     print("I am creating an object")

  def getInfo(self):
    print(f"The language is  {self.language}.The salary is {self.salary}")


harry = Employee("Harry",13000,"C++")
print(harry.name , harry.language , harry.salary)

rohan = Employee("Rohan",5656,"Rust")
print(rohan.name , rohan.language , rohan.salary)
