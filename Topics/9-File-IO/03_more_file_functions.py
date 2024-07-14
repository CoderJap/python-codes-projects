f = open("lines.txt")

# lines = f.readlines() # This will read all lines straight up
# print(lines,type(lines))

line = f.readline() # This will read line one by one
while(line!=""):
  print(line)
  line = f.readline()

f.close()

