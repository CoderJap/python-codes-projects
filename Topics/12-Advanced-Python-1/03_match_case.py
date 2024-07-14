# just like switch statement 

def http_status(status):
  match status:
    case 200:
      return "Ok"
    case 404:
      return "Not found"
    case 500:
      return "Internal Server Error"
    case _: # default case
      return "Unknown status"
    
n = int(input("Enter http code: "))
print(http_status(n))