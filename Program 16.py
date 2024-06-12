#16. Write a program in python that counts the frequency of each character in a string.
s=input("Enter a string: ")
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("Frequency of each character is as follows: ")
for j in d:
    print("Frequency of ",j," is ",d[j])
