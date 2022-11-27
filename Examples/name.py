# name.py, Chapter 02, Python Crash Course
# program prints "ada lovelace"

name = "ada lovelace"
print(name.title()) # name is the variable
                    # title() is the method

name = "Ada Lovelace"
print(name.upper())
print(name.lower()) # name is the variable
                    # upper() is the method

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)


