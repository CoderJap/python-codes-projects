# for i in range(n): #0 to n-1
#   print(i)

'''
range func in python is used to generate a sequence og number 
we can also specify the start , stop and step-size(jump) as follows:

range(start,stop,step_size)
step_size is usually not used with range 
'''

# How to iterate list , tuples and strings using for loops 
print("Iterating Lists")
l = [1 , 4 , 6 , 234 , 6 , 764]

for i in l:
  print(i)

print("Iterating Tuples")

t = (6,231,75)

for i in t:
  print(i)

print("Iterating Strings")

s = "hARRY"

for i in s:
  print(i)
