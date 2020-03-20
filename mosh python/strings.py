# to add ' or " into string

course = "Python's Course for Beginners"
print(course)

course = 'Python Course for "Beginners"'
print(course)

course = '''
Hi JunSheng

Here is our first email to you.

Thank you,
The support team

'''
print(course)

course = 'Python Course for Beginners'
#         012345
#                                 -2-1
# 0:3 = 0 to 3
another = course[:]

print(another)