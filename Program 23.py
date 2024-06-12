#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
temp=int(input("Enter the temperature: "))
unit=input("Enter the unit(C/F): ")
if unit=='C':
    f=(9*temp/5)+32
    print("Temperature in Fahrenheit: ", f)
elif unit=='F':
    c=(temp-32)*5/9
    print("Temperature in Celsius: ", c)
else:
    print("Enter correct unit!")
