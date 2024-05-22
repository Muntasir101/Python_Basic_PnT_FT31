def summation(number1, number2):
    result = number1 + number2
    print(result)


summation(30, 10)


def greetings(employee_name='Someone'):
    print("Welcome To Our Company", employee_name)


greetings("Mr.Smith")
greetings()


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


# option 1
print(subtraction(30, 10))

# option 2
result = subtraction(50, 40)
print(result)

print(subtraction(20, 10) - multiplication(20, 10))

print(
    subtraction
        (
        100,  # number 1
        50  # number 2
    )
)
print(subtraction(multiplication(200, 10), multiplication(subtraction(50, 40), 10)))


def salary_calculate(employee_salary):
    return employee_salary


def bonus_calculate(employee_salary):
    return employee_salary * .10


print(bonus_calculate(salary_calculate(0)))
