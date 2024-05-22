# Text Type  :	str
# variables
name = 's'
Name = "green"
age = 30
flower = "rose"

print(flower)


# Numeric Types  :	int, float, complex
ID = 30
tax = 10.5
a = 1j

# A variable name must start with a letter or the underscore character
_country = 'Bangladesh'
city = 'Dhaka'

# A variable name cannot start with a number
# 1email = "mail@gmail.com"

# A variable name can only contain alphaNumeric characters and underscores (A-z, 0-9, and _ )
student_1_Email = 'student1@gmail.com'

# Variable names are case-sensitive (age, Age and AGE are three different variables)
age = 20
Age = 30
AGE = 50

# Assign single values
fruit_1 = 'apple'
fruit_2 = 'orange'
fruit_3 = 'lemon'

# Assign multiple values
city_1, city_2, city_3 = "Dhaka", "NY", "Paris"

print(city_1)  # single variable print

print(city_2, city_3)  # multiple variables print NY Paris

print(city_1 + " " + city_2 + " " + city_3)  # Dhaka NY Paris

marks_1, marks_2, marks_3 = 30, 60, 90
print(marks_1 + marks_2)  # 3060 but result is 90

# print(city_1 + marks_1) # TypeError: can only concatenate str (not "int") to str

"""
+ : concatenate
+ : add
"""

print(city_1, marks_1)  # Dhaka 30

x = y = z = 'orange'
