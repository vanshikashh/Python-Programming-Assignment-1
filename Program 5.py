#5. Write a program that takes a string input from the user and writes it to a text file.
s=input("Enter a string: ")
file=open("C:\\Users\\ivans\\OneDrive\\Desktop\\UNI\\pyth ML\\file.txt","w")
file.write(s)
file.close()
