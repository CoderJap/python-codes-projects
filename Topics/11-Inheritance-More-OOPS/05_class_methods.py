class Employee:
  a=1

  @classmethod
  def show(cls):
    print(f"The class attribute is {cls.a}")


e = Employee()
e.a=45

e.show()

# when using class method toh seedha aapko class attribute dekhega and not the instance attribute like this one and then u can use cls instead of self too for better undertstanding.
