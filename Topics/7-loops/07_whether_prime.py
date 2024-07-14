# check whether the entered number is prime or not 

n = int(input("Enter your number: "))

for i in range(2,n):
  if(n%i == 0):
      print("Number is not prime")
      break
else: 
    print("Number is prime")



#print() statement by default ek new line dedegi if u dont want that new line then write it as :
# print("whatever u have to write",end="") basically comman dalke end="" yeh likh dena new line nhi ayega fir