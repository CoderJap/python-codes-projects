# Default Argument in python - 

def goodDay(name , ending="Thank You"):
  print(f"Good Day, {name}")
  print(ending)


goodDay("Japjot")

# This prints - 
# Good Day, Japjot
# Thank You

# iska matlab yeh hua ki agar maine ending ki value supply ki toh sahi func call ke time varna joh default value yaha di maine like Thank You voh use krlena 



# if supplied then 

def goodDay(name , ending="Thank You"):
  print(f"Good Day, {name}")
  print(ending)


goodDay("Japjot","Bye")

# This prints
# Good Day, Japjot
# Bye