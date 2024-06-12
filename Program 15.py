#15. Write a program that reads data from a CSV file and prints it to the console.
import csv
file=open("C:\\Users\\ivans\\OneDrive\\Desktop\\UNI\\DATA SCIENCE\\file.csv")
r=csv.reader(file)
for i in r:
    print(i)
