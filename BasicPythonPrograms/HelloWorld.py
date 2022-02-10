import re

name = input("Enter Your name: ")
if re.match("[A-Za-z]{3,}", name):
    print("Hello", name, "How are you?")
else:
    print("Entered name is incorrect!")

print("----End of Program-----")