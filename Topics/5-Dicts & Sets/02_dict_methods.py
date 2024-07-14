marks ={
  "harry":100,
  "Shubham":56,
  "Rohan":23,
  0:"Harry"
  }

# print(marks.items()) #key-value pairs ki ek list dega
# print(marks.keys())
# print(marks.values())

# marks.update({"harry":99 , "Alex":78})
# print(marks) # original marks wali dict change ho jayegi since dicts are mutable 

print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error