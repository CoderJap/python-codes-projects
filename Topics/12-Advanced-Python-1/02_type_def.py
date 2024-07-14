# To bring the roles of datatypes in python 

# ye batana ki konsa variable konse datatype ko store krega and konsa function konse dataype ko lega and also konse datatype ko return krega

n : int = 5

m: int = 7

name : str = "Harry"

def sum(a:int,b:int) -> int:
  return a+b

add: int = sum(m,n)
print(add)


# from typing import List, Tuple, Dict, Union

# # List of integers 
# numbers : List[int] = [1 , 2 , 3 , 4 , 5]

# # Tuple of a string and an integer
# person : Tuple[str , int] = ("Alice" , 30)

# # Dictionary with string keys and integer values
# scores : Dict[str , int] = {"Alice":90 , "Bob":85}

# # Union type for variables that can hold multiple values 
# identifier: Union[int , str] = "ID123"
# identifier = 12345 # Also valid 