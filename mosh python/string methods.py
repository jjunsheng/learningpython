#counting characters in string, can be use to count number of entry in a list
course = 'Python for Beginners'
print(len(course))

# . is a method
#original course variable did not change
print(course.upper())
print(course)
print(course.lower())

#find / replace character in a string
print(course.find('O'))
print(course.replace('Beginners' , 'Absolute Beginners'))
print(course.replace('o' , 'Absolute Beginners')) #lol ugly

#expression to find word in a string, diifferent approach, case sensitive*
print('Python' in course)

# !find method! return the index of the characters while !in method! give you boolean value

#print everything?
print(course.title())