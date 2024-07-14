class Employee:
  a=1

class Programmer(Employee): # programmer inherits from employee
  b=2

class Manager(Programmer): # manager inherits from programmer 
  c=3

o = Manager()
print(o.a)
print(o.b)
print(o.c)


# This is an example of multi-level inheritance.