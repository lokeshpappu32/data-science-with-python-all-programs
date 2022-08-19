'''#Python program to print the factorial of a given number.


#Using Loops

n=int(input("Enter a number :"))
fact=1
while n>0:
    fact=fact*n
    n=n-1

print(fact)
'''

#using functions (Iterative method)

n=int(input("Enter a number:"))

def facto(n):
    fact=1
    for i in range (1,n+1,1):
        fact=fact*i

    return fact

val=facto(n)
print(val)
'''
#using functions (Recursive Method)

n=int(input("Enter a number:"))
def facto(n):
  fact=1
  while(n>0):
    fact=fact*n
    n=n-1
  return fact

val=facto(n)
print(val)'''

