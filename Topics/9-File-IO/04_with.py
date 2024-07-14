f = open("file1.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file1.txt","r") as f:
  print(f.read())


# you dony have to explicitly close the file now