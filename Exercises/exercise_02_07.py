# exercise_02_07.py, Chapter 02, Python Crash Course
#
# Stripping Names: store a person's name, and include
# some whitespace characters at the beginning and end
# of the name. Make sure you use each character
# combination, "\t" and "\n", at least once.
#
# print the name once, so the whitespace around the
# name is displayed. Then print the name using each
# of the three stripping functions, lstrip(), rstrip(),
# and strip().
#
# compile and execute this file with the following 
# command-line script:
#
# $ python3 exercise_02_07.py

name1 = " eddie"
name2 = "alex "
name3 = " michael "
name4 = "  david"

# note: titlecase added for readability and to
# illustrate that methods can be chained together
print("List of original Van Halen members: " + "\n\t" + name1.lstrip().title() 
                                             + "\n\t" + name2.rstrip().title()
                                             + "\n\t" + name3.strip().title()
                                             + "\n\t" + name4.strip().title())


