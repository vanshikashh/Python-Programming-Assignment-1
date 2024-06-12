#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
op=input("Enter the operator: ")
if op=="+":
    print("Sum: ",n1+n2)
elif op=="-":
    print("Difference: ",n1-n2)
elif op=="*":
    print("Product: ",n1*n2)
elif op=="/":
    print("Quotient: ",n1//n2)
    print("Remainder: ",n1%n2)
else:
    print("Wrong operator")
