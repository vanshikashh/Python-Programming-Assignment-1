#3. Write a python program that calculates the factorial of a given number.
n=int(input("Enter the number: "))
c=1
for i in range(1,n+1):
    c*=i
print("factorial is: ", c)
