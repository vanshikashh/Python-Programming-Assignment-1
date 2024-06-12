#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
flag=True
final=""
while flag:
    s=input("Enter line: ")
    if s=="":
        flag=False
    else:
        final+=s+'\n'
print("Lines read:", final, sep="\n")
