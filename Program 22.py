#22. Write a python program that returns the minimum and maximum values in a list of numbers.
l=eval(input("Enter a list of numbers: "))
min=l[0]
max=l[0]
for i in l:
    if min>i:
        min=i
    if max<i:
        max=i
print("Minimum value: ", min)
print("Maximum value: ", max)    
