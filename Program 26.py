#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
s=input("Enter a string: ")
pre=input("prefix: ")
suf=input("suffix: ")
if s.startswith(pre):
    print("string starts with a given prefix ",pre)
if s.endswith(suf):
    print("string starts with a given suffix ",suf)
