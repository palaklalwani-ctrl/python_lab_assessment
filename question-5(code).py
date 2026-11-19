n= int(input("Enter the value of n="))
def factorial(n):
  if n==0:
    return 1
  else:
    c= n*factorial(n-1)
    return c
print("Factorial is --->", factorial(n))
