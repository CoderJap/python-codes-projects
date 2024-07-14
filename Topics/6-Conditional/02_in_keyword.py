# a = "Jap is a software engineer"
# print("Jap" in a )

# print("Rohan" in a )

# to detect some spam keywords in a comment 

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("Enter your comment: ")


if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
  print("This comment is a spam one")

else:
  print("This comment is not a spam")

# in keyword also works in lists

l = ["Harry" , "Rohan" , "Shubham", "Divya"]

name = input("Enter your name: ")

if(name in l):
  print("Your name is in the list")

else:
  print("Your name is not in the list")

  # to check if any post was talking about harry and now we have to handle with case sensitive behaviour of in keyword so we will use lower function 

  post = " Harry is nice guy but what are your thoughts about harry and how HaRRy is like HarRy"

  if("harry" in post.lower()):
    print("This post is talking about harry")

  else:
    print("This post isn't talking about harry")