# usinf walrus operator 

# the walrus operator (:=), introduced in python 3.8, allows you to assign values to variables as part of an expression. 

if(n := len([1,2,3,4])) > 3:
  print(f"List is too long ({n} elements, expected < 3)")

# Output => List is too long (4 elements, expected < 3

# In this example, n is assigned the value of len([1,2,3,4]) and the used in the comparison within the if statement