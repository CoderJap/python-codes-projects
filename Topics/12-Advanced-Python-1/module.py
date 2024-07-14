# __name__ evaluates to the name of the module in python from where the program is ran


def myFunc():
  print("Hello from module")


if __name__ == "__main__":
  # If this code is directly executed by running the file its present in 
  print("We are directly running this code")
  myFunc()
  print(__name__)
  



