class Employee:
  def __init__(self):
    print("Constructor of Employee")
  a=1

class Programmer(Employee):
  def __init__(self):
    print("Constructor of Programmer") 
  b=2

class Manager(Programmer): 
  def __init__(self):
    super().__init__() # beacuse of this now when obj of manager class is created tab programmer ka constructor bhi call hoga iske sath. (parent ka constructor bhi call hota hai when used super()__init__(). )
    print("Constructor of Manager")
  c=3

# o = Employee()
# o = Programmer()
o = Manager()


