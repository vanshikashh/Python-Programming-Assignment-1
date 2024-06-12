# 11. Write a python program that generates the first n numbers in the Fibonacci sequence.
n=int(input("Enter a number: "))
a=0
b=1
print("Fibonacci Series: ",a,b,end=" ")
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
