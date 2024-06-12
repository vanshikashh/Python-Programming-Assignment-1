#21. Write a python program that counts the occurrences of a specific element in a list.
l=eval(input("Enter the list: "))
el=int(input("Enter the element: "))
c=0
for i in l:
    if i==el:
        c+=1
print("Number of occurences: ",c)
    
