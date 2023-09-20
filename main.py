
Name = input(' Student Name:' '')
id = input('id#:' '')
course = input(' Course:' '')
section = input(' Section:' '')



# Get the average of 4th quarter grades

FIRSTGRADES = eval(input("Enter the first grades: "))
SECONDGRAGES = eval(input("Enter the second grades: "))
THIRDGRAGES = eval(input("Enter the third grades: "))
FOURTHGRAGES = eval(input("Enter the fourth grades: "))

result = (FIRSTGRADES + SECONDGRAGES + THIRDGRAGES + FOURTHGRAGES ) / 4



print(Name)
print(id)
print(course)
print(section)


# GRADES OUTPUT

print(' First Grades:', FIRSTGRADES  )
print(' Second Grades:', SECONDGRAGES  )
print(' Third Grades:',THIRDGRAGES)
print(' Fourth Grades:',FOURTHGRAGES )
print('average grades: ', result)



