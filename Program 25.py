#25. Write a program that copies the contents of one text file to another.
f1=open("C:\\Users\\ivans\\OneDrive\\Desktop\\UNI\\pyth ML\\file.txt")
f2=open("C:\\Users\\ivans\\OneDrive\\Desktop\\UNI\\pyth ML\\file.txt","w")
s=f1.read()
f2.write(s)
