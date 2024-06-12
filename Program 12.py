#12. Write a python program that calculates the sum of the digits of a given number.
n=int(input("Enter a number: "))
c=0
for i in str(n):
    c+=int(i)
print("Sum of the digits: ", c)    
