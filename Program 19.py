#19. Write a python program that removes all punctuation from a given string.
import string

s=input("Enter a string: ")
s1=""
for i in s:
    if i not in string.punctuation:
        s1+=i
print(s1)
